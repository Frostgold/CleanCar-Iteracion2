# Generated by Django 2.2.16 on 2020-10-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CleanCar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cod', models.IntegerField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='slider')),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
