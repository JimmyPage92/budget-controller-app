from budget_controller_app.budget.models import Income, ExpensesInfo
from django.db.models import Sum
from django.http import JsonResponse

def chart_show(request):
   labels_income = []
   data_income = []
   labels_expanses = []
   data_expanses = []
   queryset_income = Income.objects.filter(author=request.user).aggregate(budget_total=Sum('income'))
   queryset_expanses = ExpensesInfo.objects.filter(author_expanse=request.user).aggregate(expanses=Sum('cost'))






