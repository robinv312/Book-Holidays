from django.urls import path,include
from . import views
urlpatterns=[
 path('stock',views.StockList.as_view()),
]