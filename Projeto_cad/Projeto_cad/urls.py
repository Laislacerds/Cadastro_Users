from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios-cadastrados/', views.usuarios_cadastrados, name='usuarios_cadastrados'),
]