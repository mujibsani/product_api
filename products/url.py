from django.urls import path
from .views import *
urlpatterns = [

    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),
    path('product/<int:pk>/attribute/', ProductAttributeListView.as_view()),
    path('product/<int:pk>/attribute/<int:id>/', ProductAttributeView.as_view()),
    path('product/<int:pk>/price/', ProductPriceListView.as_view()),
    path('product/<int:pk>/price/<int:id>/', ProductPriceView.as_view()),

]
