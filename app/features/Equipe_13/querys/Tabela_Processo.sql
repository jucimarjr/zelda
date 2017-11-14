
DROP TABLE IF EXISTS processo;

CREATE TABLE processo (
  processo_id int(11) AUTO_INCREMENT NOT NULL,
  processo_descricao varchar(100) NOT NULL,
  processo_tipo int(11) NOT NUll,
  
  usuario_id int(11) NOT NULL,
  PRIMARY KEY (processo_id),
  FOREIGN KEY(usuario_id) REFERENCES zelda.usuario(usuario_id)
);

DROP TABLE IF EXISTS docs;
CREATE TABLE docs (
  docs_id int(11) AUTO_INCREMENT NOT NULL,
  docs_descricao varchar(100) NOT NULL,
  docs_tipo int(11) NOT NUll,
  docs_link varchar(100) NOT NULL,
  
  processo_id int(11) NOT NULL,
  PRIMARY KEY (docs_id),
  FOREIGN KEY(processo_id) REFERENCES zelda.processo(processo_id)
);