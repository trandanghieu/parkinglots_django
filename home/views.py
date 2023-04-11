from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def pricing(request):
    return render(request,'pricing.html')

def testimonial(request):
    return render(request,'testimonial.html')

def why(request):
    return render(request,'why.html')
