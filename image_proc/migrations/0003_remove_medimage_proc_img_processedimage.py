# Generated by Django 4.1.4 on 2022-12-10 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_proc', '0002_alter_medimage_proc_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medimage',
            name='proc_img',
        ),
        migrations.CreateModel(
            name='ProcessedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_img', models.ImageField(upload_to='C:\\Users\\Kalyibek\\PycharmProjects\\INAI\\med_srs\\media\\stock_images')),
                ('med_img', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='image_proc.medimage')),
            ],
        ),
    ]
