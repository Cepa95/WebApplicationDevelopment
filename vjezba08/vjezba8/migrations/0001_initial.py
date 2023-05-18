# Generated by Django 4.2.1 on 2023-05-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predmeti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kod', models.CharField(max_length=10)),
                ('program', models.TextField(max_length=50)),
                ('ects', models.IntegerField()),
                ('sem_red', models.IntegerField()),
                ('sem_izv', models.IntegerField()),
                ('izborni', models.CharField(choices=[('DA', 'da'), ('NE', 'ne')], max_length=10)),
            ],
        ),
    ]
