# Generated by Django 3.2.6 on 2021-09-01 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
