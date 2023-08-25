from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from.models import blog
# Create your views here.
def frontpage(request):
	return render(request,'front.html')

def homepage(request):
	return render(request,'home.html')

def addblog(request):
	return render(request,'addblog.html')

def savedata(request):
	bname = request.GET.get("bname")
	bb = request.GET.get("bb")

	b=blog(bname=bname,bb=bb)
	b.save()

	data = blog.objects.all()
	return render(request,'displayblog.html',{'data':data})


def displayblog(request):
	data = blog.objects.all()
	return render(request,'displayblog.html',{'data':data})