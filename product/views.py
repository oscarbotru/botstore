from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import Bot


# def bot_list(request):
#     context = {
#         'object_list': Bot.objects.all()
#     }
#     return render(request, 'product/bot_list.html', context)


class BotListView(ListView):
    model = Bot
    # paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
        return queryset


class BotDetailView(DetailView):
    model = Bot
    # template_name = 'product/bot_detail.html'
