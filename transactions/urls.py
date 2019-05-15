from django.conf.urls import url

from transactions.views import MyTransictions

urlpatterns = [

    url('deposit', MyTransictions.diposit_view, name='deposit'),
    url('withdrawal', MyTransictions.withdrawal_view, name='withdrawal'),
]
