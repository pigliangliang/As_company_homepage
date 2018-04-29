# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['votes'], 'verbose_name': '\u9009\u62e9', 'verbose_name_plural': '\u9009\u62e9'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['pub_date'], 'verbose_name': '\u95ee\u9898', 'verbose_name_plural': '\u95ee\u9898'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name=b'\xe9\x80\x89\xe6\x8b\xa9\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\xa5\xa8\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98'),
        ),
    ]
