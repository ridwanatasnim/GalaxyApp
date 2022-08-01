from django.urls import path,re_path
from .import views


urlpatterns = [
    path('', views.product_queries, name='product_queries'),
    path('category/', views.product_category, name='product_category'),
    re_path(r'^category/(?P<category>[a-zA-Z_]+)', views.product_group_by_category, name='product_group_by_category'),
    re_path(r'^subcategory/(?P<category>[a-zA-Z_]+)/(?P<sub_category>[0-9a-zA-Z_]+)', views.product_group_by_sub_category, name='product_group_by_sub_category'),
    path('thana_list/', views.thana_list, name='thana_list'),
    path('market_list/', views.market_list, name='market_list'),
    path('district_list/', views.district_list, name='district_list'),

]
