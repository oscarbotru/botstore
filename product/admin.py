from django.contrib import admin

from product.models import Bot, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

    search_fields = ('name', 'description',)

    inlines = [ImageInline]
