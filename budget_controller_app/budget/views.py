from django.conf import settings
from django.shortcuts import render
from .models import Income, ExpensesInfo
from django.core.mail import EmailMessage
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.urls import reverse_lazy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os


@login_required(login_url='login')
def home_user_page(request):  # strona startowa jak sie uzytkownik zaloguje
    try:
        budget_total = Income.objects.filter(author=request.user).aggregate(budget_total=Sum('income'))

        expanse_total = ExpensesInfo.objects.filter(author_expanse=request.user).aggregate(expanses=Sum('cost'))
        if budget_total['budget_total'] == None:
            budget_total['budget_total'] = 0
        if expanse_total['expanses'] == None:
            expanse_total['expanses'] = 0


        fig, ax = plt.subplots()
        ax.bar(['Expanses', 'Budget'], [(expanse_total['expanses']), budget_total['budget_total']],
               color=['red', 'green'])
        plt.xlabel('Your incomes and expanses')
        plt.ylabel('PLN')
        ax.set_title('Your total expenses vs total budget')
        red_patch = mpatches.Patch(color='red', label='Amount of expanses')
        green_patch = mpatches.Patch(color='green', label='Amount of budget')
        ax.legend(handles=[red_patch, green_patch], loc=(0.4, 0.8))
        plt.savefig(os.path.join('test.png'), dpi=90, format='png', bbox_inches='tight')
        plt.switch_backend('agg')
        plt.show()
        plt.close()
    except TypeError:
        print('NO DATA')
    diff = (budget_total|expanse_total)
    context = {'title': 'User page', 'incomes': Income.objects.all(),
               'expanses': ExpensesInfo.objects.all(), 'budget_total': budget_total['budget_total'],
               'expanse_total': expanse_total['expanses'], "chart_name": "test", 'diff': diff}
    return render(request, 'budget/home-budget.html', context=context)


@login_required(login_url='login')
def plan_expanses(request):  # tu obliczam sume wydatkow np. dla RENT albo dla FOOD czy Fuel/
    # TODO zrobic formularz zeby dodawac ustalona kwote do wydania i porownac ja z kwota wydana juz na konkretny typ

    sum_definite_expanse = ExpensesInfo.objects.all().aggregate(Sum('cost'))
    sum2 = ExpensesInfo.objects.all().annotate(Count('expense_reason'))
    sum_rent = ExpensesInfo.objects.filter(expense_reason__startswith='Rent').aggregate(Sum('cost'))
    sum_food = ExpensesInfo.objects.filter(expense_reason__startswith='Food').aggregate(Sum('cost'))
    sum_entertainment = ExpensesInfo.objects.filter(expense_reason__startswith='Entertainment').aggregate(Sum('cost'))
    context = {'sum_definite_expanse': sum_definite_expanse, 'sum2': sum2, 'sum_rent': sum_rent, 'sum_food': sum_food,
               'sum_entertainment': sum_entertainment}
    return render(request, 'budget/plan-your-expanse.html', context=context)


def about(request):  # strona about_app
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


def send_email(request):

    EmailMessage(
        subject="Test email!",
        body="This is a test email!",
        from_email=[settings.EMAIL_HOST_USER],
        to=[settings.EMAIL_HOST_USER]
    )
