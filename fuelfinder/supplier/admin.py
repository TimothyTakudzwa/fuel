from django.contrib import admin
from .models import SupplierProfile, FuelUpdate, FuelRequest, Province, Transaction, TokenAuthentication, SupplierRating


admin.site.site_header = "FuelFinder Super Admin"
admin.site.site_title = 'Admin Portal'
admin.site.index_title = 'FuelFinder Admin'


admin.site.register(SupplierProfile)
admin.site.register(FuelUpdate)
admin.site.register(FuelRequest)
admin.site.register(Province)
admin.site.register(Transaction)
admin.site.register(TokenAuthentication)
admin.site.register(SupplierRating)

