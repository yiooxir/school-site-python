#coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Journal


def journal_list(request):
    """
    контроллер отображения список статей журнала событий класса
    """
    journal_objects = Journal.objects.all()
    header = {
        'line1': 'все самое интересное здесь.',
        'line2': 'События нашего класса'
    }
    return render_to_response('journal_list.html', RequestContext(request, {
        'articles': journal_objects,
        'header': header
    }))


def journal_article(request, article_slug):
    """
    контроллер отображения конкретной статьи журнала событий класса
    """
    article = Journal.objects.get(slug=article_slug)
    header = {
        'line1': 'вот это новость...',
        'line2': 'Событие нашего класса'
    }
    return render_to_response('journal_article.html', RequestContext(request, {
        'article': article,
        'header': header
    }))

