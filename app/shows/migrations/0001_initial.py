# Generated by Django 2.1.3 on 2018-11-15 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='댓글 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글 목록',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='전시명')),
                ('period', models.CharField(max_length=200, verbose_name='전시기간')),
                ('thumbnail', models.ImageField(upload_to='thumbnail', verbose_name='썸네일')),
                ('poster', models.ImageField(upload_to='poster', verbose_name='포스터')),
                ('description', models.TextField(blank=True, null=True, verbose_name='상세설명')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='가격')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일자')),
            ],
            options={
                'verbose_name': '전시',
                'verbose_name_plural': '전시 목록',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ShowPick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Show')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Show'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shows.Show', verbose_name='전시회'),
        ),
        migrations.AlterUniqueTogether(
            name='showpick',
            unique_together={('show', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('show', 'user')},
        ),
    ]