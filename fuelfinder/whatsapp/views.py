from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from supplier.models import BuyerProfile
from .helper_functions import bot_action
from django.views.decorators.csrf import csrf_exempt
import json 

@csrf_exempt 
def index(request):
    token = request.GET.get('token')
    data = json.loads(request.body)
    # message = data['messages']['body']
    # phone_number = data['message']['chatid'].split('@')[0]
    message = data['message']
    phone_number = data['phone_number']
    token = 'sq0pk8hw4iclh42b'
    if token != 'sq0pk8hw4iclh42b':
        return HttpResponse('Unauthorized')
    else:
        check = BuyerProfile.objects.filter(phone_number = phone_number).exists()
        if check:
            user = BuyerProfile.objects.filter(phone_number=phone_number).first()
            if user.name.is_active:
                response_message = bot_action(user, message)                
            else:
                response_message = "Your cannot use this, please create a buyer account and then add the phone number"
        else:
            response_message = "We could not find an account associated with you"
    return HttpResponse(response_message)
