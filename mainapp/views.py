from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')
    pass


def products(request):
    links_menu = [
        {'href': 'products_all', 'titel': 'все'},
        {'href': 'products_home', 'titel': 'дом'},
        {'href': 'products_office', 'titel': 'офис'},
        {'href': 'products_modern', 'titel': 'модерн'},
        {'href': 'products_classic', 'titel': 'класика'},

    ]

    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')

