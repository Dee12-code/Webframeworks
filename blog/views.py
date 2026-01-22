from django.shortcuts import render

def home(request):
    context = {'message': "This is my blog of the year"}
    return render(request, 'blog/home.html', context)