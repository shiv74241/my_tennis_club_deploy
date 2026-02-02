from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  
    path('admin/', admin.site.urls),
    path('abouts/', views.abouts, name='abouts'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/', views.members, name='members'),
    path('testing/', views.testing, name='testing'),
    path('testing2/', views.members2, name='members2'),
    path('submit_form/', views.handle_form, name='submit_form'),
    path("students/", views.student_list, name="student_list"),
    path('vest-products/', views.vest_products, name='vest_products'),
    path('payment/cod/', views.payment_cod, name='payment_cod'),
    path('payment/bank/', views.payment_bank, name='payment_bank'),
    path("pay/", views.upi_payment, name="upi_payment"),
    ]


    