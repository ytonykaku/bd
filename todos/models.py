from django.db import models


class EstadosBrasil(models.Model):
    UF = models.CharField(primary_key=True, max_length=2)


class Faltas(models.Model):
    N_Jogo = models.IntegerField()
    jogador_recebeu = models.IntegerField()
    jogador_marcou = models.IntegerField()
    time_marcou = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='faltas_marcou')
    time_sofreu = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='faltas_sofreu')
    minuto = models.IntegerField()
    segundo = models.IntegerField(default=0)


class Gols(models.Model):
    N_Jogo = models.IntegerField()
    jogador_marcou = models.IntegerField()
    jogador_assistencia = models.IntegerField()
    time_marcou = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='gols_marcou')
    time_sofreu = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='gols_sofreu')
    minuto = models.IntegerField()
    segundo = models.IntegerField(default=0)


class Jogador(models.Model):
    bid = models.IntegerField(primary_key=True)
    nome = models.TextField()
    idade = models.IntegerField()
    posicao = models.TextField(default='0')
    numero_camisa = models.IntegerField(unique=True, default=0)
    nome_time = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)


class Jogo(models.Model):
    N_Jogo = models.IntegerField(primary_key=True)
    estadio = models.TextField()
    time_visitante = models.TextField()
    time_mandante = models.TextField()
    placar_visitante = models.IntegerField()
    placar_mandante = models.IntegerField()
    N_rodada = models.IntegerField()


class StatsJogador(models.Model):
    bid = models.IntegerField(primary_key=True)
    faltas_sofridas = models.IntegerField(default=0)
    faltas_feitas = models.IntegerField(default=0)
    numero_de_gols = models.IntegerField(default=0)
    amarelos = models.IntegerField(default=0)
    vermelhos = models.IntegerField(default=0)
    numero_de_assistencias = models.IntegerField(default=0)
    jogador = models.OneToOneField(Jogador, on_delete=models.CASCADE)


class StatsJogo(models.Model):
    nome_time = models.TextField()
    N_Jogo = models.IntegerField()
    cartao_amarelo = models.IntegerField(default=0)
    cartao_vermelho = models.IntegerField(default=0)
    impedimentos = models.IntegerField(default=0)
    escanteios = models.IntegerField(default=0)
    faltas = models.IntegerField(default=0)
    passes = models.IntegerField(default=0)
    chutes = models.IntegerField(default=0)
    chutes_a_gol = models.IntegerField(default=0)
    posse_de_bola = models.IntegerField(default=0)
    precisao_do_passe = models.IntegerField(default=0)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='stats_jogo')


class StatsTime(models.Model):
    nome_time = models.TextField()
    mando_de_campo = models.TextField()
    gols_marcados = models.IntegerField(default=0)
    gols_sofridos = models.IntegerField(default=0)
    vitorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    empates = models.IntegerField(default=0)
    pontos = models.IntegerField(default=0)
    saldo_de_gols = models.IntegerField(default=0)
    num_jogos = models.IntegerField(default=0)
    time = models.OneToOneField('Team', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nome_time', 'mando_de_campo'], name='unique_statstime_entry')
        ]
        managed = False  # Isso desativa a criação automática de tabelas

    def save(self, *args, **kwargs):
    # Sobrescreva o método save para evitar a criação automática do campo 'id'
        pass


class Substituicoes(models.Model):
    N_Jogo = models.IntegerField()
    jogador_saiu = models.IntegerField()
    jogador_entrou = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    minuto = models.IntegerField()
    segundo = models.IntegerField(default=0)


class Team(models.Model):
    nome_time = models.TextField(primary_key=True)
    serie = models.CharField(max_length=1)
    UF = models.ForeignKey(EstadosBrasil, on_delete=models.CASCADE, null=True)
    tecnico = models.TextField(unique=True, default='')
