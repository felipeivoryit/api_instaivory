# Generated by Django 2.2 on 2019-04-23 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaivory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instaivoryusuario',
            name='senha',
        ),
    ]
