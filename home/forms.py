from .models import Merchant, Payment_info
from django.forms import ModelForm
from django.contrib.auth.models import User

class MyMerchant(ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'


class Profile(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name' , 'last_name')


class EditForm(ModelForm):
    class Meta:
        model = Payment_info
        fields = ('payment_details', 'activity', 'billing_address_1', 'billing_address_2', 'billing_address_city', 'billing_address_state', 'billing_address_pin','amount','status')