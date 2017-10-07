---
layout: default
---

## Tabela de Setor
A tabela  do setor, tem os seguintes atributos: setor_id, setor_nome, setor_situação, setor_pai.

|     coluna     | descrição                                 | tipo de dado |
|:---------------|------------------------------------------ |--------------|
| setor_id  | No atributo setor_id, ficam armazenados os dados referentes a identificação de cada setor, onde cada setor é identificado de forma única, ou seja, o setor_id é uma chave primária.  | int |
| setor_nome  |  No atributo setor_nome, ficam armazenados os dados referentes ao nome de cada setor, pois cada setor tem que ter um nome. | varchar[50]  |
| setor_situacao  |  No atributo setor_situação, ficam armazenados os dados referentes a situação de cada setor, ele é responsável por indicar o se o setor está ativo ou não. | int |
| setor_pai |  No atributo setor_pai, ficam armazenados o id do setor_pai, ou seja ele recebe um valor inteiro, identificando o setor superior de cada setor que está abaixo da hieráquia.  | int |


![](http://www.cdn.ueg.br/source/mobilidade_nacional_211/noticias/31283/uea.png)
