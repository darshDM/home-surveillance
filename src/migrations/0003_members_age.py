# Generated by Django 3.1.7 on 2021-03-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='age',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
