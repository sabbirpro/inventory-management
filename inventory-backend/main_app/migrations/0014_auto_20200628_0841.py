# Generated by Django 3.0.4 on 2020-06-28 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20200628_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='InvoiceNumber',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
