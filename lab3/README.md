TASK 1 - > initialized the virtualenv with python 3.7 and insatlled django inside the virtual environment .

TASK 2 - > built the structure as shown .

TASK 3 - > Ran django . 

TASK 4 - > Stopped and committed .

TASK 5 - > Made a new template .

TASK 6 - > Created the new folder /main/templates and a main.html file inside. Also main.py .Committed . 

TASK 7 - > Checked settings.py and url.py

TASK 8 - > Checked both the files main.html which was ran as a default page and health which was a subdir page .

TASK 9 - > Checked main/urls.py and the configs there .

TASK 10 - > Ran Django server again and it is still working . Committed . 

TASK 11 - > Installed lib requests in the pipenv .

TASK 12 - > Opened the page /health and it is working . 

TASK 13 - > 

1. Edited the date , the URL of the page , the server info and the client info.

def health(request):
    servdate = date.today().strftime("%d/%m/%Y")

    current_url = request.get_full_path()
    host_address = request.get_host()
    current_url_full = host_address+current_url

    osinfo = os.uname().version
    osinfo2 = os.uname().machine
    osinfo3 = os.uname().nodename
    osinfo_full = osinfo + " " + osinfo2 + " " + osinfo3

    agent = request.META["HTTP_USER_AGENT"]
    agent_ip = request.META['REMOTE_ADDR']
    agent_full = agent + " , The IP ADDRESS THIS REQUEST IS COMING FROM IS : " + agent_ip

    response = {'date': servdate, 'current_page': current_url_full, 'server_info': osinfo_full ,'client_info': agent_full}
    return JsonResponse(response)
-----------------------------------------------------------------------------

2. 
