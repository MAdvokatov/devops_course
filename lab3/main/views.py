import logging

import requests
from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime
from datetime import date

logging.basicConfig(level=logging.INFO)


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    servdate = date.today().strftime("%d/%m/%Y")

    current_url = request.get_full_path()
    host_address = request.get_host()
    current_url_full = host_address + current_url

    osinfo = os.uname().version
    osinfo2 = os.uname().machine
    osinfo3 = os.uname().nodename
    osinfo_full = osinfo + " " + osinfo2 + " " + osinfo3

    agent = request.META["HTTP_USER_AGENT"]
    agent_ip = request.META['REMOTE_ADDR']
    agent_full = agent + " , The IP ADDRESS THIS REQUEST IS COMING FROM IS : " + agent_ip

    response = {'date': servdate, 'current_page': current_url_full, 'server_info': osinfo_full,
                'client_info': agent_full}
    return JsonResponse(response)


