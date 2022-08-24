from django.contrib import admin

from domain.models import DomainPage


@admin.register(DomainPage)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'draft']
    list_filter = ['create_date']
    exclude = ['now_date']
    list_editable = ['draft']

