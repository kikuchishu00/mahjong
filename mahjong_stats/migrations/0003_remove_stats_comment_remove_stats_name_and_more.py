# Generated by Django 4.1.7 on 2023-02-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahjong_stats', '0002_alter_stats_name_delete_player_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='name',
        ),
        migrations.AlterField(
            model_name='stats',
            name='date',
            field=models.DateField(verbose_name='日付'),
        ),
    ]