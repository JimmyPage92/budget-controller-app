import matplotlib
from django.shortcuts import render
from .models import Income, ExpensesInfo
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.urls import reverse_lazy
import matplotlib.pyplot as plt

@login_required(login_url='login')
def home_user_page(request):# strona startowa jak sie uzytkownik zaloguje
    try:
        budget_total = Income.objects.filter(author=request.user).aggregate(budget_total=Sum('income'))
        expanse_total = ExpensesInfo.objects.filter(author_expanse=request.user).aggregate(expanses=Sum('cost'))
        fig, ax = plt.subplots()
        ax.bar(['Expanses', 'Budget'], [(expanse_total['expanses']), budget_total['budget_total']], color=['red', 'green'])
        plt.xlabel('Your incomes and expanses')
        plt.ylabel('PLN')
        ax.set_title('Your total expenses vs total budget')
        plt.legend(title='Expanses and Incomes')
        plt.savefig('test.png')
        plt.show()
        plt.switch_backend('agg')
    except TypeError:
        print('NO DATA')
    context = {'title': 'User page', 'incomes': Income.objects.all(),
               'expanses': ExpensesInfo.objects.all(), 'budget_total': budget_total['budget_total'],
               'expanse_total': expanse_total['expanses']}
    return render(request, 'budget/home-budget.html', context=context)

def about(request):
    return render(request, 'budget/about.html', {'title': 'About'})

class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    template_name = 'budget/income_form.html'
    fields = ['date_income', 'reason_income', 'income']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ExpanseCreateView(LoginRequiredMixin, CreateView):
    model = ExpensesInfo
    template_name = 'budget/expanse_form.html'
    fields = ['date_expanse', 'expense_reason', 'cost']

    def form_valid(self, form):
        form.instance.author_expanse = self.request.user
        return super().form_valid(form)

class IncomeDetailView(DetailView):
    model = Income
    template_name = 'budget/income-detail.html'


class ExpanseDetailView(DetailView):
    model = ExpensesInfo
    template_name = 'budget/expanse-detail.html'

class UpdateIncomeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Income
    template_name = 'budget/income_form.html'
    fields = ['date_income', 'reason_income', 'income']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        income = self.get_object()
        return self.request.user == income.author

class UpdateExpanseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ExpensesInfo
    template_name = 'budget/expanse_form.html'
    fields = ['date_expanse', 'expense_reason', 'cost']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        expanse = self.get_object()
        return self.request.user == expanse.author_expanse

class IncomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Income
    template_name = 'budget/delete_income.html'
    success_url = reverse_lazy('user-page')

    def test_func(self):
        income = self.get_object()
        return self.request.user == income.author

class ExpanseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ExpensesInfo
    template_name = 'budget/delete_expanse.html'
    success_url = reverse_lazy('user-page')

    def test_func(self):
        expanse = self.get_object()
        return self.request.user == expanse.author_expanse