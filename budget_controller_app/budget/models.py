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

CHOICES_EXPENSES = (
    ('Rent', 'Rent'),
    ('Food', 'Food'),
    ('Fuel', 'Fuel'),
    ('Entertainment', 'Entertainment'),
    ('Other', 'Other'),
    ('Cosmetics and Chemicals', 'Cosmetics and Chemicals'),
)

class Income(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_income = models.DateField(default=timezone.now, verbose_name='Date income ("YYYY-MM-DD")')
    reason_income = models.CharField(choices=CHOICES_INCOME, blank=True, max_length=15)
    income = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name='Amount income', blank=False)

    def get_absolute_url(self):
        return reverse('user-page')

    def __str__(self):
        return f'Hello {self.author} Your income : {self.income} PLN from {self.reason_income}'

class ExpensesInfo(models.Model):
    author_expanse = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_reason = models.CharField(choices=CHOICES_EXPENSES, blank=True, max_length=50)
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name='Amount of expanse')
    date_expanse = models.DateField(default=timezone.now, verbose_name='Date expanse ("YYYY-MM-DD")')

    def get_absolute_url(self):
        return reverse('user-page')

    def __str__(self):
        return f'Your expense: {self.expense_reason} PLN is from {self.date_expanse} and amounts to {self.cost}'

