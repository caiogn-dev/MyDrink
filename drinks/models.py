from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=50, choices=[
        ('acido', 'Ácido'),
        ('doce', 'Doce'),
        ('alcoolico', 'Alcoólico'),
        ('nao_alcoolico', 'Não Alcoólico')
    ])

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    unidade_medida = models.CharField(max_length=50)
    preco_medio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

class Drink(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='drinks/', null=True, blank=True)
    tempo_preparo = models.IntegerField(help_text='Tempo de preparo em minutos')
    dificuldade = models.CharField(max_length=20, choices=[
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil')
    ])
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    media_avaliacoes = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_avaliacoes = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    def atualizar_avaliacao(self):
        avaliacoes = self.avaliacoes.all()
        if avaliacoes:
            self.media_avaliacoes = sum(a.nota for a in avaliacoes) / len(avaliacoes)
            self.total_avaliacoes = len(avaliacoes)
        else:
            self.media_avaliacoes = 0
            self.total_avaliacoes = 0
        self.save()

    class Meta:
        verbose_name = 'Drink'
        verbose_name_plural = 'Drinks'

class Receita(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='receitas')
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    instrucoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.drink.nome} - {self.ingrediente.nome}"

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

class Avaliacao(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('drink', 'usuario')
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.drink.atualizar_avaliacao() 