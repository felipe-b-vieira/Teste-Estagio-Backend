from django.db import models

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
class Usuario(models.Model):
	nomeUsuario = models.CharField(max_length=100)
	senha = models.CharField(max_length=50)
	email= models.CharField(max_length=100)
	primeiroNome = models.CharField(max_length=50)
	ultimoNome = models.CharField(max_length=50)
	endereco = models.TextField()
	
	def __str__(self):
		return self.nomeUsuario
		
# Modelo do pedido, utilizado PROTECT no caso de usuário ou produto serem deletados
class Pedido(models.Model):
	produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
	usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
	precoTotal = models.FloatField()
	quantItens = models.IntegerField(default=0)
	pago = models.BooleanField()
	
	def __str__(self):
		return self.pago