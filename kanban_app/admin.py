from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('creator', 'status', 'text', 'date')


admin.site.register(Card, CardAdmin)
