# Generated by Django 3.2.7 on 2021-09-15 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_wizard', '0002_auto_20190306_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='run',
            options={'ordering': ('-pk',), 'verbose_name': 'data wizard', 'verbose_name_plural': 'data wizard'},
        ),
    ]