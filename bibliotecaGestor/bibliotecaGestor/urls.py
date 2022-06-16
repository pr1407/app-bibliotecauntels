"""bibliotecaGestor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from biblioteca import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('buscarLibro/', views.buscar, name='buscar'),
    path('elminiarLibro/<int:idlibro>', views.eliminar, name='eliminar'),
    path('editarLibro/<int:idlibro>', views.editar, name='editar'),
    path('registrarP/', views.registrarP, name='registrarP'),
    path('registrarLibro/', views.registrar, name='registrar'),
    path('devolver/', views.devolverP, name='devolver'),
    path('editarP/<int:idprestamo>', views.editarP, name='editarP'),
]
