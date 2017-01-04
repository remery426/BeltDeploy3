from django.shortcuts import render,redirect
from ..login_app.models import User
from .models import Trip
from django.contrib import messages

def index(request):
    if request.session['thisuser']=='':
        return redirect('/')
    thisuser = User.objects.get(username=request.session['thisuser'])

    context = {
        'user_trips' : Trip.objects.filter(userlist=thisuser),
        'all_trips'  : Trip.objects.all()
    }
    return render(request,'belt_app/index.html',context)
def logout(request):
    print "test"
    request.session['thisuser']=''
    return redirect('/')
def add_page(request):
    return render(request, 'belt_app/add_page.html')
def add(request):
    this_user= User.objects.get(username=request.session['thisuser'])
    response = Trip.objects.add(request.POST, this_user)
    if not response['status']:
        for error in response['error']:
            messages.error(request, error)

        return redirect('belt_app/add_page')
    return redirect('belt_app/travels')
def trip(request,id):
    our_trip = Trip.objects.get(id=id)
    
    context = {
        'thistrip' : Trip.objects.get(id=id),
        'trip_takers' : User.objects.filter(userlist = our_trip )
    }
    return render(request,"belt_app/trip.html", context)
def join(request,id):
    current_user = User.objects.get(username=request.session['thisuser'])
    this_trip = Trip.objects.get(id=id)
    this_trip.userlist.add(current_user)
    return redirect('belt_app/travels')
