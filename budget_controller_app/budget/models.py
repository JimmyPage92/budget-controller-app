import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
CHOICES_INCOME = (
    ('Salary', 'Salary'),
    ('Social', 'Social'),
    ('Donation', 'Donation'),
    ('Other', 'Other'),
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
    date_income = models.DateField(default=timezone.now, verbose_name='Date income ("YYYY-MM-DD")')
    reason_income = models.CharField(choices=CHOICES_INCOME, blank=True, max_length=15)
    currency = models.CharField(choices=CHOICES_CURRENCY, default='', max_length=5)
    income = models.FloatField(default=0.0, verbose_name='Amount income')

    def get_absolute_url(self):
        return reverse('user-page')

    def __str__(self):
        return f'Hello {self.author} Your income : {self.income} {self.currency} from {self.reason_income}'

class ExpensesInfo(models.Model):
    author_expanse = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_reason = models.CharField(choices=CHOICES_EXPENSES, blank=True, max_length=50)
    cost = models.FloatField(default=0.0, verbose_name='Amoint of expanse')
    date_expanse = models.DateField(default=timezone.now, verbose_name='Date expanse ("YYYY-MM-DD")')
    currency_expanse = models.CharField(choices=CHOICES_CURRENCY, default='', max_length=5)

    def get_absolute_url(self):
        return reverse('user-page')

    def __str__(self):
        return f'Your expense: {self.expense_reason} is from {self.date_added} and amounts to {self.cost}'

