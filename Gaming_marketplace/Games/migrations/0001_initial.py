# Generated by Django 4.2.5 on 2023-10-22 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=50)),
                ('creator', models.TextField(max_length=50)),
                ('genre', models.TextField(max_length=150)),
                ('year', models.IntegerField(max_length=20)),
            ],
        ),
    ]
