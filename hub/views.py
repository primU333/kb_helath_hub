from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    info = Home_Page_Info.objects.all().last()
    advices = Advice.objects.all()[:4]
    methods = Prevention_Method.objects.all()[:3]
    test = Testimonial.objects.all().last()
    stats = Home_Stats.objects.all().last()
    address = Contact_Us_Page_Info.objects.all().last()

    context = {
        'info' : info,
        'advices' : advices,
        'methods' : methods,
        'test' : test,
        'stats' : stats,
        'address' : address,
    }
    return render(request, 'hub/index.html', context)


def about(request):
    info = About_Us_Page_Info.objects.all().last()
    objs = Objective.objects.all()[:5]
    team = Team_Member.objects.all()[:3]
    address = Contact_Us_Page_Info.objects.all().last()

    context = {
        'info' : info,
        'objs' : objs,
        'team' : team,
        'address' : address,
        'title' : 'About Us'
    }
    return render(request, 'hub/about.html', context)



def contact(request):
    info = Contact_Us_Page_Info.objects.all().last()
    address = Contact_Us_Page_Info.objects.all().last()

    context = {
        'title' : 'Contact Us',
        'info' : info,
        'address' : address
    }

    if request.POST:
        new_message = Contact_Us_Message()
        new_message.name = request.POST.get('name')
        new_message.subject = request.POST.get('subject')
        new_message.email = request.POST.get('email')
        new_message.message = request.POST.get('message')
        try:
            new_message.save()
            message = 'Message Successfully sent'
            context['message'] = message
        except:
            message = 'Could not send your message, please try again!'
            context['error'] = message

    else:
        pass
    return render(request, 'hub/contact.html', context)




def news(request):

    news = New.objects.all()
    address = Contact_Us_Page_Info.objects.all().last()

    context = {
        'all_news':news,
        'address' : address,
        'title': 'News'
    }

    return render(request, 'hub/news.html', context)


def news_detail(request, news_title, news_id):
    cur_news = New.objects.get(id=news_id)
    address = Contact_Us_Page_Info.objects.all().last()

    context = {
        'title' : news_title,
        'news' : cur_news,
        'address' : address
    }

    if request.POST:
        new_comment = News_Comment()
        new_comment.news = cur_news
        new_comment.user_email = request.POST.get('email')
        new_comment.user_name = request.POST.get('name')
        new_comment.user_photo = request.FILES.get('photo')
        new_comment.comment = request.POST.get('comment')

        try:
            new_comment.save()
            message = 'View Successfully added'
            context['message'] = message
        except:
            message = 'Could not add your View, please try again'
            context['error'] = message
    else:
        pass
    return render(request, 'hub/news_detail.html', context)

