from django.contrib import admin
from .models import SupplierProfile, FuelUpdate, FuelRequest, Province, Transaction


admin.site.site_header = "FuelFinder Admin"
admin.site.site_title = 'Admin Portal'
admin.site.index_title = 'FuelFinder Admin'


admin.site.register(SupplierProfile)
admin.site.register(FuelUpdate)
admin.site.register(FuelRequest)
admin.site.register(Province)
admin.site.register(Transaction)
