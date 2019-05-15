from django.contrib import admin

from .models import Deposit, Withdrawal


admin.site.register(Deposit)
admin.site.register(Withdrawal)
