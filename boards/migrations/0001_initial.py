# Generated by Django 4.1.3 on 2022-11-16 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='태그이름')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
            ],
            options={
                'verbose_name_plural': '태그',
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
                ('tag', models.ManyToManyField(blank=True, to='boards.tag', verbose_name='태그')),
            ],
            options={
                'verbose_name_plural': '게시판',
            },
        ),
    ]
