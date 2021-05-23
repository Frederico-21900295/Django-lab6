from django.shortcuts import render


def home_page_view(request):
    return render(request, 'website/base.html')


def home_page_view(request):
    return render(request, 'website/home.html')


def home1_page_view(request):
    return render(request, 'website/home1.html')


def home2_page_view(request):
    return render(request, 'website/home2.html')
