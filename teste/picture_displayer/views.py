from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Image

images = [
    {   "id":0,
        "image": "asdahdi3u2i2jtghq3408tghfrae0gmnva"},
    {"id":1,"image": "acprmjp3r83wptvm4n3c743ta3txc34t,x7tg3"},
    {"id":2,"image": ",watv0384+0hxt4.340+ym3qt,«30+v4rq2,m56ty«"},
]

#The home is a list of images 
def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request,'picture_displayer/image_list.html', context)

#This is to add images
def add_image(request):
    if request.method == 'POST':
        filename = request.POST['image_name']
        uploaded_file = request.FILES['Image']
        image = Image(name = filename, image = uploaded_file)
        image.save()
        return redirect('/')
    return render(request,'picture_displayer/add_image.html')

def view_image(request,pk):
    received_image = Image.objects.get(pk=pk)
    received_image.image = str(received_image.image) 

    context = {
        'image': Image.objects.get(pk=pk)
    }

    return render(request,'picture_displayer/view_image.html', context)

def delete_image(request,pk):
    Image.objects.filter(id=pk).delete()
    return redirect('/')