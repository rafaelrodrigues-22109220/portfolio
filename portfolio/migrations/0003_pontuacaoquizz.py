# Generated by Django 4.0.4 on 2022-05-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_post_alter_pessoa_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
    ]
