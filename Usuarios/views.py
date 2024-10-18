from django.shortcuts import redirect,render

# Create your views here.
def banner(request):
    return render(request, 'banner.html')