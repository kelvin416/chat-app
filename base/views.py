from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .forms import RoomForm

# Create your views here using CRUD operation

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home-view')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-view')
        else:
            messages.error(request, 'Username or Password does not exists')

    context = {}
    return render(request, "base/login_register.html", context)


def logout_user(request):
    logout(request)
    return redirect('home-view')


def home_view(request):
    q = request.GET.get("q") if request.GET.get('q') !=None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count
    }
    return render(request, "base/home.html", context)

def room_view(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        'room': room
    }
    return render(request, "base/room.html", context)

@login_required(login_url='/login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-view')
        
    context = {
        'form': form
    }
    return render(request, "base/room_form.html", context)


# updating a room takes in two attributes request and pk
@login_required(login_url='/login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You Are Not Allowed here!!")


    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home-view')
    context = {
        'form': form
    }
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You Are Not Allowed here!!")

    if request.method == 'POST':
        room.delete()
        return redirect("home-view")

    context = {
        'obj': room
    }

    return render(request, "base/delete.html", context)
