from django.shortcuts import render

from ssl_app.models import SSLPage


def ssl_app(request):
    return render(request, 'ssl/index.html', {'ssls': SSLPage.objects.all().order_by('create_date').filter(
        draft=True)})
