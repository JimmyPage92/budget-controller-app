# Generated by Django 4.1.2 on 2022-10-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0008_alter_income_date_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date_income',
            field=models.DateTimeField(null=True),
        ),
    ]
