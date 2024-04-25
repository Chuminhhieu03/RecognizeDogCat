from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image

# Create your views here.
from app.model.predict import predict
import io


def index(request):
    return render(request, 'index.html')


def recognize(request):
    if request.method == "POST":
        image = request.FILES['image']
        pil_image = Image.open(image).convert("RGB")  # Convert the image to RGB
        image_io = io.BytesIO()
        pil_image.save(image_io, format='JPEG')  # Save the image in JPEG format
        a = predict(image_io.getvalue())  # Get the image content as bytes
        return JsonResponse({'result': 'success', 'message': f"This is a {a}"})