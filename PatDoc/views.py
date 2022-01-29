from django.http import HttpResponse
from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')
    #return HttpResponse("Welcome")

def book(request):
    if request.method == "POST":
        doctor_email = request.POST['doctor']
        patient_email = request.POST['email']
        name = request.POST['patient']
        age = request.POST['age']
        relation = request.POST['relation']
        date = request.POST['date']
        time = request.POST['time']

        json_data = {
            'doctor': doctor_email,
            'email': patient_email,
            'patient': name,
            'age': age,
            'relation': relation,
            'date': date,
            'time': time
        }
        api_url = "http://localhost:5000/book"
        r = requests.post(url = api_url, json = json_data)
        if r.status_code == 200:
            return render(request, "bookings.html")
        else:
            return render(request, "search.html")

def search(request):
    if request.method == "POST":
        email = request.POST['browser']
        json_data = {
            'email': email
        }
        api_url ="http://localhost:5000/doctor"
        r = requests.post(url =api_url,json=json_data)
        if r.status_code == 200:
            accounts = r.json()
            return render(request, "drinfo.html",{'account':accounts} )
        else:
            msg = r.json['msg']
            return render(request, "search.html", {'msg': msg})
    
    api_url = "http://localhost:5000/doctor"
    r = requests.get(api_url)
    doctors = r.json()
    return render(request, 'search.html',{'doctors':doctors})
