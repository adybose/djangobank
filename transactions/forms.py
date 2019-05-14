from django import forms

from .models import Deposit, Withdraw


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ["amount"]


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ["amount"]
