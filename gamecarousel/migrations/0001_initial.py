# Generated by Django 4.0.3 on 2022-04-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('gameno', models.AutoField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('gname', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField()),
                ('rating', models.SmallIntegerField(max_length=5)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
