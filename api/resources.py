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
from tastypie.authorization import Authorization


#o authorization serve para permitir post put e delete sem login, sendo utilizado durante os testes
	
#resource do produto
class ProdutoResource(ModelResource):
	class Meta:
		queryset = Produto.objects.all()
		resource_name = 'produto'
		authorization = Authorization()

		
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
		authorization = Authorization()
		
#resource do pedido
class PedidoResource(ModelResource):
	class Meta:
		queryset = Pedido.objects.all()
		resource_name = 'pedido'
		authorization = Authorization()
		

class AuthenticationResource(ModelResource):

	def __get_api_key_for_user(self, user):
		return '%s' % (user.api_key.key)

	class Meta:
		resource_name = 'authentication'
		queryset = User.objects.all()
		allowed_methods = ['post']

	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/login%s$" %
				(self._meta.resource_name, trailing_slash()),
				self.wrap_view('login'), name="api_login"),
		]


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