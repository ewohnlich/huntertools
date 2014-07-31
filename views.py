from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.views import generic

def Home(request):
 return render(request, 'home.html')

def ChangeLog(request):
 return render(request, 'changelog.html')
def FAQ(request):
 return render(request, 'faq.html')
def About(request):
 return render(request, 'about.html')