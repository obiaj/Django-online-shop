from django.shortcuts import render,redirect
from .form import SignupForm
from item.models import Category,Item
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
#items = Item.objects.filter(is_sold=False)[0:6]
#categories = Category.objects.all().order_by('?')


def index(request):

    user=User.objects.filter(username=request.user)
    
    P = Paginator(Category.objects.all(),3)
    P2 = Paginator(Item.objects.filter(is_sold=False),6)
    page2 = request.GET.get('page')
    page = request.GET.get('page')
    categories = P.get_page(page2)
    items=P2.get_page(page)
    return render(request,'core/index.html',{
        'categories': categories,
        'items':items,
        'user':user
    })


def contact(request):
    return render(request,'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:

        form = SignupForm()

    return render(request,'core/signup.html',{
        'form':form
    })
