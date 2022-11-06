# Generated by Django 4.1.2 on 2022-11-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0030_alter_expensesinfo_author_expanse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesinfo',
            name='expense_reason',
            field=models.CharField(blank=True, choices=[('Rent', 'Rent'), ('Food', 'Food'), ('Fuel', 'Fuel'), ('Entertainment', 'Entertainment'), ('Other', 'Other'), ('Cosmetics and Chemicals', 'Cosmetics and Chemicals')], max_length=50),
        ),
    ]