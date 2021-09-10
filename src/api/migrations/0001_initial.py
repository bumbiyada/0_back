# Generated by Django 3.2.5 on 2021-07-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Foiv', models.CharField(blank=True, default='', max_length=64, verbose_name='ФОИВ')),
                ('Document_type', models.CharField(blank=True, default='', max_length=64, verbose_name='Тип документа')),
                ('Document_number', models.CharField(blank=True, default='', max_length=64, verbose_name='Номер документа')),
                ('Document_init_data', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания документа')),
                ('Stage_name', models.CharField(blank=True, max_length=64, verbose_name='Этап')),
                ('Stage_data', models.DateTimeField(blank=True, null=True, verbose_name='Дата проведения этапа')),
                ('Stage_user', models.CharField(blank=True, default='', max_length=64, verbose_name='Исполнитель')),
                ('Is_aborted', models.BooleanField(default=False, verbose_name='Прервана')),
                ('Is_done', models.BooleanField(default=True, verbose_name='Выполнена')),
                ('Marked_on_delete', models.BooleanField(default=False, verbose_name='Пометка на удаление')),
            ],
            options={
                'db_table': 'documents',
            },
        ),
    ]
