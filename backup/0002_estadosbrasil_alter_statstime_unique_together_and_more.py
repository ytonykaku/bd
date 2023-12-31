# Generated by Django 4.2.7 on 2023-12-05 04:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EstadosBrasil",
            fields=[
                (
                    "UF",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="statstime",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="faltas",
            name="jogo",
        ),
        migrations.RemoveField(
            model_name="gols",
            name="jogador_assistencia_obj",
        ),
        migrations.RemoveField(
            model_name="gols",
            name="jogador_marcou_obj",
        ),
        migrations.RemoveField(
            model_name="gols",
            name="jogo",
        ),
        migrations.RemoveField(
            model_name="gols",
            name="time_marcou_obj",
        ),
        migrations.RemoveField(
            model_name="gols",
            name="time_sofreu_obj",
        ),
        migrations.RemoveField(
            model_name="substituicoes",
            name="jogo",
        ),
        migrations.AddField(
            model_name="faltas",
            name="segundo",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gols",
            name="segundo",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="statstime",
            name="time",
            field=models.OneToOneField(
                default=2, on_delete=django.db.models.deletion.CASCADE, to="todos.team"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="substituicoes",
            name="segundo",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="faltas",
            name="jogador_marcou",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="faltas",
            name="jogador_recebeu",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="faltas",
            name="time_marcou",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="faltas_marcou",
                to="todos.team",
            ),
        ),
        migrations.AlterField(
            model_name="faltas",
            name="time_sofreu",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="faltas_sofreu",
                to="todos.team",
            ),
        ),
        migrations.AlterField(
            model_name="gols",
            name="time_marcou",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="gols_marcou",
                to="todos.team",
            ),
        ),
        migrations.AlterField(
            model_name="gols",
            name="time_sofreu",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="gols_sofreu",
                to="todos.team",
            ),
        ),
        migrations.AlterField(
            model_name="jogador",
            name="numero_camisa",
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name="statstime",
            name="nome_time",
            field=models.TextField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="substituicoes",
            name="jogador_entrou",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="substituicoes",
            name="jogador_saiu",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="team",
            name="tecnico",
            field=models.TextField(default="", unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="StatsJogo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_time", models.TextField()),
                ("N_Jogo", models.IntegerField()),
                ("cartao_amarelo", models.IntegerField(default=0)),
                ("cartao_vermelho", models.IntegerField(default=0)),
                ("impedimentos", models.IntegerField(default=0)),
                ("escanteios", models.IntegerField(default=0)),
                ("faltas", models.IntegerField(default=0)),
                ("passes", models.IntegerField(default=0)),
                ("chutes", models.IntegerField(default=0)),
                ("chutes_a_gol", models.IntegerField(default=0)),
                ("posse_de_bola", models.IntegerField(default=0)),
                ("precisao_do_passe", models.IntegerField(default=0)),
                (
                    "jogo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stats_jogo",
                        to="todos.jogo",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="statstime",
            name="id",
        ),
        migrations.AlterField(
            model_name="team",
            name="UF",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="todos.estadosbrasil",
            ),
        ),
    ]
