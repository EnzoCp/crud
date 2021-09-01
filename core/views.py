from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        quantidade = request.POST['quantidade']
        preco = request.POST['preco']
        product = Product.objects.create(nome=nome, descricao=descricao,
                                         quantidade=quantidade, preco=preco,
                                         )
        return redirect('home')
    else:
        return render(request, 'addproduct.html')


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return render(request, 'home.html', {'message': f'Product {product.nome} deletado'})
