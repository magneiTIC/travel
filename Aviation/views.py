from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
from Vol.forms import *


from Vol.models import Vol, Compagnie, Trajet

# Create your views here.

7

def home(request):
    vols=Vol.objects.all()
    compagnies=Compagnie.objects.all()
    trajets=Trajet.objects.all()

    return render(request,'home/index.html',{'vols':vols,'compagnies':compagnies,'trajets':trajets})


def listeTrajets(request):
   trajets=Trajet.objects.all()
   return render(request,'home/listeTrajets.html',{'trajets':trajets})

def listeVolTrajet(request,pk):
   trajet=Trajet.objects.get(id = pk)
   return render(request,'home/listeVolTrajet.html',{'trajet':trajet})

def trajet(request):
    return render(request,'home/trajet.html')


def ListeVols(request):
    vols=Vol.objects.all()
    return render(request,'home/listeVols.html',{'vols':vols})


def vol(request,pk):
    vol=Vol.objects.get(id = pk)
    return render(request,'home/vol.html',{'vol':vol}) 

@login_required
def deleteVol(request, pk=None):
    vols=Vol.objects.all()
    resp = { 'status' : 'echec', 'msg' : '' }
    if pk is None:
        resp['msg'] = 'Aucun information fournie'
    else:
        try:
            Vol.objects.filter(id = pk).delete() #update(delete_flag = 1)
            resp['status'] = 'success'
            messages.success(request, "Vol supprime avec succes")
        except:
            resp['msg'] = 'Echec lors de la suppression du vol'
    # return HttpResponse(json.dumps(resp), content_type="application/json")
        return render(request,'home/listeVols.html',{'vols':vols})




def compagnie(request,pk):    
    compagnie=Compagnie.objects.get(id = pk)
    print(compagnie.logo)
    return render(request,'home/compagnie.html',{'compagnie':compagnie})

def listeCompagnies(request):
    compagnies= Compagnie.objects.all()
    return render(request,'home/listeCompagnies.html',{'compagnies':compagnies})

@login_required
def updateCompagnie(request, pk = None):
    form = compagnieForm()
    if pk is None:
        compagnie = {}
    else:
        compagnie=Compagnie.objects.get(id = pk)
    # return render(request,'home/modifCompagnie.html',{'compagnie':compagnie})
        return render(request,'home/updateCompagnie.html',{'compagnie':compagnie, 'form':form})

@login_required
def saveCompagnie(request,pk):
    compagnie = Compagnie.objects.get(id=pk)
    # form = compagnieForm()
    if request.method == 'POST':
        form = compagnieForm(request.POST,request.FILES, instance=compagnie)
        if form.is_valid():
            form.save()
            return redirect('liste-compagnies')
    else: 
       form=compagnieForm(instance=compagnie)
    return render(request, 'home/updateCompagnie.html', {'form': form})    

