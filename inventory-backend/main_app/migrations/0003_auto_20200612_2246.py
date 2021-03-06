# Generated by Django 3.0.4 on 2020-06-12 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200612_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Brand',
            new_name='BrandId',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Unit',
            new_name='UnitId',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='Outlet',
            new_name='OutletId',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='Supplier',
            new_name='SupplierId',
        ),
        migrations.RenameField(
            model_name='purchasecost',
            old_name='Cost',
            new_name='CostId',
        ),
        migrations.RenameField(
            model_name='purchasecost',
            old_name='Purchase',
            new_name='PurchaseId',
        ),
        migrations.RenameField(
            model_name='purchaseitem',
            old_name='Product',
            new_name='ProductId',
        ),
        migrations.RenameField(
            model_name='purchaseitem',
            old_name='Purchase',
            new_name='PurchaseId',
        ),
        migrations.RenameField(
            model_name='purchasepayment',
            old_name='Purchase',
            new_name='PurchaseId',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='CategoryId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Category'),
        ),
    ]
