from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from gdrobot.models import BlogsPost

# Create your views here.
def archive(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("gdrobotnews.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))