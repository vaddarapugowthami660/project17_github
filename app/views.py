from django.shortcuts import render

# Create your views here.
def operators(request):
    d={'a':101}
    return render(request,'operators.html',d)


def operators1(request):
    d={'a':104,'b':103,}
    return render(request,'operators1.html',d)

def operators2(request):
    d={'a':3,'b':7,'c':8}
    return render(request,'operators2.html',d)

def operators3(request):
    d={'a':3,'b':7,'c':8}
    return render(request,'operators3.html',d)
