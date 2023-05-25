from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

@csrf_exempt
def users(request):
    users_from_db = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'usrs': users_from_db,
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def delete_player(request):
    if request.method == 'POST':
        x = User.objects.filter(id=request.POST['zawownik'])
        x.delete()
        return redirect(users)


@csrf_exempt
def delete(request):
    users_from_db = User.objects.all().values()
    template = loader.get_template('delete.html')
    context = {
        'usrs': users_from_db,
    }
    return HttpResponse(template.render(context, request))




@csrf_exempt
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@csrf_exempt
def insert_player(request):
    if request.method == 'POST':
        user = User(imie=request.POST['imie'], nazwisko=request.POST['nazwisko'], telefon=request.POST['telefon'], wiek=request.POST['wiek'])
        user.save()
        return redirect(users)