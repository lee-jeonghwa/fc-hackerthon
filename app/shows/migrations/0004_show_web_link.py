# Generated by Django 2.1.3 on 2018-11-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_show_pick_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='web_link',
            field=models.URLField(blank=True, null=True, verbose_name='웹주소'),
        ),
    ]
