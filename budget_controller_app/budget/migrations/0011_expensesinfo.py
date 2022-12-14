# Generated by Django 4.1.2 on 2022-10-16 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0010_alter_income_date_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.CharField(max_length=20)),
                ('cost', models.FloatField()),
                ('date_added', models.DateField()),
                ('user_expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
