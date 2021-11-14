# Generated by Django 3.2.9 on 2021-11-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('competance', models.CharField(max_length=1000)),
                ('langue', models.CharField(max_length=500)),
                ('interet', models.CharField(max_length=500)),
                ('objectif', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.TextField()),
                ('Projet', models.TextField()),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
