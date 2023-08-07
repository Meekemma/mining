from django.contrib import admin
from .models import *

# Register your models here.

class  MiningHistoryAdmin(admin.ModelAdmin):
    list_display=('user_profile', 'cryptocurrency', 'mined_amount', 'mined_date')   

class MiningStatusAdmin(admin.ModelAdmin):
    list_display=('user_profile', 'cryptocurrency')

class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'created_on')    

class Testimonyadmin(admin.ModelAdmin):
    list_display=('name', 'created_on')

admin.site.register(Profile)
admin.site.register(Cryptocurrency)
admin.site.register(MiningStatus, MiningStatusAdmin)
admin.site.register(MiningHistory, MiningHistoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Testimony, Testimonyadmin)
admin.site.register(Withdrawal)
admin.site.register(Deposit)
admin.site.register(Invoice)
admin.site.register(Balance)

