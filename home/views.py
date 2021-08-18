from home.models import event,winners, banner
from django.shortcuts import redirect, render , HttpResponse
from home.models import registration as rg
import datetime

# Create your views here.
def index(request):
    event_data = event.objects.all()
    banner_data = banner.objects.all()
    
    date = event.objects.values('date_time')

    timeNow = datetime.datetime.now()


    dict = {'event_data':event_data, 'banner_data':banner_data}
    
    return render(request,'esport.html',dict)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def winners_page(request):
    winner_data = winners.objects.all()
    dict = {'winner_data':winner_data}
    return render(request,'winners.html',dict)

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        team_member = request.POST.get('team_member')
        player1 = request.POST.get('player1')
        player2 = request.POST.get('player2')
        player3 = request.POST.get('player3')
        player4 = request.POST.get('player4')
        team = request.POST.get('team_name')


        store = rg(name=name, email = email, whatsapp =whatsapp, team_name= team , player_1 = player1, player_2= player2, player_3=player3, player_4= player4,members=team_member)
        store.save()
    event_data = event.objects.all()
    dict = {'event_data':event_data}
    return render(request,'registration-successful.html',dict)


def registration_page(request):
    
    return render(request,'registration.html')



