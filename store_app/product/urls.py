
from django.urls import path
from product.views import contact_us, about_us, productIndex, index, show, delete,  CreateProductView, UpdateProductView
urlpatterns = [
    path('contactus', contact_us),
    path('aboutus', about_us),
    path('all', productIndex, name="products.all"),
    path('all_products_page', index, name="products.index"),
    path("<int:id>", show, name="products.show"),
    path('delete/<int:id>', delete, name="product.delete"),
    path('create', CreateProductView.as_view(), name="product.create"),
    path('edit/<int:pk>', UpdateProductView.as_view(), name="product.edit")
]
