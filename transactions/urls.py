from django.conf.urls import url

from transactions.views import MyTransactions

urlpatterns = [

    url('deposit', MyTransactions.deposit_view, name='deposit'),
    url('withdrawal', MyTransactions.withdrawal_view, name='withdrawal'),
]
