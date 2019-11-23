from django.shortcuts import render, get_object_or_404, redirect


from supplier.models import *
from supplier.forms import *
from .forms import *

from datetime import datetime

def index(request):
    return render(request, 'users/index.html')


def suppliers_list(request):
    suppliers = SupplierProfile.objects.all()
    return render(request, 'users/suppliers_list.html', {'suppliers': suppliers})

# Begining Of Supplier Management

def supplier_user_create(request, sid):
    supplier = get_object_or_404(SupplierProfile, id=sid) 
    if request.method == 'POST':
        user_count = SupplierContact.objects.filter(supplier_profile=supplier).count()
        if user_count > 50:
            raise Http404("Organisations has 50 users, delete some ")
        form = SupplierContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cellphone = form.cleaned_data['cellphone']
            telephone = form.cleaned_data['telephone']

            user = User.objects.create_user(email, email, password)
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()   
            contact = SupplierContact.objects.create(user=user, cellphone=cellphone, telephone=telephone, supplier_profile=supplier)
            #contact.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('users:suppliers_list')
            
        
        else:
            msg = "Error in Information Submitted"
            messages.error(request, msg)
    else:
        form = SupplierContactForm()


    return render (request, 'users/add_user.html', {'form': form, 'supplier': supplier}) 

def edit_supplier(request,id):
    supplier = get_object_or_404(SupplierProfile, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            data = form.cleaned_data
            supplier = form.save()
            messages.success(request, 'Changes Successfully Update')
            return redirect('users.index')
    else:
        form = SupplierProfile(instance=supplier)
    return render(request, 'users/supplier_edit.html', {'form': form, 'supplier': supplier})

def delete_user(request,id):
    supplier = get_object_or_404(SupplierProfile, id=id)

    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            supplier.delete()
            messages.success(request, 'User Has Been Deleted')
        return redirect('administrator:blog_all_posts')
    form = ActionForm()    

    return render(request, 'user/supplier_delete.html', {'form': form, 'supplier': supplier})










