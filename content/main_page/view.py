#coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from content.children.models import Children


def index(request):
    header = {
        'line1': 'приветствуем вас, мы',
        'line2': 'настоящий 2-А класс'
    }
    children = Children.objects.all()

    return render_to_response('main_page.html', RequestContext(request,{
        'children': children,
        'header': header
    }))