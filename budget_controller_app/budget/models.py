from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.
CHOICES_INCOME = (
    ('Blank', 'Blank'),
    ('Social', 'Social'),
    ('Salary', 'Salary'),
    ('Donation', 'Donation')
)

CHOICES_CURRENCY = (
    ('PLN', 'PLN'),
    ('€', 'EURO'),
    ('£', 'GBP'),
    ('$', 'USD'),
)

CHOICES_EXPENSES = (
    ('Rent', 'Rent'),
    ('Food', 'Food'),
    ('Fuel', 'Fuel'),
    ('Entertainment', 'Entertainment'),
    ('Other', 'Other'),
)


class Income(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_income = models.DateField(null=True)
    reason_income = models.CharField(choices=CHOICES_INCOME, default='', max_length=15)
    currency = models.CharField(choices=CHOICES_CURRENCY,default='',max_length=5)
    income = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return f'Hello {self.author} You have now: {self.income} {self.currency} from {self.reason_income}'

class ExpensesInfo(models.Model):
    expense_name = models.CharField(choices=CHOICES_EXPENSES, default='', max_length=50)
    cost = models.FloatField()
    date_added = models.DateField()
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Your expense: {self.expense_name} from {self.date_added} amounts to {self.cost}'

