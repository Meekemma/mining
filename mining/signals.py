import uuid

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .models import Profile,Referral



def generate_referral_code():
    code = str(uuid.uuid4()).replace("-", "")[:7]
    return code


@receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group =Group.objects.get(name='customer')
        instance.groups.add(group)

        # Create a customer profile
        profile=Profile.objects.create(
				user=instance,
                first_name=instance.first_name,
                last_name=instance.last_name,
                username=instance.username,
                email=instance.email,
                  
		)

        Referral.objects.create(
            profile=profile, 
            referral_code=generate_referral_code()
            )
                

post_save.connect(customer_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created == False:
        try:
            instance.profile.save()
            print('Profile updated!!!')
        except:
            Profile.objects.create(user=instance)
            print('Profile created for existing')

post_save.connect(update_profile, sender=User)