from django.shortcuts import render
from django.utils import timezone
from .models import Game, Category
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    games_new = Game.objects.order_by('created_date')[:3][::-1]
    return render(request, 'games/index.html', {'games_new': games_new})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})

#def game_list(request, pk):
#    game_list = get_object_or_404(Category, pk=pk)
#   return render(request, 'games/game_list.html', {'game_list': game_list})