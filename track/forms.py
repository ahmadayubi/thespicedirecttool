from django import forms
import datetime


class OrderForm(forms.Form):
    amount = forms.FloatField(max_value=10000, min_value=0)
    buyer = forms.CharField(max_length=100)
    order_id = forms.CharField(max_length=100)
    paid = forms.FloatField(max_value=100, min_value=0)
    date = forms.DateField(initial=datetime.date.today())


class ExpenseForm(forms.Form):
    reason = forms.CharField()
    amount = forms.FloatField(max_value=10000, min_value=0)
    date = forms.DateField(initial=datetime.date.today())


class SearchForm(forms.Form):
    order = forms.CharField()


class InvoiceForm(forms.Form):
    store = forms.CharField(max_length=50)
    date = forms.DateField(initial=datetime.date.today())
    invoice_id = forms.IntegerField(max_value=100000000, min_value=0)

    twoglass = forms.IntegerField(max_value=10000, min_value=0)
    oneglass = forms.IntegerField(max_value=10000, min_value=0)
    twocan = forms.IntegerField(max_value=10000, min_value=0)

    twoglass_p = forms.FloatField(max_value=10000, min_value=0)
    oneglass_p = forms.FloatField(max_value=10000, min_value=0)
    twocan_p = forms.FloatField(max_value=10000, min_value=0)
