
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext


def index(request):
    template = loader.get_template('homepage/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
