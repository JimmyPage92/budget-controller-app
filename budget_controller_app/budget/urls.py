from . import views
from django.urls import path
from . import views
from .views import IncomeCreateView, ExpanseCreateView, UpdateIncomeView, UpdateExpanseView, IncomeDeleteView,\
    ExpanseDeleteView, ExpanseDetailView, IncomeDetailView

urlpatterns = [
    path('user_page/', views.home_user_page, name='user-page'),#strona zalogowanego uzytkownika
    path('about_app/', views.about, name='about-page'),
    path('income/<int:pk>', IncomeDetailView.as_view(), name='income-detail'),
    path('expanse/<int:pk>', ExpanseDetailView.as_view(), name='expanse-detail'),
    path('income/new/', IncomeCreateView.as_view(), name='income-create'),
    path('expanse/new/', ExpanseCreateView.as_view(), name='expanse-create'),
    path('income/update/<int:pk>', UpdateIncomeView.as_view(), name='income-update'),
    path('expanse/update/<int:pk>', UpdateExpanseView.as_view(), name='expanse-update'),
    path('income/delete/<int:pk>', IncomeDeleteView.as_view(), name='income-delete'),
    path('expanse/delete/<int:pk>', ExpanseDeleteView.as_view(), name='expanse-delete'),
]