# Generated by Django 4.1.2 on 2022-10-31 19:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0017_alter_expensesinfo_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesinfo',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='income',
            name='date_income',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='income',
            name='reason_income',
            field=models.CharField(choices=[('Social', 'Social'), ('Salary', 'Salary'), ('Donation', 'Donation')], default='', max_length=15),
        ),
    ]