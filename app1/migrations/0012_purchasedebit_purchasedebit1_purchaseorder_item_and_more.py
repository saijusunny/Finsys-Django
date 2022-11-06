# Generated by Django 4.0.4 on 2022-11-04 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_remove_itemtable_tax_rate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchasedebit',
            fields=[
                ('pdebitid', models.AutoField(primary_key=True, serialize=False, verbose_name='pdid')),
                ('debit_no', models.IntegerField(default=1000)),
                ('vendor', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('debitdate', models.DateField(null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('supply', models.CharField(max_length=150, null=True)),
                ('billno', models.CharField(max_length=100, null=True)),
                ('subtotal', models.CharField(max_length=100, null=True)),
                ('taxamount', models.CharField(max_length=100, null=True)),
                ('grandtotal', models.CharField(max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='purchasedebit1',
            fields=[
                ('pdebid', models.AutoField(primary_key=True, serialize=False, verbose_name='pddid')),
                ('items', models.CharField(max_length=100, null=True)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('pdebit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasedebit')),
            ],
        ),
        migrations.CreateModel(
            name='purchaseorder_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100, null=True)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('amount', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='bill_item',
            new_name='purchasebill_item',
        ),
        migrations.AddField(
            model_name='vendor',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company'),
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='billing_address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='deliver_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='vendor_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='billing_address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='deliver_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='vendor_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='firstname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='porder_item',
        ),
        migrations.AddField(
            model_name='purchaseorder_item',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchaseorder'),
        ),
    ]
