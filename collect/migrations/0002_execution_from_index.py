# Generated by Django 2.2 on 2019-05-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='execution',
            name='from_index',
            field=models.BooleanField(default=False, verbose_name='If from index template?'),
        ),
    ]
