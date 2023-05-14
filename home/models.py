from django.db import models

# Create your models here.

# A Class to store patient Information
class Patient_info(models.Model):
    patient_name = models.CharField(max_length=200, null=True)
    patient_phone = models.CharField(max_length=15, null=True)
    patient_gst_no  = models.CharField(max_length=200, null=True)
    patient_adress_1 = models.CharField(max_length=200, null=True)
    patient_address_2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pin = models.CharField(max_length=6, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.patient_name

# A Class to store Payment Detals
class Payment_info(models.Model):
    patient_id = models.ForeignKey(Patient_info, on_delete=models.CASCADE, null=True)
    payment_details = models.TextField(null=True)
    activity = models.TextField(null=True)
    billing_address_1 = models.CharField(max_length=200, null=True)
    billing_address_2 = models.CharField(max_length=200, null=True)
    billing_address_city = models.CharField(max_length=200, null=True)
    billing_address_state = models.CharField(max_length=200, null=True)
    billing_address_pin = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    c_gst = models.IntegerField(null=True)
    s_gst = models.IntegerField(null=True)
    total_amount = models.IntegerField(null=True)
    status = models.CharField(max_length=200, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
        
        

    def __str__(self):
        return self.payment_details
    

#merchant Settings

class Merchant(models.Model):
    mobile = models.IntegerField(null=False)
    gst = models.CharField(max_length=50, null=False)
    c_gst = models.IntegerField(blank=True, null=False)
    s_gst = models.IntegerField(blank=False)

    def __str__(self):
        return self.gst
    