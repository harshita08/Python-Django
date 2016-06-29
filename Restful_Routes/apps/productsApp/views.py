from django.shortcuts import render, redirect
from .models import Product, ProdManager

def index(request):
	# show all the products
	context = {
		"all_products": Product.objects.all()
	}
	return render(request, 'productsApp/index.html', context)


def show(request, id):
	context = {
		"all_products": Product.objects.get(id=id)
	}
	return render(request, 'productsApp/show.html', context)


def new(request):
	return render(request, 'productsApp/add.html')


def edit(request, id):
	context = {
		"all_products": Product.objects.get(id=id)
	}
	return render(request, 'productsApp/edit.html', context)
	

def create(request):
	product_tuple = Product.prodManager.create(request.POST['name'], request.POST['description'], request.POST['price'])
	data = {}
	for k,v in product_tuple[1].iteritems():
		data["message"] = v
			#'message': product_tuple[1]}
	return render(request,'productsApp/add.html', data)


def destroy(request, id):
	Product.prodManager.filter(id=id).delete()
	return redirect('/products')


def update(request, id):
	prod_edit_tuple = Product.prodManager.edit(id, request.POST['name'], request.POST['description'], request.POST['price'])
	data = {'bool': prod_edit_tuple[0],
			'message': prod_edit_tuple[1]}
	return redirect('/products', data)
