# api/resources.py
from api.models import Produto,Perfil,Pedido
from tastypie import fields
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from tastypie.http import HttpUnauthorized, HttpForbidden, HttpNotFound
from tastypie.authentication import ApiKeyAuthentication
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from tastypie.authorization import DjangoAuthorization,Authorization
from tastypie.authentication import ApiKeyAuthentication,Authentication


#a classe abaixo é usado para autenticar apenas em certos requests
class ApiKeyAuthenticationFiltrado(ApiKeyAuthentication):

    #para o get de produtos e de detalhes de produto, não tem necessidade de autenticação, e é isso que esse código faz, permitindo get passar direto
	def is_authenticated(self, request, **kwargs):
		""" If GET, don't check auth, otherwise fall back to parent """
		if request.method == "GET":
			return True
		else:
			return super(ApiKeyAuthenticationFiltrado, self).is_authenticated(request, **kwargs)

#o authorization serve para permitir post put e delete sem login, sendo utilizado durante os testes


#resource do produto
class ProdutoResource(ModelResource):
	data_criacao = fields.DateTimeField(attribute='data_criacao', use_in='detail')
	descricao = fields.CharField(attribute='descricao', use_in='detail')
	
	class Meta:
		queryset = Produto.objects.all()
		resource_name = 'produto'
		authorization = Authorization()
		include_resource_uri = False
		authentication = ApiKeyAuthenticationFiltrado()
		
	#altera o json de saida para o padrão
	def alter_list_data_to_serialize(self, request, data):
		if 'objects' in data:
			d = {'products': ""}
			d['products'] = data.pop('objects')
			return d
		return data
	

		
#resource do perfil	
class PerfilResource(ModelResource):
	class Meta:
		queryset = Perfil.objects.all()
		resource_name = 'perfil'
		
#resource do usuario		
class UsuarioResource(ModelResource):
	perfil = fields.OneToOneField(PerfilResource, 'perfil', related_name='profile', full=True)
	class Meta:
		queryset = User.objects.all()
		resource_name = 'usuario'
		fields = ['username','email','perfil']
		authorization = DjangoAuthorization()
		authentication = ApiKeyAuthentication()
		
#resource do pedido
class PedidoResource(ModelResource):
	class Meta:
		queryset = Pedido.objects.all()
		resource_name = 'pedido'
		authorization = DjangoAuthorization()
		authentication = ApiKeyAuthentication()
		

class AuthenticationResource(ModelResource):

	def __get_api_key_for_user(self, user):
		return '%s' % (user.api_key.key)

	class Meta:
		resource_name = 'auth'
		queryset = User.objects.all()
		allowed_methods = ['post']

	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/login%s$" %
				(self._meta.resource_name, trailing_slash()),
				self.wrap_view('login'), name="api_login"),
		]
	
	#para esse resource, não é necessário verificar alguma autenticação do usuário, esse é o próprio objetivo do POST, verificar e retornar a Key caso positivo.
	#Por isso, temos a mudança do is_authenticated para garantir que ele possa mandar a requisição sem nenhum tipo de autorização
	def is_authenticated(self, request, **kwargs):
		""" If POST, don't check auth, otherwise fall back to parent """
		if request.method == "POST":
			return True
		else:
			return super(AnonymousPostAuthentication, self).is_authenticated(request, **kwargs)


	def login(self, request, **kwargs):
		self.method_check(request, allowed=['post'])
		data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))
		username = data.get('usuario', '')
		password = data.get('senha', '')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				last_login = user.last_login
				login(request, user) # updates the last login
				return self.create_response(request, {
					'api_key': self.__get_api_key_for_user(user),
					})
			else:
				return self.create_response(request, {
					'success': False,
					'reason': 'disabled',
					}, HttpForbidden )
		else:
			return self.create_response(request, {
				'success': False,
				'reason': 'Incorrect user name or password',
				}, HttpUnauthorized )