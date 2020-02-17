from django.shortcuts import render


def erro_404(request, exception):
        data = {}
        return render(request,'erro_404.html', data)

def erro_500(request):
        data = {}
        return render(request,'erro_500.html', data)