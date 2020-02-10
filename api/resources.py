# api/resources.py
from tastypie.resources import ModelResource
from api.models import Produto,Usuario,Pedido
from tastypie.authorization import Authorization

#o authorization serve para permitir post put e delete sem login, sendo utilizado durante os testes

#resource do produto
class ProdutoResource(ModelResource):
    class Meta:
        queryset = Produto.objects.all()
        resource_name = 'produto'
        authorization = Authorization()
		
#resource do usuario		
class UsuarioResource(ModelResource):
    class Meta:
        queryset = Usuario.objects.all()
        resource_name = 'usuario'
        authorization = Authorization()
		
#resource do pedido
class PedidoResource(ModelResource):
    class Meta:
        queryset = Pedido.objects.all()
        resource_name = 'pedido'
        authorization = Authorization()