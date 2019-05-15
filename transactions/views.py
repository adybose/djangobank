from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from .forms import DepositForm, WithdrawalForm

class MyTransactions(View):

    @login_required()
    def deposit_view(request):
        if not request.user.is_authenticated:
            raise Http404
        else:
            title = "Deposit"
            form = DepositForm(request.POST or None)

            if form.is_valid():
                deposit = form.save(commit=False)
                deposit.user = request.user
                deposit.user.balance += deposit.amount
                deposit.user.save()
                deposit.save()
                messages.success(request, 'You Have Deposited {} ₹.'
                             .format(deposit.amount))
                return redirect("home")

            context = {
                    "title": title,
                    "form": form
                  }
            return render(request, "transactions/form.html", context)


    @login_required()
    def withdrawal_view(request):
        if not request.user.is_authenticated:
            raise Http404
        else:
            title = "Withdrawal"
            form = WithdrawalForm(request.POST or None)

            if form.is_valid():
                withdrawal = form.save(commit=False)
                withdrawal.user = request.user


                if withdrawal.user.balance >= withdrawal.amount:

                    withdrawal.user.balance -= withdrawal.amount
                    withdrawal.user.save()
                    withdrawal.save()
                    messages.error(request, 'You Have Withdrawn {} ₹.'
                               .format(withdrawal.amount))
                    return redirect("home")

                else:
                    messages.error(
                    request,
                    'You Can Not Withdraw More Than You Balance.'
                    )

            context = {
                    "title": title,
                    "form": form
                  }
            return render(request, "transactions/form.html", context)
