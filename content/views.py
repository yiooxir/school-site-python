#coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def index(request):
    print 1
    return render_to_response('index.html', RequestContext(request,{
        'myvar': 'hello world',
    }))
