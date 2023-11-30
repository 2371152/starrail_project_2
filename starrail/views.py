from django.shortcuts import render
from django.views.generic import ListView
from accounts.models import StrategyModel

# Create your views here.


def mypage_view(request):
    return render(request, 'mypage.html')


class StrategyList(ListView):
    template_name = 'index.html'
    queryset = StrategyModel.objects.all()


class Universe_3View(ListView):
    template_name = 'universe_3.html'
    queryset = StrategyModel.objects.all()


class Universe_4View(ListView):
    template_name = 'universe_4.html'
    queryset = StrategyModel.objects.all()


class Universe_5View(ListView):
    template_name = 'universe_5.html'
    queryset = StrategyModel.objects.all()


class Universe_6View(ListView):
    template_name = 'universe_6.html'
    queryset = StrategyModel.objects.all()


class Universe_7View(ListView):
    template_name = 'universe_7.html'
    queryset = StrategyModel.objects.all()


class Universe_8View(ListView):
    template_name = 'universe_8.html'
    queryset = StrategyModel.objects.all()


class Destiny_View(ListView):
    template_name = 'destiny.html'
    queryset = StrategyModel.objects.all()
