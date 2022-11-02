from django.shortcuts import render
from .models import Income, ExpensesInfo
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import matplotlib.pyplot as plt
import numpy as np
from django.db.models import Q
from django.contrib.auth.models import User

@login_required(login_url='login')
def home_user_page(request):# strona startowa jak sie uzytkownik zaloguje
    expense_items = ExpensesInfo.objects.filter(author_expanse=request.user).order_by('-date_expanse')
    try:
        budget_total = Income.objects.filter(author=request.user).aggregate(budget_total=Sum('income'))
        expense_total = ExpensesInfo.objects.filter(author_expanse=request.user).aggregate(expenses=Sum('cost'))
        fig, ax = plt.subplots()
        ax.bar(['Expenses', 'Budget'], [abs(expense_total['expenses']), budget_total['budget_total']],
               color=['red', 'green'])
        ax.set_title('Your total expenses vs total budget')
        plt.savefig('budget_controller_app/static/budget/expense.jpg')
    except TypeError:
        print('NO DATA')
    context = {'expense_items': expense_items, 'title': 'Budget app', 'incomes': Income.objects.all(),
               'expanses': ExpensesInfo.objects.all(), 'budget': budget_total,
               'expenses': expense_total}
    return render(request, 'budget/home-budget.html', context=context)

def about(request):
    return render(request, 'budget/about.html', {'title': 'About'})

class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    template_name = 'budget/income_form.html'
    fields = ['date_income', 'reason_income', 'currency', 'income']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ExpanseCreateView(LoginRequiredMixin, CreateView):
    model = ExpensesInfo
    template_name = 'budget/expanse_form.html'
    fields = ['date_expanse', 'expense_reason', 'currency_expanse', 'cost']

    def form_valid(self, form):
        form.instance.author_expanse = self.request.user
        return super().form_valid(form)

class UpdateIncomeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Income
    template_name = 'budget/income_form.html'
    fields = ['date_income', 'reason_income', 'currency', 'income']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        income = self.get_object()
        return self.request.user == income.author

class UpdateExpanseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ExpensesInfo
    template_name = 'budget/expanse_form.html'
    fields = ['date_expanse', 'reason_income', 'currency', 'income']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        expanse = self.get_object()
        return self.request.user == expanse.author_expanse

class IncomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Income
    template_name = 'budget/delete_income.html'
    success_url = '/'

    def test_func(self):
        income = self.get_object()
        return self.request.user == income.author

class ExpanseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ExpensesInfo
    template_name = 'budget/delete_expanse.html'
    success_url = '/'

    def test_func(self):
        expanse = self.get_object()
        return self.request.user == expanse.author_expanse