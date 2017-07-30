from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm, ProductForm, CategoryForm
from .models import Product, Cart, Category

# Create your views here.



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'products/login.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'products/index.html')
            else:
                return render(request, 'products/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'products/login.html', {'error_message': 'Invalid login'})
    return render(request, 'products/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'products/index.html')
    context = {
        "form": form,
    }
    return render(request, 'products/register.html', context)

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:
            return render(request, 'products/index.html')

def swipe(request):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:

        product_ids = []
        #for product in Product.objects.filter(user=request.user):
        for product in Product.objects.all():
            product_ids.append(product.pk)
        return_products = Product.objects.filter(pk__in=product_ids)
        count = Product.objects.filter(pk__in=product_ids).count()
        return render(request, 'products/swipe.html', {
            'product_list': return_products,
            'count': count,
        })

def about(request):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:
            return render(request, 'products/about.html')


def detail(request, product_id):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:
        user = request.user
        product = get_object_or_404(Product, pk=product_id)
        rating = ((product.prating*2)+(product.nrating))*100
        if (rating!=0):
            rating = rating/(((product.prating/2)+product.nrating)*2)
            rating = rating/2
        return render(request, 'products/detail.html', {'product': product, 'user': user, 'rating' : rating})

def addcart(request, product_id):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:
        user = request.user
        product = get_object_or_404(Product, pk=product_id)
        cart = Cart()
        cart.uid = user
        cart.pid = product
        cart.qty = 1
        cart.save()
        return render(request, 'products/detail.html', {'product': product, 'user': user, 'stat': 'Added to cart'})

def showcart(request):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:
        carts = Cart.objects.filter(uid=request.user)
        return render(request, 'products/cart.html', {
            'cart_list': carts,
            'user': request.user,
        })

def delete_cart(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    cart.delete()
    carts = Cart.objects.filter(uid=request.user)
    return render(request, 'products/cart.html', {
        'cart_list': carts,
        'user': request.user,
    })




def ratep(request, product_id):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:
        user = request.user
        product = get_object_or_404(Product, pk=product_id)
        product.prating+=1
        product.save()
        return render(request, 'products/detail.html', {'product': product, 'user': user, 'stat': 'Rated Positively'})

def raten(request, product_id):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:
        user = request.user
        product = get_object_or_404(Product, pk=product_id)
        product.nrating+=1
        product.save()
        return render(request, 'products/detail.html', {'product': product, 'user': user, 'stat': 'Rated Negatively'})


def search(request):
    if not request.user.is_authenticated():
        return render(request, 'products/login.html')
    else:
        products = Product.objects.all()
        query = request.GET.get("q")
        if query:
            products = products.filter(
                Q(pname__icontains=query) |
                Q(pdisc__icontains=query)
            ).distinct()
            return render(request, 'products/search.html', {
                'products': products,
            })
        else:
            return render(request, 'products/search.html')

