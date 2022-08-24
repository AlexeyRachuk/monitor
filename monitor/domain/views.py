from django.shortcuts import render

from domain.models import DomainPage


def domain(request):
    return render(request, 'domain/index.html', {'domains': DomainPage.objects.all().order_by('create_date').filter(
        draft=True)})
