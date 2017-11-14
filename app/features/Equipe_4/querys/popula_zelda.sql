/* Insere o Zelda na tabela sistema */
use zelda;
INSERT INTO `sistema` (`sistema_id`, `sistema_nome`, `sistema_desc`, `sistema_status`, `sistema_prefixo`) VALUES (NULL, 'Zelda', 'Sistema de autenticação de serviços da UEA', '0', 'ZD');

/* Popula as funcionalidades do Zelda */
INSERT INTO `funcionalidade` (`funcionalidade_id`,`funcionalidade_codigo`, `funcionalidade_nome`, `funcionalidade_desc`, `funcionalidade_caminho`, `funcionalidade_caminho_imagem`, `funcionalidade_status`, `sistema_id`) VALUES (NULL,'ZD0001', 'Menu de Funcionários', 'Provê acesso a uma lista de todos os funcionários cadastrados no sistema e exibe seus campos. Possibilita também a edição, cadastro e desativação dos registros listados', '/funcionario', '/static/assets/funcionalidades_imagens/menu_funcionarios.png', '0', '1');
INSERT INTO `funcionalidade` (`funcionalidade_id`,`funcionalidade_codigo`, `funcionalidade_nome`, `funcionalidade_desc`, `funcionalidade_caminho`, `funcionalidade_caminho_imagem`, `funcionalidade_status`, `sistema_id`) VALUES (NULL,'ZD0002', 'Menu de Setores', 'Provê acesso a uma lista de todos os setores cadastrados no sistema e exibe seus campos. Possibilita também a edição, cadastro e desativação dos registros listados', '/setor', '/static/assets/funcionalidades_imagens/menu_setores.png', '0', '1');
INSERT INTO `funcionalidade` (`funcionalidade_id`,`funcionalidade_codigo`, `funcionalidade_nome`, `funcionalidade_desc`, `funcionalidade_caminho`, `funcionalidade_caminho_imagem`, `funcionalidade_status`, `sistema_id`) VALUES (NULL,'ZD0003', 'Menu de Usuários', 'Provê acesso a uma lista de todos os usuários cadastrados no sistema e exibe seus campos. Possibilita também a edição, cadastro e exclusão dos registros listados', '/usuario', '/static/assets/funcionalidades_imagens/menu_usuarios.png', '0', '1');
INSERT INTO `funcionalidade` (`funcionalidade_id`,`funcionalidade_codigo`, `funcionalidade_nome`, `funcionalidade_desc`, `funcionalidade_caminho`, `funcionalidade_caminho_imagem`, `funcionalidade_status`, `sistema_id`) VALUES (NULL,'ZD0004', 'Menu de Sistemas', 'Provê acesso a uma lista de todos os sistemas cadastrados no banco e exibe seus campos. Possibilita também a edição, cadastro e desativação dos registros listados', '/sistema', '/static/assets/funcionalidades_imagens/menu_sistemas.png', '0', '1');
INSERT INTO `funcionalidade` (`funcionalidade_id`,`funcionalidade_codigo`, `funcionalidade_nome`, `funcionalidade_desc`, `funcionalidade_caminho`, `funcionalidade_caminho_imagem`, `funcionalidade_status`, `sistema_id`) VALUES (NULL,'ZD0005', 'Menu de Funcionalidades', 'Provê acesso a uma lista de todas as funcionalidades cadastradas no banco e exibe seus campos. Possibilita também a edição, cadastro e desativação dos registros listados', '/funcionalidade', '/static/assets/funcionalidades_imagens/menu_funcionalidades.png', '0', '1');
INSERT INTO `funcionalidade` (`funcionalidade_id`,`funcionalidade_codigo`, `funcionalidade_nome`, `funcionalidade_desc`, `funcionalidade_caminho`, `funcionalidade_caminho_imagem`, `funcionalidade_status`, `sistema_id`) VALUES (NULL,'ZD0006', 'Menu de Perfis', 'Provê acesso a uma lista de todos os perfis cadastrados no banco e exibe seus campos. Possibilita também a edição, cadastro e desativação dos registros listados', '/perfil', '/static/assets/funcionalidades_imagens/menu_perfis.png', '0', '1');
/* Popula os perfis do Zelda */
INSERT INTO `perfil` (`perfil_id`, `perfil_nome`) VALUES (NULL, 'Administrador');
INSERT INTO `perfil` (`perfil_id`, `perfil_nome`) VALUES (NULL, 'Usuário Comum');

/* Define as permissões de cada perfil (assumindo que o perfil administrador ficou com o id 1) */
INSERT INTO `permissao` (`permissao_id`, `funcionalidade_id`, `perfil_id`) VALUES (NULL, '1', '1');
INSERT INTO `permissao` (`permissao_id`, `funcionalidade_id`, `perfil_id`) VALUES (NULL, '2', '1');
INSERT INTO `permissao` (`permissao_id`, `funcionalidade_id`, `perfil_id`) VALUES (NULL, '3', '1');
INSERT INTO `permissao` (`permissao_id`, `funcionalidade_id`, `perfil_id`) VALUES (NULL, '4', '1');
INSERT INTO `permissao` (`permissao_id`, `funcionalidade_id`, `perfil_id`) VALUES (NULL, '5', '1');
INSERT INTO `permissao` (`permissao_id`, `funcionalidade_id`, `perfil_id`) VALUES (NULL, '6', '1');

/* Insere um admin no banco (usuario: Administrador, email: admin@uea.edu.br, senha: caiorolandodarocha) */
INSERT INTO `usuario` (`usuario_id`, `usuario_login`, `usuario_senha`, `usuario_email`, `usuario_status`, `perfil_id`) VALUES (NULL, 'Administrador', '709b4aa0e4fa0cfee2dc7662c5fe156f', 'admin@uea.edu.br', '1', '1');
