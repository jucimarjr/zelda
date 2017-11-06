--
-- Database: zelda
--
DROP DATABASE IF EXISTS zelda;
CREATE SCHEMA zelda;
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
  setor_id int(11) AUTO_INCREMENT NOT NULL,
  setor_nome varchar(100) NOT NULL,
  setor_pai int(11),
  setor_situacao int(11) NOT NULL DEFAULT '0',
   
  PRIMARY KEY (setor_id),
  FOREIGN KEY (setor_pai) REFERENCES zelda.setor(setor_id)
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

-- --------------------------------------------------------

--
-- Estrutura da tabela perfil
--

DROP TABLE IF EXISTS perfil;
CREATE TABLE perfil (
  perfil_id int(11) AUTO_INCREMENT NOT NULL,
  perfil_nome varchar(50) NOT NULL,

  PRIMARY KEY(perfil_id)
);

-- ------------------------------------------------

--
-- Estrutura da tabela usuario
--

DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario (
  usuario_id int(11) AUTO_INCREMENT NOT NULL,
  usuario_login varchar(100) NOT NULL,
  usuario_senha varchar(50),
  usuario_email varchar(100) NOT NULL,
  usuario_status int(11) NOT NULL DEFAULT '0',
  usuario_caminho_foto varchar(100),

  perfil_id int(11) NOT NULL,

  PRIMARY KEY (usuario_id),
  FOREIGN KEY (perfil_id) REFERENCES zelda.perfil(perfil_id)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela sistema
--

DROP TABLE IF EXISTS sistema;
CREATE TABLE sistema (
  sistema_id int(11) AUTO_INCREMENT NOT NULL,
  sistema_nome varchar(75) NOT NULL,
  sistema_desc varchar(300),
  sistema_status int(11) NOT NULL DEFAULT '0',
  sistema_prefixo varchar(10) NOT NULL, /* Prefixo usado para descrever funcionalidades do sistema (ZD) */

  PRIMARY KEY(sistema_id)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela funcionalidade
--

DROP TABLE IF EXISTS funcionalidade;
CREATE TABLE funcionalidade (
  funcionalidade_id int(11) AUTO_INCREMENT NOT NULL,
  funcionalidade_codigo varchar(20) NOT NULL,
  funcionalidade_nome varchar(100) NOT NULL,
  funcionalidade_desc varchar(200),
  funcionalidade_caminho varchar(150) NOT NULL,
  funcionalidade_caminho_imagem varchar(150),
  funcionalidade_status int(11) NOT NULL DEFAULT '0',
  
  sistema_id int(11) NOT NULL,

  PRIMARY KEY(funcionalidade_id),
  FOREIGN KEY(sistema_id) REFERENCES zelda.sistema (sistema_id)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela permissão
--

DROP TABLE IF EXISTS permissao;
CREATE TABLE permissao (
  permissao_id int(11) AUTO_INCREMENT NOT NULL,

  funcionalidade_id int(11) NOT NULL,
  perfil_id int(11) NOT NULL,

  PRIMARY KEY(permissao_id),
  FOREIGN KEY(perfil_id) REFERENCES zelda.perfil(perfil_id),
  FOREIGN KEY(funcionalidade_id) REFERENCES zelda.funcionalidade(funcionalidade_id)

);