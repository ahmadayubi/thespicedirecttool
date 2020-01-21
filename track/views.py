from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Packager
from .forms import UserForm

app_name = 'track'


class HomeView(TemplateView):
    def get(self, request):
        form = UserForm
        packager = Packager.objects.order_by('name')[:5]
        total = 0
        for pack in packager:
            total += pack.quantity
        context = {
            'packager': packager,
            'form': form,
            'total': total,
            'show': False,
        }
        return render(request, 'index.html', context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            quant = form.cleaned_data['post']
            form = UserForm()
        if 'Yama' in request.POST:
            yama = Packager.objects.get(id=1)
            yama.quantity -= quant
            yama.packaged_can += quant
            yama.save()
            name = 'Yama'
        elif 'Zak' in request.POST:
            zak = Packager.objects.get(id=2)
            zak.quantity -= quant
            zak.packaged_can += quant
            zak.save()
            name = 'Zak'
        else:
            adil = Packager.objects.get(id=3)
            adil.quantity -= quant
            adil.packaged_can += quant
            adil.save()
            name = 'Adil'

        packager = Packager.objects.order_by('name')[:5]
        total = 0
        for pack in packager:
            total += pack.quantity
        context = {
            'packager': packager,
            'form': form,
            'show': True,
            'name': name,
            'total': total,
        }

        return render(request, 'index.html', context)
