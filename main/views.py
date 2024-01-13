from main.models import *
# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render



def indexHandler(request):
    cats = Category.objects.all()
    services = Service.objects.all()
    tovars = Tovar.objects.all()
    partners = Partner.objects.all()
    otzivs = Otziv.objects.all()
    feeds = Feedback.objects.all()
    foto = ''
    try:
        foto = Fon.objects.get(id=1)
    except Fon.DoesNotExist:
        pass
    contact = ''
    try:
        contact = Contact.objects.get(id=1)
    except Contact.DoesNotExist:
        pass

    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        if request.POST.get('categoriya'):
            feed.categoriya = request.POST.get('categoriya')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')

    # if request.method == 'POST':
    #     BOT_TOKEN = "6598966305:AAFeSGzxWV6ersCQ4bNfcZxXLuoMMeSK9TI"
    #     TELEGRAM_CHAT_ID = "610795666"
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     comment = request.POST.get('comment')
    #     categoriya = request.POST.get('categoriya')
    #     feedback = Feedback(name=name, phone=phone, comment=comment, categoriya=categoriya)
    #     feedback.save()
    #     if comment:
    #         message = f"Новый клиент\nИмя: {name}\nНомер: {phone}\nТовар: {comment}"
    #     else:
    #         message = f"Новый клиент\nИмя: {name}\nНомер: {phone}"
    #     response = requests.get(
    #         f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")
    #     from django.shortcuts import redirect
    #     return redirect('/')



    return render(request, 'index.htm', {
        'contact': contact,
        'cats': cats,
        'tovars': tovars,
        'partners': partners,
        'services': services,
        'feeds': feeds,
        'otzivs': otzivs,
        'foto': foto,
    })



