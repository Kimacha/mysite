from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.core.mail import BadHeaderError, send_mail


def home_view(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    email = request.POST.get('email', '')
    if name and subject and message and email:
        try:
            send_mail(subject, message, email, ['abisaimsizilo@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('')

    open_map = AboutOpenMap.objects.first()
    what_we_do = WhatWeDo.objects.filter()
    team = TeamMembers.objects.all()
    projects = OurProjects.objects.all()

    context = {
        'open_map': open_map,
        'team': team,
        'projects': projects,
        'what_we_do': what_we_do,
    }
    return render(request, 'index.html', context)
