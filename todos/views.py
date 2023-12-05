from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Jogo
from .models import Team
from .models import Jogador
from .models import Substituicoes
from .models import StatsTime
from .models import StatsJogador
from .models import Faltas
from .models import Gols

from .forms import JogadorForm


def times_list(request):
    jogo = Jogo.objects.all()
    team = Team.objects.all()
    jogador = Jogador.objects.all()
    substituicoes = Substituicoes.objects.all()
    statstime = StatsTime.objects.all()
    statsjogador = StatsJogador.objects.all()
    faltas = Faltas.objects.all()
    gols = Gols.objects.all()

    return render(request,
                "todos/times_list.html", {"times": team})

def placar_list(request):
    jogo = Jogo.objects.all()
    team = Team.objects.all()
    jogador = Jogador.objects.all()
    substituicoes = Substituicoes.objects.all()
    statstime = StatsTime.objects.all()
    statsjogador = StatsJogador.objects.all()
    faltas = Faltas.objects.all()
    gols = Gols.objects.all()

    return render(request,
                "todos/placar_list.html", {"jogo": jogo})

def jogador_list(request):
    jogo = Jogo.objects.all()
    team = Team.objects.all()
    jogador = Jogador.objects.all()
    substituicoes = Substituicoes.objects.all()
    statstime = StatsTime.objects.all()
    statsjogador = StatsJogador.objects.all()
    faltas = Faltas.objects.all()
    gols = Gols.objects.all()

    return render(request,
                "todos/jogador_list.html", {"jogador": jogador})

def statsjogador_list(request):
    jogo = Jogo.objects.all()
    team = Team.objects.all()
    jogador = Jogador.objects.all()
    substituicoes = Substituicoes.objects.all()
    statstime = StatsTime.objects.all()
    statsjogador = StatsJogador.objects.all()
    faltas = Faltas.objects.all()
    gols = Gols.objects.all()

    return render(request,
                "todos/statsjogador.html", {"statsjogador": statsjogador})


def cadastrar_jogador(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jogadorlist')  # Redirecione para a página desejada após o cadastro
    else:
        form = JogadorForm()

    return render(request, 'adicionar_jogador.html', {'form': form})

def atualizar_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('pagina_listagem_jogadores')  # Redireciona para a página de listagem de jogadores
    else:
        form = JogadorForm(instance=jogador)

    return render(request, 'atualizar_jogador.html', {'form': form, 'jogador': jogador})

