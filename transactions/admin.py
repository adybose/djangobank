from django.contrib import admin

from .models import Deposit, Withdrawal, Interest


admin.site.register(Deposit)
admin.site.register(Withdrawal)
admin.site.register(Interest)
