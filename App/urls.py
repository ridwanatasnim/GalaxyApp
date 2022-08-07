from django.urls import path,re_path
from .import views

urlpatterns = [
   
    path('category/', views.product_category, name='product_category'),
    path('orders/', views.orders, name='orders'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('update_stock/', views.update_stock, name='update_stock'),
    
    re_path(r'^category/(?P<category>[a-zA-Z_]+)', views.product_group_by_category, name='product_group_by_category'),
    re_path(r'^subcategory/(?P<category>[a-zA-Z_]+)/(?P<sub_category>[0-9a-zA-Z_]+)', views.product_group_by_sub_category, name='product_group_by_sub_category'),
    re_path(r'^order_details/(?P<order_id>[A-Z0-9_]+)/', views.order_details, name='order_details'),
    path('thana_list/', views.thana_list, name='thana_list'),
    path('market_list/', views.market_list, name='market_list'),
    path('district_list/', views.district_list, name='district_list'),

]
