from django.contrib import admin

from ssl_app.models import SSLPage


@admin.register(SSLPage)
class SSLAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'draft']
    list_filter = ['create_date']
    exclude = ['now_date']
    list_editable = ['draft']

