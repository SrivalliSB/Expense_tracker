from django.contrib import admin
from .models import Expense, Income, Wallet

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Wallet)