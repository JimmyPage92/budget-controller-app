from django.urls import path
from . import views

urlpatterns = [
    path('user_page/', views.home_user_page, name='user-page'),  # strona zalogowanego uzytkownika
    path('about_app/', views.about, name='about-page'),
    path('income/<int:pk>', views.IncomeDetailView.as_view(), name='income-detail'),
    path('expanse/<int:pk>', views.ExpanseDetailView.as_view(), name='expanse-detail'),
    path('income/new/', views.IncomeCreateView.as_view(), name='income-create'),
    path('expanse/new/', views.ExpanseCreateView.as_view(), name='expanse-create'),
    path('income/update/<int:pk>', views.UpdateIncomeView.as_view(), name='income-update'),
    path('expanse/update/<int:pk>', views.UpdateExpanseView.as_view(), name='expanse-update'),
    path('income/delete/<int:pk>', views.IncomeDeleteView.as_view(), name='income-delete'),
    path('expanse/delete/<int:pk>', views.ExpanseDeleteView.as_view(), name='expanse-delete'),
    path('expanse/plan/', views.plan_expanses, name='plan-expanse'),
    path('expanse/plan/sum/', views.plan_expanses, name='plan-expanse-sum'),
    path('send_email/', views.send_email, name='send-test-email'),
]
