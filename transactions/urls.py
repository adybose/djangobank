from django.conf.urls import url

from transactions.views import MyTransactions

urlpatterns = [

    url('deposit', MyTransactions.diposit_view, name='deposit'),
    url('withdraw', MyTransactions.withdrawal_view, name='withdraw'),
]
