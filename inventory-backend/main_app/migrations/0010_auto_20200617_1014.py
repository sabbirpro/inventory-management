# Generated by Django 3.0.4 on 2020-06-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200617_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasepayment',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
