from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class FuelRequest(models.Model):
    name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)
    split = models.BooleanField(default=False)
    fuel_type = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=200)
    delivery_method = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['date', 'time', 'name']

    def __str__(self):
        return f'{str(self.name)} - {str(self.amount)}'


class BuyerProfile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer_name')
    fuel_request = models.OneToOneField(FuelRequest, on_delete=models.CASCADE, related_name='fuel', null=True)
    phone_number = models.CharField(max_length=20, default='')
    stage = models.CharField(max_length=20, default='registration')
    position = models.IntegerField(default=0)
    image = models.ImageField(default='default.png', upload_to='buyer_profile_pics')

    def __str__(self):
        return f' {self.name.username} Profile '

    def save(self, *args, **kwargs):
        super(BuyerProfile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)    

    class Meta:
        ordering = ['name']
