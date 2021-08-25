from django.shortcuts import render
from .text_generator import create

# Create your views here.

def text_generation(request):
    context = {}
    if request.method == "POST":
        file = request.FILES.get("file")
        if file.name.lower().endswith(('.txt')):
            context['output'] = create(file.read().decode('utf-8'))

    return render(request, 'McCloud/text_generation.html', context)


 