from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("HI GOOD EVENING TO ALL....")

def htmltag(request):
	return HttpResponse("<h2>HI WELCOME TO APSSDC PROGRAM </h2>")

def username(request,uname):
	return HttpResponse("<h2>HI WELCOME <span style='color:red'>{}</span> TO APSSDC PROGRAM</h2>".format(uname))

def username(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:blue'>HI USER <span style='color:blue'>{}</span> AND YOUR AGE IS <span style='color:pink'>{}</span></h3>".format(un,ag))

def  empdetails(request,eid,eage,ename):
	return HttpResponse("<script>alert('HI WELCOME {}')</script><h3>HI WELCOME{} YOUR AGE IS {} AND ID IS {}</h3>".format(ename,ename,eage,eid))


def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k= {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studetdetails(request):
	return render(request,'html/std.html')

	