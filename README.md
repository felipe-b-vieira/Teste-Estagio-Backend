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

Para o login de usuário e recuperação da API Key, é necessário utilizar a url:
./api/authentication/login/ com o body em json enviando o "usuario" e "senha".
A informação retornada será um json contendo apenas a API Key.