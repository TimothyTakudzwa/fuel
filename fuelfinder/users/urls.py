from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('suppliers/', views.suppliers_list, name="suppliers_list"),
    path('buyers/', views.buyers_list, name="buyers_list"),
    path('delete/<phone_number>', views.delete, name="delete"),
    path('supplier_user_create/<int:sid>', views.supplier_user_create, name="supplier_user_create"),
    path('supplier_user_delete/<int:sid>', views.suppliers_delete, name="suppliers_delete"),

    # path('/index/', views.index, name="home")
    # path('/index/', views.index, name="home")

]