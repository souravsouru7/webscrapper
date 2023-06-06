from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Links
from django.http import HttpResponseRedirect
# Create your views here.
def Scraper(request):
    if request.method == "POST":
        
        site=request.POST.get("site","")
        page=requests.get(site)
        soup=BeautifulSoup(page.text,'html.parser')
   

        for link in soup.find_all('a'):
            link_adress=(link.get('href'))
            link_text=link.string
            Links.objects.create(adress=link_adress,name=link_text)
        return HttpResponseRedirect("/")
    else:
        data=Links.objects.all()
    return render(request,"myapp/result.html",{"data":data})

def clear (request):
    Links.objects.all().delete()
    return render(request,"myapp/result.html")