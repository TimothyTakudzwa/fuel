from django.shortcuts import render, get_object_or_404, redirect


from supplier.models import *
from supplier.forms import *
from buyer.models import *
from buyer.forms import *
from .forms import *

from datetime import datetime

def index(request):
    return render(request, 'users/index.html')


def suppliers_list(request):
    suppliers = SupplierProfile.objects.all()
    edit_form = SupplierProfileEditForm()
    delete_form = ActionForm()
    return render(request, 'users/suppliers_list.html', {'suppliers': suppliers, 'edit_form': edit_form, 'delete_form': delete_form})

def suppliers_delete(request, sid):
    supplier = SupplierProfile.objects.filter(id=sid).first()
    if request.method == 'POST':
        supplier.delete()    

    return redirect('users:suppliers_list')

def buyers_list(request):
    buyers = BuyerProfile.objects.all()
    edit_form = BuyerProfileEditForm()
    delete_form = ActionForm()
    return render(request, 'users/buyers_list.html', {'buyers': buyers, 'edit_form': edit_form, 'delete_form': delete_form})

def buyers_delete(request, sid):
    buyer = BuyerProfile.objects.filter(id=sid).first()
    if request.method == 'POST':
        buyer.delete()    

    return redirect('users:buyers_list')

# Begining Of Supplier Management

def supplier_user_create(request, sid):
    supplier = get_object_or_404(SupplierProfile, id=sid) 
    staff = SupplierContact.objects.filter(supplier_profile=supplier)
    count = SupplierContact.objects.all().count()
    delete_form = ''
    edit_form = ''
    if request.method == 'POST':
        user_count = SupplierContact.objects.filter(supplier_profile=supplier).count()
        if user_count > 50:
            raise Http404("Organisations has 50 users, delete some ")
        form = SupplierContactForm(request.POST)
        profile_form = UserUpdateForm(request.POST, instance=supplier)

        if profile_form.is_valid():
            supplier = profile_form.save()
            messages.success(request, 'Your Changes Have Been Saved')
            return redirect('users:supplier_user_create', sid=supplier.id)

        

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
            return redirect('users:supplier_user_create', sid=supplier.id)
            
        
        else:
            msg = "Error in Information Submitted"
            messages.error(request, msg)
    else:
        form = SupplierContactForm()
        profile_form = UserUpdateForm(instance=supplier)



    return render (request, 'users/add_user.html', {'form': form, 'supplier': supplier, 'staff': staff, 'count': count,
     'delete_form':delete_form, 'edit_form': edit_form, 'profile_form':profile_form}) 


def buyer_user_create(request, sid):
    buyer = get_object_or_404(BuyerProfile, id=sid) 
    staff = BuyerContact.objects.filter(buyer_profile=buyer)
    count = BuyerContact.objects.all().count()
    delete_form = ''
    edit_form = ''
    if request.method == 'POST':
        user_count = BuyerContact.objects.filter(buyer_profile=buyer).count()
        if user_count > 10:
            raise Http404("Your organisation has reached the maximum number of users, delete some ")
        form = BuyerContactForm(request.POST)
        profile_form = UserUpdateForm(request.POST, instance=buyer)

        if profile_form.is_valid():
            buyer = profile_form.save()
            messages.success(request, 'Your Changes Have Been Saved')
            return redirect('users:buyer_user_create', sid=buyer.id)

        

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cellphone = form.cleaned_data['phone']
            user = User.objects.create_user(email, email, password)
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()   
            contact = BuyerContact.objects.create(user=user, phone=cellphone, buyer_profile=buyer)
            #contact.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('users:buyer_user_create', sid=buyer.id)
            
        
        else:
            msg = "Error in Information Submitted"
            messages.error(request, msg)
    else:
        form = BuyerContactForm()
        profile_form = UserUpdateForm(instance=buyer)



    return render (request, 'users/add_buyer.html', {'form': form, 'buyer': buyer, 'staff': staff, 'count': count, 'delete_form':delete_form, 'edit_form': edit_form, 'profile_form':profile_form}) 


def edit_supplier(request,id):
    supplier = get_object_or_404(SupplierProfile, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            data = form.cleaned_data
            supplier = form.save()
            messages.success(request, 'Changes Successfully Updated')
            return redirect('users.index')
    else:
        form = SupplierProfile(instance=supplier)
    return render(request, 'users/supplier_edit.html', {'form': form, 'supplier': supplier})

def edit_buyer(request,id):
    buyer = get_object_or_404(BuyerProfile, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=buyer)
        if form.is_valid():
            data = form.cleaned_data
            buyer = form.save()
            messages.success(request, 'Changes Successfully Updated')
            return redirect('users.index')
    else:
        form = BuyerProfile(instance=supplier)
    return render(request, 'users/buyer_edit.html', {'form': form, 'buyer': buyer})

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










