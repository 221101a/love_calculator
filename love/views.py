from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from love.models import User
from django.views.decorators.csrf import csrf_exempt #include this
# Create your views here.
def welcome(request):
    template=loader.get_template("welcome.html")
    res=template.render()
    return HttpResponse(res)

@csrf_exempt # include  this
def store_user(request):
    if(request.method=='POST'):
        user=User()
        user.user_name=request.POST['name']
        user.user_love=request.POST['love']
        user.save()
        l=[90,99,99,99,100,100]
        context={
            'l':l
        }
        template=loader.get_template("store_user.html")
        res=template.render(context,request)
        return HttpResponse(res)
    else:
        msg='first fill data of welcome page and submit,tehn see result !!!'
        context={
            'msg':msg
        }
        template=loader.get_template("welcome.html")
        res=template.render(context,request)
        return HttpResponse(res)

def data_leak(request):
    user=User.objects.all
    context={
        'user':user
    }
    template=loader.get_template("data_leak.html")
    res=template.render(context,request)
    return HttpResponse(res)