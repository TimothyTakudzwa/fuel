# Generated by Django 2.2.7 on 2019-11-23 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20191122_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(blank=True, max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('supplier_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.SupplierProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__last_name'],
            },
        ),
        migrations.DeleteModel(
            name='SupplierUserProfile',
        ),
    ]
