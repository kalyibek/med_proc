# Generated by Django 4.1.4 on 2022-12-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_proc', '0005_rename_stock_img_processedimage_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='medimage',
            name='proc_img',
            field=models.ImageField(null=True, upload_to='C:\\Users\\Kalyibek\\PycharmProjects\\INAI\\med_srs\\media\\processed_images'),
        ),
        migrations.DeleteModel(
            name='ProcessedImage',
        ),
    ]
