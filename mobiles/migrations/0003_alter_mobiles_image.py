# Generated by Django 4.2.7 on 2023-12-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0002_alter_mobiles_options_alter_mobiles_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='image',
            field=models.ImageField(default='photos/1.jpg', upload_to='photos/%y/%m/%d'),
        ),
    ]
