from django.contrib import admin
from . models import Patient_info, Payment_info, Merchant

# Register your models here.

admin.site.register(Patient_info)
admin.site.register(Payment_info)
