---
layout: default
---

## Tabela de Usuário
A tabela usuário tem os seguintes atributos : usuario_id, usuario_email, usuario_login, usuario_senha, usuario_perfil_id, usuario_logado e usuario_status.
|   coluna    | descrição           | tipo de dado |
|:------------|---------------------|--------------|
| usuario_id  | O atributo usuario_id é uma chave primária e será a identificação de cada objeto cadastrado no banco de dados.  | int(11) |
| usuario_email | No atributo usuario_email, fica armazenado o email que o usuário cadastrou | varchar(50) |
| usuario_login | No atributo usuario_login, ficam armazenados os dados referentes ao login que o usuário cadastrou | varchar(100) |
| usuario_senha | No atributo usuario_senha, fica armazenado a senha que o usuário cadastrou  | varchar(50) |
| usuario_perfil_id | No atributo usuario_perfil_id, irá guardar o id do perfil do usuário. | int(11) |
| usuario_logado| No atributo usuario_logado, irá definir se o usuário está logado, definindo como 1 caso esteja logado ou 0 caso contrário | int(11) |
| usuario_status| O atributo usuario_status determina se o email do usuario foi confirmado | int(11) |

![](http://www.cdn.ueg.br/source/mobilidade_nacional_211/noticias/31283/uea.png)
