# Generated by Django 2.2.6 on 2019-12-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadImage',
        ),
        migrations.AddField(
            model_name='photo',
            name='latitude',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='longitude',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
