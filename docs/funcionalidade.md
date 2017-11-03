---
layout: default
---

## Tabela de Funcionalidade
A tabela funcionalidade tem os seguintes atributos : funcionalidade_id, funcionalidade_codigo, funcionalidade_nome, funcionalidade_desc, funcionalidade_caminho, funcionalidade_caminho_imagem, funcionalidade_status, sistema_id.

|   coluna    | descrição           | tipo de dado |
|:------------|---------------------|--------------|
| funcionalidade_id  | O atributo funcionalidade_id é uma chave primária e será a identificação de cada objeto cadastrado no banco de dados.  | int(11) |
| funcionalidade_codigo | No atributo funcionalidade_codigo fica é um identificador literal composto pelo prefixo do sistema e funcionalidade_id | varchar(20) |
| funcionalidade_nome | No atributo funcionalidade_nome fica armazenado o nome da funcionalidade cadastrada | varchar(100) |
| funcionalidade_desc | No atributo funcionalidade_desc fica armazenada a descrição da funcionalidad cadastrada | varchar(200) |
| sistema_id  | O atributo sistema_id é uma chave estrangeira e será a identificação do sistema que contém a funcionalidade.  | int(11) |
| funcionalidade_caminho | No atributo funcionalidade_caminho fica armazenado o caminho (url) para acesso da funcionalidado dentro do sistema (definido por sistema_id) | varchar(100) |
| funcionalidade_caminho_imagem | No atributo funcionalidade_caminho_imagem fica armazenado o caminho para a imagem usada para representar a funcionalidade | varchar(100) |
| funcionalidade_status  | O atributo funcionalidade_status determina se a funcionalidade está ou não ativada  | int(11) |


![](http://www.cdn.ueg.br/source/mobilidade_nacional_211/noticias/31283/uea.png)
