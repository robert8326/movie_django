# Generated by Django 3.2.6 on 2021-08-11 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезды рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
    ]
