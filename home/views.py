from django.shortcuts import render, redirect
from . models import Patient_info, Payment_info, Merchant
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyMerchant, Profile, EditForm
from django.db.models import Sum, Q
from .cusFunc import CreateList, G_Total, Total, Check
from django.core.paginator import Paginator

# Create your views here.


@login_required(login_url = 'loginPage')
def LogoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url = 'loginPage')
def home(request):
    return render(request, 'home.html')

@login_required(login_url = 'loginPage')
def Register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        gst = request.POST['gst']
        adr_1 = request.POST['address-1']
        adr_2 = request.POST['address-2']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        re = Check(gst)
        print(re)
        if(re==True):
            Patient = Patient_info(patient_name = name, patient_phone = phone, patient_gst_no=gst.upper(), patient_adress_1=adr_1, patient_address_2 = adr_2, city=city, state=state, pin=pin)
            Patient.save()
            h = Patient_info.objects.filter(Q(patient_gst_no = gst.upper()))
            return render(request, 'tick.html', {'h':h})
            
        else:
             messages.error(request, "Entered GST NO Already Exists, Check Credentials OR Search for Customer in Customer Tab")
    return render(request, 'register.html')


@login_required(login_url = 'loginPage')
def Search(request):
    if request.method == 'POST':
        searched= request.POST['q']
        result = Patient_info.objects.filter(Q (patient_name__contains = searched) | Q(patient_gst_no__contains = searched) | Q(patient_phone__contains = searched) | Q(city = searched)).order_by('created_on')
        context = {'result':result}
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

@login_required(login_url = 'loginPage')
def Billing(request,pk):
    p_d = Patient_info.objects.get(id=pk)
    mer = Merchant.objects.get()
    if request.method == 'POST':
        choice = request.POST['choice']
        payment_details = request.POST['payment_details']
        activity = request.POST['activity']
        total_amt = request.POST['amount']
        status = request.POST['status']

        if(choice == '1'):
            adress1 = p_d.patient_adress_1
            address2 = p_d.patient_address_2
            city = p_d.city
            state = p_d.state
            pin = p_d.pin

        elif(choice == '2'):
            adress1 = request.POST['address-1']
            address2 = request.POST['address-2']
            city = request.POST['city']
            state = request.POST['state']
            pin = request.POST['pin']
             
        c_gst = ((int(total_amt)*int(mer.c_gst))/100)
        s_gst = ((int(total_amt)*int(mer.s_gst))/100)
        amount = (int(c_gst) + int(s_gst) + int(total_amt))
        payment = Payment_info(patient_id = p_d, payment_details = payment_details, activity=activity, billing_address_1 = adress1, billing_address_2 = address2, billing_address_city = city, billing_address_state = state, billing_address_pin = pin, c_gst = c_gst, s_gst=s_gst, total_amount = total_amt, amount=amount, status=status)
        payment.save()
        return redirect('search')
    else:
        return render(request, 'billing.html', {'p_d':p_d})

@login_required(login_url='loginPage')
def EditBill(request, pk):
    info = Payment_info.objects.get(id=pk)
    h = Patient_info.objects.get(id = info.patient_id.id)
    form = EditForm(instance=info)
    if request.method == 'POST':
         form = EditForm(request.POST, instance=info)
         if form.is_valid():
            rem = form.save()
            return redirect('search')

    return render(request, 'editbill.html', {'form':form, 'h':h})

@login_required(login_url = 'loginPage')
def Patient_view(request, pk):
    p_info = Patient_info.objects.get(id=pk)
    pay_info = Payment_info.objects.filter(patient_id = pk)
    print(pay_info)
    context = {'p_info':p_info, 'pay_info':pay_info}
    return render(request, 'patient_view.html', context)

@login_required(login_url = 'loginPage')
def View_bill(request, pk):
    pay_info = Payment_info.objects.get(id=pk)
    print(pay_info)
    p_id = pay_info.patient_id

    p_info = Patient_info.objects.get(patient_name=p_id)

    m_info = Merchant.objects.get()
    context = {'p_info': p_info, 'pay_info':pay_info, 'm_info':m_info}
    return render(request, 'view.html', context)

@login_required(login_url = 'loginPage')
def dashboard(request):
    t_order = Payment_info.objects.count()
    t_cus = Patient_info.objects.count()
    t_sum = Payment_info.objects.aggregate(Sum('amount'))
    p_info = Payment_info.objects.all().order_by('-time_stamp')[0:10]
    context = {'t_order':t_order, 't_cus':t_cus, 'sum':t_sum, 'p_info':p_info}
    print(p_info)
    return render(request, 'index.html' , context)

@login_required(login_url = 'loginPage')
def AppSetting(request):
    info = Merchant.objects.get()
    form = MyMerchant(instance=info)
    if request.method == 'POST':
        form = MyMerchant(request.POST, instance=info)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated Succesfully")
        else:
            messages.error(request, "Something Went Wrong")
            form = MyMerchant
    return render(request, 'setting.html', {'form':form})


#Sales Register

def salesRegister(request):
    start_date = None
    end_date = None
    lst = None
    records = None
    g_total = None
    total = None
    cus_info = Patient_info.objects.all()
    if request.method == 'POST':
        start_date = request.POST['fdate']
        end_date = request.POST['tdate']
        records = Payment_info.objects.filter(time_stamp__date__range=(start_date, end_date))
        print(records)
        lst = CreateList(records)
        g_total = G_Total(records)
        total = Total(records, start_date, end_date)
    
    return render(request, 'recors.html', {'records':records, 'lst':lst, 'cus_info':cus_info, 'g_total':g_total, 'total':total, 'start':start_date, 'end':end_date})

#End Sales Register




@login_required(login_url='loginPage')
def Customer(request):
    posts = Patient_info.objects.all() # fetching all post objects from database
    p = Paginator(posts, 7) # creating a paginator object
	# getting the desired page number from url
    # 
    page_number = request.GET.get('page')
	
    try:
	    page_obj = p.get_page(page_number) # returns the desired page object
	
    except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
	    page_obj = p.page(1)
	
    except EmptyPage:
		# if page is empty then return last page
	    page_obj = p.page(p.num_pages)
            
    context = {'page_obj': page_obj}
	# sending the page object to index.html
    return render(request, 'cus.html', context)


@login_required(login_url = 'loginPage')
def MyProfile(request, pk):
    info = User.objects.get(id=pk)
    form = Profile(instance=info)
    if request.method == 'POST':
        form = Profile(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            messages.error(request, "Something went wrong")
    return render(request, 'profile.html', {'form':form})


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except :
            messages.error(request, "User Does Not Exist")
            
            

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Check Your Credentials")
    return render(request, 'login.html')
