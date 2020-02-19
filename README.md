# Teste Estágio API Django

Esse projeto irá conter o teste de estágio com objetivo de criar uma API utilizando o Django.
A API será colocado no Heroku.

O comando para ativar o virtualenv é '.\envpythonapi\Scripts\activate.bat'

Abaixo serão adicionadas informações em relação a documentação e utilização da API.

A API é composta de três entidades e seus respectivos campos:

Pedidos:
• Produto (foreign key)
• Usuário (foreign key)
• Quantidade de itens (integer)
• Preço total (float)
• Pago (boolean)

Usuários:
• Nome de usuário (string)
• Senha (string)
• Email (string)
• Primeiro Nome (string)
• Último Nome (string)
• Endereço (string)

Produtos
• Nome (string)
• Descrição (string)
• Preço (float)
• Data de criação (date)
• Estoque (integer)

#Comandos

Importante observar que as requisições API abaixo precisam apresentar / no final da url, para que a requisição seja feita com sucesso.

#Usuários

• GET - Retorna um JSON com a lista de produtos.
Comando livre sem necessidade de autenticação, é necessário utilizar a url:
./api/produto/ sem envio de nenhum body.
A informação retornada será um json contendo um conjunto de produtos com quatro campos: Id, nome, preco e estoque.
• GET - Retorna um JSON com a informação detalhada de 1 produto.
Comando livre sem necessidade de autenticação, é necessário utilizar a url:
./api/produto/id/ sem envio de nenhum body.
A informação retornada será um json contendo um único produto com seis campos: Id, nome, preco, data_criacao, descricao e estoque.
• POST - Cria um novo produto
Comando que é necessário autenticação por Api Key, é necessário utilizar a url:
./api/produto/ com envio de body com as informações do produto.Data de criação é criada automaticamente.
A informação retornada será um json contendo as informações detalhadas do produto criado.
• DELETE - Remove o produto criado
Comando que é necessário autenticação por Api Key, é necessário utilizar a url:
./api/produto/id sem envio de body.
Não será retornada informação.
• PATCH - Atualiza produto
Comando que é necessário autenticação por Api Key, é necessário utilizar a url:
./api/produto/ enviando as informações que busca atualizar no body. A data de criação não pode ser alterada.
A informação retornada será um json contendo as informações detalhadas do produto alterado.


#Usuário

• POST - Obter token de usuário registrado
Para o login de usuário e recuperação da API Key, é necessário utilizar a url:
./api/auth/login/ com o body em json enviando o "usuario" e "senha".
A informação retornada será um json contendo apenas a API Key.