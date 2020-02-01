from django import forms
import datetime


class OrderForm(forms.Form):
    amount = forms.FloatField(max_value=10000, min_value=0)
    order_id = forms.CharField(max_length=100)
    paid = forms.FloatField(max_value=100, min_value=0)
    date = forms.DateField(initial=datetime.date.today())


class ExpenseForm(forms.Form):
    reason = forms.CharField()
    amount = forms.FloatField(max_value=10000, min_value=0)
    date = forms.DateField(initial=datetime.date.today())


class SearchForm(forms.Form):
    order = forms.CharField()
