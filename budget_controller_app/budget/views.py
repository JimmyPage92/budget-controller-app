from django.conf import settings
from django.shortcuts import render
from .models import Income, ExpensesInfo
from django.core.mail import send_mail
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from django.db.models import Sum
from .forms import ExpansesPlanForm


@login_required(login_url='login')
def home_user_page(request):  # strona startowa jak sie uzytkownik zaloguje
    budget_total = Income.objects.filter(author=request.user).aggregate(budget_total=Sum('income'))

    expanse_total = ExpensesInfo.objects.filter(author_expanse=request.user).aggregate(expanses=Sum('cost'))
    if budget_total['budget_total'] == None:
        budget_total['budget_total'] = 0
    if expanse_total['expanses'] == None:
        expanse_total['expanses'] = 0
    diff = budget_total['budget_total'] - expanse_total['expanses']
    print(diff)
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

    context = {'title': 'User page', 'incomes': Income.objects.all(),
               'expanses': ExpensesInfo.objects.all(), 'budget_total': budget_total['budget_total'],
               'expanse_total': expanse_total['expanses'], "chart_name": "test", 'diff': diff}
    return render(request, 'budget/home-budget.html', context=context)

@login_required(login_url='login')
def plan_expanses(request):
    if request.method == 'POST':
        plan_expanse = ExpansesPlanForm(request.POST)
        print(request.POST)
        if plan_expanse.is_valid():
            choice_expanses: str = plan_expanse.cleaned_data['choice_expanses']
            plan_amount: int = plan_expanse.cleaned_data['plan_amount']
    else:
        choice_expanses: str = 'default'
        plan_amount: int = 0
        plan_expanse = ExpansesPlanForm()

    sum_rent = ExpensesInfo.objects.filter(expense_reason__startswith='Rent').aggregate(Sum('cost'))
    sum_rent_to_show = sum_rent['cost__sum']
    sum_food = ExpensesInfo.objects.filter(expense_reason__startswith='Food').aggregate(Sum('cost'))
    sum_food_to_show = sum_food['cost__sum']
    sum_entertainment = ExpensesInfo.objects.filter(expense_reason__startswith='Entertainment').aggregate(Sum('cost'))
    sum_entertainment_to_show = sum_entertainment['cost__sum']
    sum_fuel = ExpensesInfo.objects.filter(expense_reason__startswith='Fuel').aggregate(Sum('cost'))
    sum_fuel_to_show = sum_fuel['cost__sum']
    sum_chemicals = ExpensesInfo.objects.filter(expense_reason__startswith='Cosmetics and Chemicals').aggregate(Sum('cost'))
    sum_chemicals_show = sum_chemicals['cost__sum']
    context = {'sum_rent': sum_rent_to_show, 'sum_food': sum_food_to_show, 'sum_fuel_to_show': sum_fuel_to_show,
               'sum_entertainment': sum_entertainment_to_show, 'sum_chemicals_show': sum_chemicals_show,
               'plan_expanse': plan_expanse, 'plan_amount': plan_amount,
               'choice_expanses': choice_expanses}
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
    send_mail(
        subject="Test email!",
        message="This is a test email!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['settings.EMAIL_HOST_USER'],
        fail_silently=False,
    )