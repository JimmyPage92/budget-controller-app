# Generated by Django 4.1.2 on 2022-11-06 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0035_alter_expensesinfo_cost_alter_income_income'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensesinfo',
            name='currency_expanse',
        ),
        migrations.RemoveField(
            model_name='income',
            name='currency',
        ),
    ]
