from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from supplier.models import BuyerProfile
from .helper_functions import bot_action


def index(request):
    token = request.GET.get('token')
    data = request.json
    message = data['messages']['body']
    phone_number = data['message']['chatid'].split('@')[0]
    if token != 'sq0pk8hw4iclh42b':
        return 'Unauthorized'
    else:
        check = BuyerProfile.objects.filter(phone_number = phone_number).exists()
        if check:
            user = BuyerProfile.objects.get(phone_number=phone_number)
            if user.is_active:
                response_message = bot_action(user, message)
            else:
                response_message = "Your account has been blocked"
        else:
            response_message = "We could not find an account associated with you"
    return response_message
