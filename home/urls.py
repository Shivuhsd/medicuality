from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('setting/', views.AppSetting, name="setting"),
    path('logout/', views.LogoutPage, name='LogoutPage'),
    path('register/', views.Register, name='register'),
    path('search/', views.Search, name='search'),
    path('billing/<str:pk>/', views.Billing, name='billing'),
    path('view_bill/<str:pk>/', views.View_bill, name='view_bill'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('patient_view/<str:pk>/', views.Patient_view, name='patient_view'),
    path('profile/<str:pk>/', views.MyProfile, name='myprofile'),
    path('salesregister/', views.salesRegister, name='salesregister'),
    path('customers/', views.Customer, name='customer'),
    path('editbill/<str:pk>/', views.EditBill, name='editbill'),
]