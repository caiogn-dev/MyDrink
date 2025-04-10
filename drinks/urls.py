from django.urls import path
from . import views

app_name = 'drinks'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('drink/<int:pk>/', views.DrinkDetailView.as_view(), name='drink_detail'),
    path('categorias/', views.CategoriaListView.as_view(), name='categorias'),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('ingredientes/', views.IngredienteListView.as_view(), name='ingredientes'),
    path('busca/', views.busca, name='busca'),
    path('drink/<int:drink_pk>/avaliar/', views.AvaliacaoCreateView.as_view(), name='avaliar'),
    path('sugerir/', views.sugerir_drinks, name='sugerir'),
] 