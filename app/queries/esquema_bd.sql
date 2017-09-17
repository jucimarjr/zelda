--
-- Database: zelda
--
CREATE DATABASE IF NOT EXISTS zelda;
USE zelda;

-- --------------------------------------------------------

--
-- Estrutura da tabela funcionario
--

DROP TABLE IF EXISTS funcionario;
CREATE TABLE funcionario (
  funcionario_id int(11) AUTO_INCREMENT NOT NULL,
  funcionario_nome varchar(100) NOT NULL,
  funcionario_situacao int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (funcionario_id)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela setor
--

DROP TABLE IF EXISTS setor;
CREATE TABLE setor (
  setor_id int(11) NOT NULL,
  setor_nome varchar(50) NOT NULL,
  setor_pai int(11),
  setor_situacao int(11) NOT NULL DEFAULT '0',

  FOREIGN KEY (setor_pai) REFERENCES zelda.setor(setor_id)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela usuario
--

DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario (
  usuario_id int(11) AUTO_INCREMENT NOT NULL,
  usuario_login varchar(100) NOT NULL,
  usuario_senha varchar(50),
  usuario_logado int(11) NOT NULL DEFAULT '1',
  usuario_admin int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (usuario_id)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela lotacao
--

DROP TABLE IF EXISTS lotacao;
CREATE TABLE lotacao (
  lotacao_id int(11) AUTO_INCREMENT NOT NULL,
  funcionario_id int(11) NOT NULL,
  setor_id int(11) NOT NULL,

  PRIMARY KEY (lotacao_id),
  FOREIGN KEY (funcionario_id) REFERENCES zelda.funcionario (funcionario_id),
  FOREIGN KEY (setor_id) REFERENCES zelda.setor(setor_id)
);
