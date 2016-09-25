# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 22:38
from __future__ import unicode_literals

from itertools import groupby

from django.db import migrations, models


def update_counter(apps, schema_editor):
    Signature = apps.get_model("signatures", "Signature")
    object_list = Signature.objects.all()
    for _, g in groupby(object_list, lambda x: x.petition_id):
        for i, signature in enumerate(g):
            signature.counter = i
            signature.save(update_fields=['petition'])


class Migration(migrations.Migration):

    dependencies = [
        ('signatures', '0005_auto_20160921_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='counter',
            field=models.SmallIntegerField(default=1, verbose_name='No.'),
            preserve_default=False,
        ),
        migrations.RunPython(update_counter)
    ]