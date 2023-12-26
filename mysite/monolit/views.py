from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .forms import Register
from .models import *

def index(request):
    products = Product.objects.order_by("-release_date")[:5]
    context = {"products": products}
    return render(request, "home.html", context)

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = Register
    success_url = reverse_lazy('index')

class LoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('index')

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'user/logout.html'

class PostView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.order_by('-release_date')[:5]

class ProfileListView(LoginRequiredMixin, ListView):
    model = Basket
    context_object_name = 'baskets'
    template_name = 'user/profile.html'

def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, countProduct=1)
        return redirect('profile')
    else:
        basket = baskets.first()
        basket.countProduct += 1
        basket.save()
        return redirect('profile')

class ProductsAll(ListView):
    model = Product
    template_name = 'Products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.order_by('-release_date')

class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
