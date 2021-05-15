from django.shortcuts import render, HttpResponse
from home.form import ImageForm
from home.models import Image

def index(request):
    context={
        'message': "this is message"
    }
    # return HttpResponse("This is Home Page")
    return render(request, 'index.html', context)
def diagnosis(request):
    return render(request, 'diagnosis.html')

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    return HttpResponse("This is Contact Page")

def checkView(request):
    return render(request, "output.html")
# Create your views here.
def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'diagnosis.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'diagnosis.html', {'form': form})