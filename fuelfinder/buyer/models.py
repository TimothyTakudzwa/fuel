from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class BuyerProfile(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='buyer_profile_pics')

    def __str__(self):
        return f' {self.buyer.username} Profile '

    def save(self, *args, **kwargs):
        super(BuyerProfile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)    
 