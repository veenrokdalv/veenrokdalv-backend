# Generated by Django 4.1.2 on 2022-10-08 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkAlias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата и время добавления')),
                ('modified_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата и время изменения')),
                ('url', models.URLField(verbose_name='Url адресс')),
                ('alias', models.CharField(max_length=32, verbose_name='Псевдоним')),
            ],
            options={
                'verbose_name': 'Сокращенная ссылка',
                'verbose_name_plural': 'Сокращенные ссылки',
            },
        ),
    ]