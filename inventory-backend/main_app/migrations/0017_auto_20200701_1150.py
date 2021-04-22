# Generated by Django 3.0.4 on 2020-07-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20200701_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Number',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='outlet',
            name='Number',
            field=models.BigIntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Number',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
