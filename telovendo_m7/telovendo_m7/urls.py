"""
URL configuration for telovendo_m7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sitio_web import views as vistas_web
from gestion import views as vistas_gestion
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vistas_web.registro, name='landing'),
    path('registro/', vistas_web.registro, name='registro'),
    path('login/',auth_views.LoginView.as_view(template_name = 'pagina/login.html'), name='login' ),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'pagina/logout.html'), name='logout' ),
    path('lista_pedidos/', vistas_gestion.ListaPedidosView.as_view(), name='lista_pedidos'),
]
