from django.shortcuts import render

from product.models import Bot


def bot_list(request):
    context = {
        'object_list': Bot.objects.all()
    }
    return render(request, 'product/bot_list.html', context)
