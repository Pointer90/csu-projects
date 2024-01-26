# Generated by Django 4.2.6 on 2024-01-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSUProjects', '0001_create_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('wid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, verbose_name='ФИО')),
                ('photo', models.ImageField(upload_to='peoples/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
    ]
