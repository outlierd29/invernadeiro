# Generated by Django 2.0.4 on 2018-05-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180523_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditoria',
            name='sachanuevocampo',
            field=models.CharField(default='sachanuevo', max_length=255),
        ),
    ]
