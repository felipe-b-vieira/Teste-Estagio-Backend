from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from tastypie.models import create_api_key

#signal do próprio tastypie que permite criar a api key quando o usuário é criado
signals.post_save.connect(create_api_key, sender=User)



#Todos os max_length usados foram selecionados com base em nenhum valor fixo, sendo apenas imaginado qual valor encaixaria.


# Modelo do produto
class Produto(models.Model):
	nome = models.TextField()
	descricao = models.TextField()
	preco = models.FloatField()
	data_criacao = models.DateTimeField(auto_now_add=True)
	estoque = models.IntegerField(default=0)
	
	def __str__(self):
		return self.nome
		
# Modelo do usuario
class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	endereco = models.TextField()
	
	def __str__(self):
		return self.endereco
		
	
		
# Modelo do pedido, utilizado PROTECT no caso de usuário ou produto serem deletados
class Pedido(models.Model):
	produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
	usuario = models.ForeignKey(User, on_delete=models.PROTECT)
	precoTotal = models.FloatField()
	quantItens = models.IntegerField(default=0)
	pago = models.BooleanField()
	
	def __str__(self):
		return self.pago