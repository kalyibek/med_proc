import os
from django.db import models
from django.conf import settings


class MedImage(models.Model):
    TYPES = (
        ('heart', 'сердце'),
        ('lungs', 'легкие'),
        ('stomach', 'желудок'),
        ('liver', 'печень'),
        ('kidneys', 'почки'),
    )

    title = models.CharField(max_length=100)

    stock_img = models.ImageField(
        upload_to=os.path.join(
            settings.MEDIA_ROOT,
            'stock_images'
        )
    )

    proc_img = models.ImageField(
        upload_to=os.path.join(
            settings.MEDIA_ROOT,
            'processed_images'
        ),
        null=True,
    )

    type = models.CharField(choices=TYPES, max_length=100)
    posted_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
