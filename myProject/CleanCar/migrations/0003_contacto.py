# Generated by Django 2.2.16 on 2020-11-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CleanCar', '0002_insumo_slider_vision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=15)),
                ('mensaje', models.TextField(max_length=200)),
            ],
        ),
    ]
