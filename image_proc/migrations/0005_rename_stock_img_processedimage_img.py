# Generated by Django 4.1.4 on 2022-12-10 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_proc', '0004_alter_processedimage_med_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processedimage',
            old_name='stock_img',
            new_name='img',
        ),
    ]
