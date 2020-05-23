from django.urls import path
from . import views
app_name='Bussinessapp'

#Create Your Urls Path here
urlpatterns = [
    path('products/',views.products,name='products'),
    path('contact_us/',views.contact_us,name='contact_us')
]
