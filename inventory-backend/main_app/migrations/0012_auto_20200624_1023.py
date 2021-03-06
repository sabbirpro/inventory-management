# Generated by Django 3.0.4 on 2020-06-24 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_purchase_paymentstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Number', models.IntegerField(unique=True)),
                ('Email', models.CharField(max_length=100, null=True, unique=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('Note', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvoiceNumber', models.CharField(default='default', max_length=100, unique=True)),
                ('Discount', models.FloatField(null=True)),
                ('Date', models.DateTimeField()),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Customer')),
                ('Outlet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Outlet')),
            ],
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='SalePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField()),
                ('Date', models.DateTimeField()),
                ('Sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Sale')),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Product')),
                ('Sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Sale')),
            ],
        ),
    ]
