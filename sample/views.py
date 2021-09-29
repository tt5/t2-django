from django.shortcuts import render

# Create your views here.
def some(request):
    return render(request, 'sample/some.html')
