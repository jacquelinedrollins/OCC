from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404



def index(request):
    return HttpResponse('INDEX')
