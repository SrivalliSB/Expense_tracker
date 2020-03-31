from django.urls import path
from trackall.views import dashboard,get_all_expense,get_all_income, get_all_wallet, create_wallet, create_expense, create_income, delete_wallet, delete_expense, delete_income, edit_wallet, edit_expense, edit_income
urlpatterns =[
    path("dashboard/",dashboard),
    path("wallet/",get_all_wallet),
    path("expense/",get_all_expense),
    path("income/",get_all_income),
    path("create_wallet/", create_wallet),
    path("create_expense/", create_expense),
    path("create_income/", create_income),
    path("delete_wallet/<int:wallet_id>/", delete_wallet),
    path("delete_expense/<int:expense_id>/", delete_expense),
    path("delete_income/<int:income_id>/", delete_income),
    path("edit_wallet/<int:wallet_id>/", edit_wallet),
    path("edit_expense/<int:expense_id>/", edit_expense),
    path("edit_income/<int:income_id>/", edit_income),
]