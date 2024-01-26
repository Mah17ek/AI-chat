from django.urls import path 
from app1.views import Index,login_pag,create_account,Forget_password,otp,password,bot

urlpatterns = [
    path('index/',Index),
    path('log/',login_pag,name='log'),
    path('acc/',create_account,name='crete'),
    path('for/',Forget_password,name='for'),
    path('bot/',bot,name='bot'),
    path('otp/',otp,name='otp'),
    path('pass/',password,name='pwd')
]