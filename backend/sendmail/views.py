from django.http import HttpResponse, Http404
from django.shortcuts import render #get_object_or_404 für schnelleren zugriff verwenden
from django.template import loader

from .models import Mail

def index(request):
    return HttpResponse("test this fuck!")

def singel_mail(request, mail_id):
    try:
        mail = Mail.objects.get(pk=mail_id)
    except mail.DoesNotExist:
        raise Http404("Question does not exist")
    #get_object_or_404(Mail.objects.get(pk=mail_id))
    return render(request, 'sendmail/detail.html', {'mail': mail.name})

def all_mails(request):
    all_mails_list = Mail.objects.order_by('-creation_date')
    template = loader.get_template('sendmail/index.html')
    content = {
        "mail_list": all_mails_list,
    }
    #output = ', '.join([q.country for q in all_mails_list])
    #return HttpResponse(output)
    return HttpResponse(template.render(content, request))