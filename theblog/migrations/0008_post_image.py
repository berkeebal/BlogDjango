# Generated by Django 3.1.5 on 2021-01-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_auto_20210116_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Images/'),
        ),
    ]
