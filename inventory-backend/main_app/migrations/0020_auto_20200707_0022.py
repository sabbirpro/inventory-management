# Generated by Django 3.0.4 on 2020-07-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_myuser_outlet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='Role',
            field=models.CharField(max_length=20),
        ),
    ]