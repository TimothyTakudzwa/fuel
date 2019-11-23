from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from buyer.models import BuyerProfile


class SupplierProfile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bpn = models.CharField(max_length=20)
    picture = models.ImageField(default='default.png', upload_to='profiles')
    phone = models.CharField(max_length=20, help_text='eg 263775580596')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    class Meta:
        ordering = ['name']


class Province(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class FuelUpdate(models.Model):
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.DO_NOTHING, related_name='supplier_name')
    closing_time = models.TimeField()
    max_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    min_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deliver = models.BooleanField(default=False)
    # location = models.ForeignKey(Province, on_delete=models.DO_NOTHING, related_name='province_location')
    payment_method = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['date', 'time', 'supplier']

    def __str__(self):
        return f'{str(self.supplier)} - {str(self.max_amount)}l'


class FuelRequest(models.Model):
    name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    split = models.BooleanField(default=False)
    fuel_type = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=200)
    delivery_method = models.CharField(max_length=200)
    # location = models.ForeignKey(Province, on_delete=models.DO_NOTHING, related_name='request_location')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['date', 'time', 'name']

    def __str__(self):
        return f'{str(self.name)} - {str(self.amount)}'



class Transaction(models.Model):
    request_name = models.ForeignKey(FuelRequest, on_delete=models.DO_NOTHING, related_name='fuel_request')
    buyer_name = models.ForeignKey(BuyerProfile, on_delete=models.DO_NOTHING, related_name='buyinh_fuel')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f'{str(self.request_name)} - {str(self.buyer_name)}'

