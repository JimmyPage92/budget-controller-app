# Generated by Django 4.1.2 on 2022-10-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0013_alter_expensesinfo_reason_expenses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensesinfo',
            name='reason_expenses',
        ),
        migrations.AlterField(
            model_name='expensesinfo',
            name='expense_name',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Food', 'Food'), ('Fuel', 'Fuel'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], default='', max_length=50),
        ),
    ]
