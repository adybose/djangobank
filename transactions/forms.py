from django import forms

from .models import Deposit, Withdrawal


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ["amount"]


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ["amount"]
