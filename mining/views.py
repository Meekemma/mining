import requests
import datetime
import json
import uuid
import os
import requests
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm,CreateUserForm,ProfileForm,DepositForm,WithdrawalForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .decorators import unaunthenticated_user,allowed_users,admin_only
from django.db.models import Q
from.models import *

# Create your views here.



#---------------------------REGISTER PAGE---------------------------------------------------

def register_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account successfully created for ' + username)

            template = render_to_string('mining/email_template.html', {'username': username})

            email = EmailMessage(
                'Welcome to Climax Trade Investment',
                template,
                settings.EMAIL_HOST_USER,
                [user.profile.email],
            )
            email.fail_silently = False
            email.send()

            return redirect('login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'mining/register.html', context)




def register_with_referrer_view(request, referral_code,pk):
    try:
        profile =Profile.objects.get(id=pk)
        referrer = Referral.objects.filter(referral_code=referral_code, profile=profile).first()

         # Store referral information in session
        request.session['referral_code'] = referral_code
        request.session['referrer_pk'] = referrer.profile.pk if referrer else None

    except Profile.DoesNotExist:
        return HttpResponse("Referrer does not exist")    

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account successfully created for ' + username)

            template = render_to_string('mining/email_template.html', {'username': username})

            email = EmailMessage(
                'Welcome to Climax Trade Investment',
                template,
                settings.EMAIL_HOST_USER,
                [user.profile.email],
            )
            email.fail_silently = False
            email.send()

            return redirect('login')
    else:
        form = CreateUserForm()

    context = {'form': form, 'referrer':referrer}
    return render(request, 'mining/register.html', context)



#-------------------------LOGIN PAGE----------------------------------------

def login_page(request):
    user=None

    if request.method == 'POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        messages.info(request, 'Username OR password is incorrect')

    context={}
    return render(request, 'mining/login.html', context)


#-------------------------------LOGOUT PAGE-------------------------------------
def logoutUser(request):
    logout(request)
    return redirect('login')




#----------------------INDEX PAGE---------------------------------------------------
def index(request):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'a0793b59-f4e6-4304-9fb0-0cc8596588b5',
    }

    response = requests.get(url, headers=headers, params=parameters)

    if response.status_code == 200:
        data = response.json()

        prices = {}
        for item in data['data']:
            name = item['name']
            symbol = item['symbol']
            price = item['quote']['USD']['price']
            circulating_supply = item['circulating_supply']

            prices[symbol] = {
                'price': price,
                'name': name,
                'circulating_supply': circulating_supply,
            }

        
        
    else:
         return JsonResponse({'error': 'Unable to fetch data'}, status=response.status_code)
        
    context = {'prices': prices}
    return render(request, 'mining/index.html', context)

#------------------------ABOUT -PAGE-----------------------------------------------
def about_info(request):


    domain_name = 'Authentic investment.com'
    context = {'domain_name':domain_name}
    return render(request, 'mining/about.html', context)



#------------------------diversity -PAGE-----------------------------------------------
def diversity_info(request):


    context = {}
    return render(request, 'mining/diversity.html', context)

#------------------------ Sponsoring PAGE-----------------------------------------------
def sponsoring_info(request):


    context = {}
    return render(request, 'mining/sponsoring.html', context)

#------------------------ TERMS PAGE-----------------------------------------------
def term_info(request):


    context = {}
    return render(request, 'mining/terms.html', context)

#------------------------ Sponsoring PAGE-----------------------------------------------
def privacy_info(request):


    context = {}
    return render(request, 'mining/privacy.html', context)



#------------------------CONTACT -PAGE-----------------------------------------------
def contact_info(request):
    
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name =form.cleaned_data['name']
            email =form.cleaned_data['email']
            body =form.cleaned_data['body']
            
            send_mail(
                name,
                body,
                settings.EMAIL_HOST_USER,
                ['meek.emma007@gmail.com'],
                fail_silently=False,
                )
            form.save()
            messages.success(request, "Thank you for reaching out to you")
            return redirect('contact')

    else:
        form=ContactForm()
    context={'form':form}
    return render(request, 'mining/contact.html',  context)



#------------------------PROFILE -PAGE-----------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def profile_settings(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method =='POST':
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        
    context={'form':form, 'profile':profile}
    return render(request, 'mining/profile.html', context)



def exchanged_rate(amount):
    url = "https://www.blockonomics.co/api/price?currency=USD"
    r = requests.get(url)
    response = r.json()
    return amount/response['price']





#------------------------DEPOSIT -PAGE-----------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def deposit_info(request):
    profile = request.user.profile
    if request.user.is_authenticated:
        if request.method=='POST':
            form=DepositForm(request.POST)
            if form.is_valid():
                form.instance.profile = request.user.profile
                form.save()
                return redirect('create_payment',  pk=form.instance.id)
            
        else:
            form=DepositForm()

    context={'form':form}
    return render(request, 'mining/deposit.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def track_invoice(request, pk):
    profile = request.user.profile
    invoice =Invoice.objects.get(id=pk, profile=profile)
    data = {
            'order_id':invoice.order_id,
            'bits':invoice.btcvalue/1e8,
            'value':invoice.deposit.deposit_amount,
            'addr': invoice.address,
            'status':Invoice.STATUS_CHOICES[invoice.status+1][1],
            'invoice_status': invoice.status,
        }
    if (invoice.received):
        data['paid'] =  invoice.received/1e8
        if (int(invoice.btcvalue) <= int(invoice.received)):
            invoice.status = 2
            invoice.save()

            # Sending email notification
            template = render_to_string('mining/email_template.html', {'user': invoice.profile.user})

            email = EmailMessage(
                'Invoice Payment Confirmation',
                template,
                settings.EMAIL_HOST_USER,
                [invoice.profile.user.email],  # Use the correct field for the user's email
            )
            email.fail_silently = False
            email.send()
    else:
        data['paid'] = 0  


    context={'invoice':invoice, 'data':data}
    return render(request,'mining/invoice.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def create_payment(request, pk):
    deposit = Deposit.objects.get(id=pk)

    api_key = 'HdXGsI89PlYAaRq4aNpdurBKsDlEejh67VswUaDzcEg'
    url = 'https://www.blockonomics.co/api/new_address'

    headers = {'Authorization': "Bearer " + api_key}
    r = requests.post(url, headers=headers)
    print(r.json())
    if r.status_code == 200:
        address = r.json()['address']
        print ('Payment receiving address ' + address)
        bits = exchanged_rate(float(deposit.deposit_amount))
        print("bits:",bits)
        order_id = uuid.uuid1()
        invoice = Invoice.objects.create(order_id=order_id, address=address, btcvalue=bits*1e8, deposit=deposit)
        return HttpResponseRedirect(reverse('invoice', kwargs={'pk':invoice.id}))
    else:
        print(r.status_code, r.text)
        return HttpResponse("Error while creating payment", status=500)
    

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def receive_payment(request):
    
    if (request.method != 'GET'):
        return 
    
    txid  = request.GET.get('txid')
    value = request.GET.get('value')
    status = request.GET.get('status')
    addr = request.GET.get('addr')

    invoice = Invoice.objects.get(address = addr)
    
    invoice.status = int(status)
    if (int(status) == 2):
        invoice.received = value
    invoice.txid = txid
    invoice.save()  






#-------------------------------------DASHBOARD-----------------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def dashboard(request):
    if request.user.is_authenticated:
        profile = request.user.profile

         # Replace with the actual user
        total_deposits = profile.deposit_set.filter(status='p').aggregate(total=models.Sum('deposit_amount'))['total'] or 0

        
        pending_withdrawals = Withdrawal.objects.filter(profile=profile, status='P')
        completed_withdrawals = Withdrawal.objects.filter(profile=profile, status='C')
        

    context = {
        'total_deposits': total_deposits,
        'pending_withdrawals': pending_withdrawals,
        'completed_withdrawals': completed_withdrawals,
    }
    return render(request, 'mining/dashboard.html', context)



#-------------------------------------TRANSACTION-----------------------------------------------------
def transactionPage(request):
    if request.user.is_authenticated:
        profile = request.user.profile

        deposits = Deposit.objects.filter(Q(profile=profile),Q(status='C') | Q(status='P')
        
)

        
    
            
    context={'deposits':deposits}
    return render(request, 'mining/transaction.html', context)

#-------------------------------------WITHDRAWAL-----------------------------------------------------


def withdrawal_info(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = WithdrawalForm(request.POST)
            if form.is_valid():
                withdrawal_amount = form.cleaned_data['withdrawal_amount']
                wallet = form.cleaned_data['wallet']
                pin = form.cleaned_data['pin']

                withdrawal_instance = form.save(commit=False)
                withdrawal_instance.profile = request.user.profile
                withdrawal_instance.save()

                # Sending Email notification
                template = render_to_string('mining/email_template.html', {'user': withdrawal_instance.profile.user})
                
                email = EmailMessage(
                    'Withdrawal in process',
                    template,
                    settings.EMAIL_HOST_USER,
                    [withdrawal_instance.profile.user.email]  # Use the email field of the user
                )
                email.fail_silently = False
                email.send()

                return redirect('dashboard')
            
        else:
            form = WithdrawalForm()    
    domain_name = 'Authentic investment.com'
    context = {'form': form ,'domain_name':domain_name}
    return render(request, 'mining/withdrawal.html', context)
        




def support_page(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            subject = request.POST['subject']
            priority = request.POST['Priority']  # Use the correct name attribute
            details = request.POST['details']

            send_mail(
                subject,  # Use the subject variable
                details,  # Use the details variable
                settings.EMAIL_HOST_USER,
                ['meek.emma007@gmail.com'],
                fail_silently=False,
            )
            messages.add_message(request, messages.SUCCESS, 'Support request submitted successfully.', extra_tags='support_request')
            return redirect('support')
            
    context={}
    return render(request, 'mining/support.html', context)



def plan_view(request):
    
            
    context={}
    return render(request, 'mining/plans.html', context)


def share_view(request):
    
            
    context={}
    return render(request, 'mining/share.html', context)


def referal_view(request):
    
            
    context={}
    return render(request, 'mining/referral.html', context)