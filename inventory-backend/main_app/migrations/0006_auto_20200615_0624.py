# Generated by Django 3.0.4 on 2020-06-15 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200615_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
