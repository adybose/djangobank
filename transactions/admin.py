from django.contrib import admin

from .models import Diposit, Withdrawal, Interest


admin.site.register(Diposit)
admin.site.register(Withdrawal)
admin.site.register(Interest)
