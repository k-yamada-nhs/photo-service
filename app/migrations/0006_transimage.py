# Generated by Django 2.2.6 on 2019-10-31 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.ImageField(upload_to='projects/1/base')),
                ('style', models.ImageField(upload_to='projects/1/style')),
            ],
        ),
    ]