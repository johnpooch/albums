# Generated by Django 2.0.6 on 2018-06-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='owner',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
