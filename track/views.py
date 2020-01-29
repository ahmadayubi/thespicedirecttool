from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Order, Expense
from .forms import OrderForm, ExpenseForm

app_name = 'track'


class HomeView(TemplateView):
    def get(self, request):
        search = OrderForm()
        context = {
            'search': search,
        }
        ##
        # packager = Packager.objects.order_by('name')[:5]
        # total = 0
        # for pack in packager:
        #    total += pack.quantity
        # context = {
        #    'packager': packager,
        #    'form': form,
        #    'total': total,
        #    'show': False,
        #    'expForm': expForm,
        # }
        return render(request, 'index.html', context)

    def post(self, request):
        if 'FIND' in request.POST:
            searchForm = OrderForm(request.POST)
            if searchForm.is_valid():
                sOrder = searchForm.cleaned_data['order_id']
                fOrder = Order.objects.filter(order_id=sOrder)
                shipper = fOrder[0]
                context = {
                    'info': shipper,
                }
                print("HERE")
                return render(request, 'find.html', context)
        return render(request, 'index.html')


class ExpenseView(TemplateView):
    def get(self, request):
        exp = Expense.objects.all()
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
        search = OrderForm()
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
            searchForm = OrderForm(request.POST)
            if searchForm.is_valid():
                sOrder = searchForm.cleaned_data['order_id']
                fOrder = Order.objects.filter(order_id=sOrder)
                shipper = fOrder[0]
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
        searchForm = OrderForm()
        context = {
            'user': user,
            'type': bType,
            'search': searchForm,
        }

        return render(request, 'done.html', context)
