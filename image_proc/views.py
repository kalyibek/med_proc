import os
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from PIL import Image, ImageFilter
from . import models


def index(request):
    med_images = models.MedImage.objects.all()
    context = {
        'med_images': med_images,
    }

    return render(request, 'index.html', context)


def proc(request):
    if request.method == 'POST':
        title = request.POST['title']
        img = request.FILES['stock_img']
        img_type = request.POST['type']

        new_med_img = models.MedImage.objects.create(
            title=title,
            stock_img=img,
            proc_img=img,
            type=img_type,
        )

        with Image.open(new_med_img.proc_img) as img:
            img.load()
            img_proc = img.convert("L")

            edges = img_proc.filter(
                ImageFilter.Kernel(
                    (3, 3),
                    (0, 1, 0, 1, -4, 1, 0, 1, 0),
                    1, 1
                )
            )

            edges.save(os.path.join(settings.MEDIA_ROOT, new_med_img.proc_img.path))

        return redirect(reverse('index'))

    return render(request, 'proc.html')


def delete(request, pk):
    med_img = models.MedImage.objects.get(pk=pk)
    os.remove(
        os.path.join(
            settings.MEDIA_ROOT,
            med_img.stock_img.path
        )
    )

    os.remove(
        os.path.join(
            settings.MEDIA_ROOT,
            med_img.proc_img.path
        )
    )

    med_img.delete()

    return redirect(reverse('index'))

