from django.shortcuts import render
from .models import Income, ExpensesInfo
from django.http import HttpResponse


def home(request):
    return render(request, 'budget/home.html', {'title': 'main page', 'incomes': Income.objects.all()})

def about(request):
    return render(request, 'budget/about.html', {'title': 'About'})

