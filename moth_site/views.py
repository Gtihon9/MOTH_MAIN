from django.shortcuts import render

# Create your views here.
def hello_page(request):
    return render(request, 'moth_site/hello.html')

def base_page(request):
    return render(request, 'moth_site/base.html')