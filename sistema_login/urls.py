from django.urls import path
from .views import cadastro_view, login_view, perfil_view, logout_view

urlpatterns = [
    path('cadastro/', cadastro_view, name='cadastro'),
    path('login/', login_view, name='login'),
    path('perfil/', perfil_view, name='perfil'),
    path('logout/', logout_view, name='logout'),
]
