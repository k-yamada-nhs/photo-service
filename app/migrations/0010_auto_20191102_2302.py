# Generated by Django 2.2.6 on 2019-11-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191102_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='style',
            field=models.FileField(default=1, upload_to='style'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.FileField(upload_to='base'),
        ),
    ]
