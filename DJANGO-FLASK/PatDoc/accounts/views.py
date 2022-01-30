from http.client import HTTPResponse
from django.shortcuts import render, redirect
import requests

def accounts(request):
    return render(request,"accounts/accounts.html")

def dhome(request):
    return render(request, "accounts/dhome.html")

def logout(request):
    del request.session['email']
    del request.session['username']
    request.session['loggedin'] = False
    del request.session['loggedin']
    return redirect("/accounts/")

def appointments(request):
    if request.method == "POST":
        id = request.POST['booking_id']
        time = request.POST['time']
        json_data = {
            'id': id,
            'app_date': time
        }
        api_url = "http://localhost:5000/appointmentstime"
        r= requests.post(url = api_url, json=json_data)
        msg = 'Your appointment for the patient has been successfully booked !'
        if r.status_code == 200:
            return render(request, "accounts/appointments.html",{'msg':msg})
    if not 'email' in request.session:
        return redirect("accounts/")
    else:
        email = request.session['email']
        json_data = {
            'email': email
        }
        api_url = "http://localhost:5000/appointments"
        r = requests.post(url = api_url, json=json_data)
        appointments = r.json()
        return render(request, 'accounts/appointments.html',{'appointments':appointments})


    

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        json_data = {
            'email': email,
            'password': password
        }

        api_url = "http://localhost:5000/login"

        r = requests.post(url=api_url, json=json_data)
        
        if r.status_code == 200:
            account=r.json()
            # print(account)
            # print(account['account']['name'])
            request.session['username']=account['account']['name']
            request.session['email']=account['account']['email']
            request.session['loggedin']=True
            print(request.session['email'])
            return redirect('/accounts/dhome')
        else:
            msg = r.json()['msg']
            return render(request,"accounts/login.html",{'msg':msg})
        
    return render(request, "accounts/login.html")

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        hospital = request.POST['hospital']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        city = request.POST['city']
        pincode = request.POST['pincode']
        time1 = request.POST['time1']
        time2 = request.POST['time2']
        sday = request.POST['sday']
        eday = request.POST['eday']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        json_data={
            'name': name,
            'email': email,
            'hospital': hospital,
            'add1': add1,
            'add2': add2,
            'city': city,
            'pincode': pincode,
            'time1': time1,
            'time2': time2,
            'sday': sday,
            'eday': eday,
            'password': password,
            'cpassword': cpassword
        }

        api_url = "http://localhost:5000/register"

        r = requests.post(url=api_url, json=json_data)
        # print(r.json())
        # print(r.status_code)
        msg = r.json()['msg']
        if r.status_code == 200:
            return redirect('/accounts/login')
        else:
            return render(request, "accounts/register.html", {'msg':msg})
        
    return render(request, "accounts/register.html")

# Create your views here.
