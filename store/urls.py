from django.urls import path
from . import views
from contacts.views import contact

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('faq/', views.faq, name='faq'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]
