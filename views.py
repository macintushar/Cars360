from django.shortcuts import render, redirect
from cars.forms import CarForm
from cars.models import Names


# Create your views here.
def new(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass

    else:
        form = CarForm()
        return render(request, 'new.html',{'form':form})


def index(request):
    cars = Names.objects.all()
    return render(request, 'index.html', {'name':cars})


def edit(request, id):  
    names = Names.objects.get(id=id)  
    return render(request,'edit.html', {'name':names})  


def update(request, id):  
    car = Names.objects.get(id=id)  
    form = CarForm(request.POST, instance = car)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'name': car})  


def destroy(request, id):  
    car = Names.objects.get(id=id)  
    car.delete()  
    return redirect("/")  