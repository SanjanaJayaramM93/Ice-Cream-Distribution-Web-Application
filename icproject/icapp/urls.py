from django.urls import path
from . import views
urlpatterns = [
      path('',views.index,name='index'),
      path('tubs',views.tubs,name='tubs'),
      path('stores',views.stores,name='stores'),
      path('<int:store_id>',views.single_store,name='single_store')
]