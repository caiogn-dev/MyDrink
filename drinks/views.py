from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Drink, Categoria, Ingrediente, Avaliacao
from .forms import AvaliacaoForm

# Create your views here.

class HomeView(ListView):
    model = Drink
    template_name = 'drinks/home.html'
    context_object_name = 'drinks'
    paginate_by = 9

    def get_queryset(self):
        return Drink.objects.all().order_by('-data_criacao')

class DrinkDetailView(DetailView):
    model = Drink
    template_name = 'drinks/drink_detail.html'
    context_object_name = 'drink'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['avaliacao_form'] = AvaliacaoForm()
            try:
                context['minha_avaliacao'] = Avaliacao.objects.get(
                    drink=self.object,
                    usuario=self.request.user
                )
            except Avaliacao.DoesNotExist:
                context['minha_avaliacao'] = None
        return context

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'drinks/categorias.html'
    context_object_name = 'categorias'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'drinks/categoria_detail.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drinks'] = Drink.objects.filter(categoria=self.object)
        return context

class IngredienteListView(ListView):
    model = Ingrediente
    template_name = 'drinks/ingredientes.html'
    context_object_name = 'ingredientes'

def busca(request):
    query = request.GET.get('q', '')
    drinks = Drink.objects.filter(nome__icontains=query) | Drink.objects.filter(descricao__icontains=query)
    return render(request, 'drinks/busca.html', {
        'drinks': drinks,
        'query': query
    })

class AvaliacaoCreateView(LoginRequiredMixin, CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'drinks/avaliacao_form.html'

    def form_valid(self, form):
        drink = get_object_or_404(Drink, pk=self.kwargs['drink_pk'])
        form.instance.drink = drink
        form.instance.usuario = self.request.user
        messages.success(self.request, 'Avaliação enviada com sucesso!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('drinks:drink_detail', kwargs={'pk': self.kwargs['drink_pk']})

def sugerir_drinks(request):
    ingredientes_ids = request.GET.getlist('ingredientes')
    if ingredientes_ids:
        ingredientes = Ingrediente.objects.filter(id__in=ingredientes_ids)
        drinks = Drink.objects.filter(receitas__ingrediente__in=ingredientes).distinct()
        drinks = sorted(drinks, key=lambda d: d.media_avaliacoes, reverse=True)
    else:
        drinks = Drink.objects.none()
        ingredientes = Ingrediente.objects.none()

    return render(request, 'drinks/sugestao.html', {
        'drinks': drinks,
        'ingredientes': ingredientes,
        'ingredientes_selecionados': ingredientes_ids
    })
