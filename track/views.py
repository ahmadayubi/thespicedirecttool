from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Order, Expense, Invoice
from .forms import OrderForm, ExpenseForm, SearchForm, InvoiceForm

app_name = 'track'


class SplashView(TemplateView):
    def get(self, request):
        return render(request, 'splash.html')


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
                buyerN = orderForm.cleaned_data['buyer']
                quant = orderForm.cleaned_data['amount']
                oID = orderForm.cleaned_data['order_id']
                paid = orderForm.cleaned_data['paid']
                date = orderForm.cleaned_data['date']
                newOrder = Order(name=user, order_id=oID,
                                 amount_paid=paid, date=date, quantity=quant, buyer=buyerN)
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
            'search': searchForm,
        }

        return render(request, 'done.html', context)


class StoreView(TemplateView):
    def get(self, request):
        form = InvoiceForm()
        view = SearchForm()
        invoice = Invoice.objects.all().order_by('-date')
        context = {
            'form': form,
            'invoices': invoice,
            'view': view,
        }
        return render(request, 'store.html', context)

    def post(self, request):
        view = SearchForm(request.POST)
        if 'ADD' in request.POST:
            invoiceForm = InvoiceForm(request.POST)
            if invoiceForm.is_valid():
                store = invoiceForm.cleaned_data['store']
                iID = invoiceForm.cleaned_data['invoice_id']

                oneGlass = invoiceForm.cleaned_data['oneglass']
                twoGlass = invoiceForm.cleaned_data['twoglass']
                twoTin = invoiceForm.cleaned_data['twocan']

                oneGlassP = invoiceForm.cleaned_data['oneglass_p']
                twoGlassP = invoiceForm.cleaned_data['twoglass_p']
                twoTinP = invoiceForm.cleaned_data['twocan_p']

                total = (oneGlass*oneGlassP) + \
                    (twoGlass*twoGlassP) + (twoTin*twoTinP)
                date = invoiceForm.cleaned_data['date']

                newInvoice = Invoice(store=store, invoice_id=iID,
                                     oneglass=oneGlass, oneglass_p=oneGlassP, twoglass=twoGlass, twoglass_p=twoGlassP,
                                     twocan=twoTin, twocan_p=twoTinP, date=date, total=total)
                newInvoice.save()
                return render(request, 'done.html')
        else:
            if view.is_valid():
                sOrder = view.cleaned_data['order']
                fOrder = Invoice.objects.filter(invoice_id=sOrder)
                shipper = list(fOrder)
                if len(shipper) > 0:
                    glassTotal = shipper[0].oneglass_p*shipper[0].oneglass + \
                        shipper[0].twoglass_p*shipper[0].twoglass
                    canTotal = shipper[0].twocan*shipper[0].twocan_p

                context = {
                    'info': shipper,
                    'gTotal': glassTotal,
                    'cTotal': canTotal,

                }
                return render(request, 'invoice.html', context)
