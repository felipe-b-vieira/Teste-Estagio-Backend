"""notable_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from api.resources import ProdutoResource,UsuarioResource,PedidoResource,AuthenticationResource

produto_resource = ProdutoResource()
usuario_resource = UsuarioResource()
pedido_resource = PedidoResource()
auth_resource = AuthenticationResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(produto_resource.urls)),
    url(r'^api/', include(usuario_resource.urls)),
    url(r'^api/', include(pedido_resource.urls)),
    url(r'^api/', include(auth_resource.urls)),
]