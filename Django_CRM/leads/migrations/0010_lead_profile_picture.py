# Generated by Django 3.2.9 on 2022-01-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_auto_20220129_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
