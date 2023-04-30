from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            topic_name=TFD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()

            TQS=Topic.objects.all()
            d1={'TQS':TQS}
            return render(request,'display_topics.html',d1)
            
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=="POST":
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            topic_name=WFD.cleaned_data['topic_name']
            name=WFD.cleaned_data['name']
            url=WFD.cleaned_data['url']
            email=WFD.cleaned_data['email']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
            WO.save()

            WQS=Webpage.objects.all()
            d1={'WQS':WQS}
            return render(request,'display_webpages.html',d1)
 
    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    AFO=AccessRecordForm()
    d={'AFO':AFO}

    if request.method=='POST':
        AFD=AccessRecordForm(request.POST)
        if AFD.is_valid():
            name=AFD.cleaned_data['name']
            author=AFD.cleaned_data['author']
            date=AFD.cleaned_data['date']
            WO=Webpage.objects.get(name=name)
            AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
            AO.save()

            AQS=AccessRecord.objects.all()
            d1={'AQS':AQS}
            return render(request,'display_accessrecords.html',d1)

    return render(request,'insert_accessrecord.html',d)