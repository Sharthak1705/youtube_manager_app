from django.shortcuts import render
from .models import Chai
from .forms import ChaiForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def chai_list(request):
    chais = Chai.objects.all().order_by('-created_at')
    return render(request,'chai_list.html', {'Chai':
    chais})

def chai_create(request):
    if request.method == "POST":
       form = ChaiForm(request.POST, request.FILES)
       if form.is_valid():
           chai = form.save(commit=False)
           chai.user = request.user
           chai.save()
           return redirect('chai_list')
       
    else:
        form = ChaiForm()
    return render(request,'chai_form.html', {'form': form} )

   
def chai_edit(request, chai_id):
    chai = get_object_or_404(Chai, pk =chai_id, user =request.user)
    if request.method == 'POST':
        form = ChaiForm(request.POST, request.FILES, instance= chai)
        if form.is_valid():
            chai = form.save(commit=False)
            chai.user = request.user
            chai.save()
            return redirect('chai_list')

    else:
      form = ChaiForm(instance = chai)
    return render(request, 'chai_form.html', {'form':form})


def chai_remove(request, chai_id):
    chai =  get_object_or_404(Chai, pk =chai_id, user = request.user)
    if request.method == 'POST':
        chai.delete()
        return redirect('chai_list')
    return render(request, 'chai_confirm.html', {'chai': chai})



