#coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def index(request):
    return render_to_response('main_page.html', RequestContext(request,{
        'my_var': 'hello world',
    }))