# Generated by Django 2.2.6 on 2019-11-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191112_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='comment',
            field=models.TextField(default='comment', max_length=255),
            preserve_default=False,
        ),
    ]
