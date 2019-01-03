from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<int:pk>/', views.game_detail, name='game_detail')
    #path('game/(?P<pk>[0-9]+)/$/', views.game_list, name='game_list')
]