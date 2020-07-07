from django.urls import path
from . import send_sms
from . import receive_sms
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_sms',send_sms.run, name='send_sms'),
    path('sms',receive_sms.sms_reply, name='receive_sms'),
]
