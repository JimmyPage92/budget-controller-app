from django.shortcuts import render
from django.http import HttpResponse

INCOMES = [
    {
        'user': 'Michal',
        'income': '2000',
    },
    {
        'user': 'Marlena',
        'income': '3000'
    }
]

def home(request):
    return render(request, 'budget/home.html', {'title': 'main page', 'incomes': INCOMES})

def about(request):
    return render(request, 'budget/about.html', {'title': 'About'})

