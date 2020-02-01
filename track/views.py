from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Order, Expense
from .forms import OrderForm, ExpenseForm, SearchForm

app_name = 'track'


class HomeView(TemplateView):
    def get(self, request):
        search = SearchForm()
        reOrder = Order.objects.all().order_by('-date')[:5]
        context = {
            'search': search,
            'orders': reOrder,
        }

        return render(request, 'index.html', context)

    def post(self, request):
        if 'FIND' in request.POST:
            searchForm = SearchForm(request.POST)
            if searchForm.is_valid():
                sOrder = searchForm.cleaned_data['order']
                fOrder = Order.objects.filter(order_id=sOrder)
                shipper = list(fOrder)
                context = {
                    'info': shipper,
                }
                return render(request, 'find.html', context)
        return render(request, 'index.html')


class ExpenseView(TemplateView):
    def get(self, request):
        exp = Expense.objects.all().order_by('-date')
        cont = {
            'expenses': exp,
        }
        return render(request, 'expense.html', cont)


class UserView(TemplateView):
    def get(self, request, id):

        user = ''
        if id == 1:
            user = 'Adil'
        elif id == 2:
            user = 'Zak'
        else:
            user = 'Yama'
        search = SearchForm()
        orderForm = OrderForm()
        expForm = ExpenseForm()
        expForm.name = user
        orderForm.name = user

        exp = Expense.objects.filter(name=user)
        order = Order.objects.filter(name=user)
        cont = {
            'expenses': exp,
            'orders': order,
            'user': user,
            'orderF': orderForm,
            'expF': expForm,
            'search': search,
        }
        return render(request, 'user.html', cont)

    def post(self, request, id):
        user = ''
        if id == 1:
            user = 'Adil'
        elif id == 2:
            user = 'Zak'
        else:
            user = 'Yama'
        bType = False
        if 'ORDER' in request.POST:
            orderForm = OrderForm(request.POST)
            if orderForm.is_valid():
                quant = orderForm.cleaned_data['amount']
                oID = orderForm.cleaned_data['order_id']
                paid = orderForm.cleaned_data['paid']
                date = orderForm.cleaned_data['date']
                newOrder = Order(name=user, order_id=oID,
                                 amount_paid=paid, date=date, quantity=quant)
                newOrder.save()
        if 'FIND' in request.POST:
            searchForm = SearchForm(request.POST)
            if searchForm.is_valid():
                sOrder = searchForm.cleaned_data['order']
                fOrder = Order.objects.filter(order_id=sOrder)
                shipper = list(fOrder)
                context = {
                    'info': shipper,
                }
                return render(request, 'find.html', context)
        else:
            expForm = ExpenseForm(request.POST)
            if expForm.is_valid():
                am = expForm.cleaned_data['amount']
                re = expForm.cleaned_data['reason']
                date = expForm.cleaned_data['date']
                newExp = Expense(name=user, reason=re, date=date, amount=am)
                newExp.save()
                bType = True
        searchForm = SearchForm()
        context = {
            'user': user,
            'type': bType,
            'search': searchForm,
        }

        return render(request, 'done.html', context)
