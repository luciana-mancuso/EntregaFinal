# Generated by Django 4.1.7 on 2023-04-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0010_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]