# Generated by Django 2.2 on 2019-11-22 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('split', models.BooleanField(default=False)),
                ('fuel_type', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=200)),
                ('delivery_method', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date', 'time', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BuyerProfile',
            fields=[
                ('fuel_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='supplier.FuelRequest')),
                ('phone_number', models.CharField(max_length=20)),
                ('stage', models.CharField(max_length=20)),
                ('position', models.IntegerField()),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='file', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SupplierProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpn', models.CharField(max_length=20)),
                ('picture', models.ImageField(default='default.png', upload_to='profiles')),
                ('phone', models.CharField(help_text='eg 263775580596', max_length=20)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FuelUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closing_time', models.TimeField()),
                ('max_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('min_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deliver', models.BooleanField(default=False)),
                ('payment_method', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='province_location', to='supplier.Province')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='supplier_name', to='supplier.SupplierProfile')),
            ],
            options={
                'ordering': ['date', 'time', 'supplier'],
            },
        ),
        migrations.AddField(
            model_name='fuelrequest',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='request_location', to='supplier.Province'),
        ),
        migrations.AddField(
            model_name='fuelrequest',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='supplier.FuelRequest')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='supplier.BuyerProfile')),
            ],
            options={
                'ordering': ['date', 'time'],
            },
        ),
    ]
