from django.shortcuts import render
import requests
from .constants import *
from supplier.models import FuelRequest


def send_message(phone_number, message):
    payload = {
        "phone": phone_number,
        "body": message
    }
    url = "https://eu33.chat-api.com/instance78632/sendMessage?token=sq0pk8hw4iclh42b"
    r = requests.post(url=url, data=payload)
    print(r)
    return r.status_code


def bot_action(user, message):
    if message.lower() == 'menu' and user.stage != 'registration':
        return requests_handler(user, message)
    if user.stage == 'registration':
        response_message = registration_handler(user, message)
    elif user.stage == 'requesting':
        response_message = requests_handler(user, message)
    else:
        response_message = ''
    return response_message


def registration_handler(user, message):
    if user.position == 0:
        full_name = user.name.first_name.capitalize() + " " + user.name.last_name.capitalize()
        response_message = greetings_message.format(full_name)
        user.position = 1
        user.save()
        print(response_message)
    elif user.position == 1:
        if message.lower() == 'yes':
            response_message = successful_integration
            user.stage = 'requesting'
            user.position = 2
            user.save()
        else:
            response_message = "Unfortunately you will have to contact your admin to make changes, but for the time being we will block this account"
            user.is_active = True
            user.save()
    return response_message


def requests_handler(user, message):
    if user.position == 1:
        response_message = "Hie, Would you like fuel today. \n\nType either *Yes* or *No*"
        user.position = 2
        user.save()
    elif user.position == 2:
        response_message = "Which type of fuel do you want\n\n1. Petrol\n2. Diesel"
        user.position = 2
        user.save()
    elif user.position == 3:
        response_message = "How many litres do you want?"
        fuel_type = "Petrol" if message == '1' else "Diesel"
        FuelRequest.objects.create(fuel_type=fuel_type, name=user)

        user.position = 4
        user.save()
    elif user.position == 4:
        response_message = fuel_finder()
    return response_message


def fuel_finder(fuel_request, user_id):
    pass