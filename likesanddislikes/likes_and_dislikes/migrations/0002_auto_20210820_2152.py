# Generated by Django 3.2.6 on 2021-08-21 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes_and_dislikes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.CharField(blank=True, max_length=64, null=True)),
                ('dislike', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='player',
            name='like',
        ),
        migrations.AlterField(
            model_name='player',
            name='lobby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='likes_and_dislikes.lobby'),
        ),
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='likes_and_dislikes.card')),
                ('guessed_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guessed_as', to='likes_and_dislikes.player')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guess', to='likes_and_dislikes.player')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='likes_and_dislikes.player'),
        ),
    ]
