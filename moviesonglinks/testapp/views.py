from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm
def h1(request):
    return render(request,"testapp/index.html")
def h2(request):
    form=MovieForm()
    if request.method=="POST":
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return h1(request)
    return render(request,"testapp/addmovie.html",{"form":form})
def h3(request):
    m1=Movie.objects.all()
    return render(request,"testapp/movielink.html",{"m1":m1})
