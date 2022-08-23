from django.shortcuts import render, redirect
from .models import Clients
from .forms import UserForm
from django.http import HttpResponseRedirect, HttpResponseNotFound


def index(request):
    table = Clients.objects.order_by('last_name').all()
    current_month_january, current_month_february, current_month_march = '', '', ''
    current_month_april, current_month_may, current_month_june = '', '', ''
    current_month_july, current_month_august, current_month_september = '', '', ''
    current_month_october, current_month_november, current_month_december = '', '', ''
    current_month_august, current_month_september, current_month_october = '', '', ''
    money_january, money_february, money_march = 0, 0, 0
    money_april, money_may, money_june = 0, 0, 0
    money_july, money_august, money_september = 0, 0, 0
    money_october, money_november, money_december = 0, 0, 0

    for tables in table:
        if tables.month == 'Январь':
            current_month_january = tables.month
            money_january += tables.money
        elif tables.month == 'Февраль':
            current_month_february = tables.month
            money_february += tables.money
        elif tables.month == 'Март':
            current_month_march = tables.month
            money_march += tables.money
        elif tables.month == 'Апрель':
            current_month_april = tables.month
            money_april += tables.money
        elif tables.month == 'Май':
            current_month_may = tables.month
            money_may += tables.money
        elif tables.month == 'Июнь':
            current_month_june = tables.month
            money_june += tables.money
        elif tables.month == 'Июль':
            current_month_july = tables.month
            money_july += tables.money
        elif tables.month == 'Август':
            current_month_august = tables.month
            money_august += tables.money
        elif tables.month == 'Сентябрь':
            current_month_september = tables.month
            money_september += tables.money
        elif tables.month == 'Октябрь':
            current_month_october = tables.month
            money_october += tables.money
        elif tables.month == 'Ноябрь':
            current_month_november = tables.month
            money_november += tables.money
        elif tables.month == 'Декабрь':
            current_month_december = tables.month
            money_december += tables.money

    month = {
        'current_month_january': current_month_january, 'current_month_february': current_month_february,
        'current_month_march': current_month_march, 'current_month_april': current_month_april,
        'current_month_may': current_month_may, 'current_month_june': current_month_june,
        'current_month_july': current_month_july, 'current_month_august': current_month_august,
        'current_month_september': current_month_september, 'current_month_october': current_month_october,
        'current_month_november': current_month_november, 'current_month_december': current_month_december,
        'table': table, 'money_january': money_january, 'money_february': money_february, 'money_march': money_march,
        'money_april': money_april, 'money_may': money_may, 'money_june': money_june, 'money_july': money_july,
        'money_august': money_august, 'money_september': money_september, 'money_october': money_october,
        'money_november': money_november,
        'money_december': money_december
    }
    return render(request, 'index.html', month)


def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit(request, id):
    client = Clients.objects.get(id=id)
    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.last_name = request.POST.get('last_name')
        client.money = request.POST.get('money')
        client.month = request.POST.get('month')
        client.service = request.POST.get('service')
        client.save()
        return HttpResponseRedirect('/')
    return render(request, 'edit.html', {'client': client})





def delete(request, id):
    try:
        klient = Clients.objects.get(id=id)
        klient.delete()
        return HttpResponseRedirect('/')
    except Clients.DoesNotExist:
        return HttpResponseNotFound('<h2>Kлиент не найден</h2>')


