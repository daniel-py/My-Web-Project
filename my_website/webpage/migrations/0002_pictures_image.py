# Generated by Django 2.2.5 on 2020-02-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='image',
            field=models.ImageField(default='placeholder.jpg', upload_to='img'),
            preserve_default=False,
        ),
    ]