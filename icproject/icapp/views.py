from django.shortcuts import render,get_object_or_404
from .models import Store,Tub


# Create your views here.

def index(request):
    return render(request,'index.html')

def stores(request):
    stores = Store.objects.all()
    return render(request,'stores.html',{'stores':stores})

def tubs(request):
    tubs =Tub.objects.all()
    return render(request,'tubs.html',{'tubs':tubs})

def single_store(request,store_id):
    page = get_object_or_404(Store,id = store_id)
    tublist = Tub.objects.filter(store= page )
    totalvolume = sum([tub.tub_size for tub in tublist])     
    return render(request,'singlestore.html',{
    'page':page,
    'tublist':tublist,
    'totalvolume':totalvolume
    })        




