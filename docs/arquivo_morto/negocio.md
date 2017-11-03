---
layout: default
---

# [1.](#header-1) DIAGRAMAS DE USO
## [1.1](#header-2) Usuário
- O usuário poderá fazer login;
- Enquanto o usuário estiver logado, poderá fazer logout.
- O usuário poderá visualizar seus dados;

## [1.2](#header-3) Administrador
- O administrador poderá fazer login;
- Enquanto o administrador estiver logado, poderá fazer logout.
- O administrador poderá visualizar seus dados;
- O administrador poderá listar usuários;
- Nesta lista, o administrador poderá cadastrar, editar e desativar um ou mais usuários.
- O administrador poderá listar funcionários;
- Nesta lista, o administrador poderá cadastrar, editar e desativar um ou mais funcionários.
- O administrador poderá listar setores;
- Nesta lista, o administrador poderá cadastrar, editar e desativar um ou mais setores.

* * *
# [2.](#header-4) DIAGRAMAS DE ATIVIDADES – CASOS DE USO DO USUÁRIO
## [2.1](#header-5) Login
- O usuário insere o seu nome de usuário e sua senha.
- O sistema verifica se o nome do usuário existe.
- Se o nome do usuário não existe, o usuário é visualizado com uma mensagem de erro e terá de inserir o nome de usuário e senha corretos como no item 2.1.
- Se o nome do usuário existe, o sistema verifica se a senha está correta.
- O sistema verifica se a senha está correta.
- Se a senha não está correta, o sistema alerta ao usuário que sua senha está incorreta, visualizando uma mensagem de erro para o usuário e ele terá de inserir o nome de usuário e senha corretos como no item 2.1.
- Se a senha está correta, o sistema inicia a sessão do usuário e redireciona para a tela adequada.
- O sistema inicia a sessão do usuário e redireciona para a tela adequada, finalizando o processo.
## [2.2](#header-6) Logout
- Enquanto logado, o usuário clica em sair.
- O sistema encerra a sessão do usuário.
- O sistema redireciona para a tela de login e finaliza o processo.
## [2.3](#header-7) Visualização de Dados de Usuário
- O usuário vai para a tela inicial.
- O sistema recupera os dados do usuário.
- O sistema exibe os dados do usuário na tela.
- O usuário ver os dados na tela e finaliza o processo.

* * *
# [3.](#header-8) DIAGRAMAS DE ATIVIDADES – CASOS DE USO DO ADMINISTRADOR
## [3.1](#header-9) Login
- O administrador insere o seu nome de usuário e sua senha.
- O sistema verifica se o nome do usuário existe.
- Se o nome do usuário não existe, o administrador é visualizado com uma mensagem de erro e terá de inserir o nome de usuário e senha corretos como no primeiro item.
- Se o nome do usuário existe, o sistema verifica se a senha está correta.
- O sistema verifica se a senha está correta.
- Se a senha não está correta, o sistema alerta ao administrador que sua senha está incorreta, visualizando uma mensagem de erro para o administrador e ele terá de inserir o nome de usuário e senha corretos como no primeiro item.
- Se a senha está correta, o sistema inicia a sessão do usuário e redireciona para a tela adequada.
- O sistema inicia a sessão do administrador o e redireciona para a tela adequada, finalizando o processo.

## [3.2](#header-10) Logout
- Enquanto logado, o administrador clica em sair.
- O sistema encerra a sessão do administrador.
- O sistema redireciona para a tela de login e finaliza o processo.


## [3.3](#header-11) Visualização de Dados de Administrador
- O administrador vai para a tela inicial.
- O sistema recupera os dados do administrador.
- O sistema exibe os dados do administrador na tela.
- O administrador visualiza os dados na tela e finaliza o processo.

* * *

# [4.](#header-12) DIAGRAMAS DE ATIVIDADES – CASOS DE USO DO ADMINISTRADOR - USUÁRIOS
## [4.1](#header-13) Listar Usuários
- O administrador vai para a tela de menu de usuários.
- O sistema requisita todos os usuários do banco.
- O sistema mostra a lista de usuários recuperados na tela.
- O administrador ver a lista de usuários recuperados e finaliza o processo.

## [4.2](#header-14) Cadastrar Usuário
- O administrador vai para a tela de cadastro de usuários preencher os campos do novo usuário.
- Se o administrador clicou em cancelar, o sistema redireciona para a tela de menu de usuários, interrompendo o processo.
- Se o administrador clicou em confirmar, o sistema valida os campos inseridos pelo usuário.
- O sistema valida os campos inseridos pelo usuário.
- Se os campos forem inválidos, o administrador terá de preencher os campos do novo usuário como no item 2.1.
- Se os campos forem válidos, o sistema cadastra o novo usuário no banco.
- O sistema cadastra o novo usuário no banco.
- O sistema redireciona para a tela de menu de usuário e finaliza o processo.

## [4.3](#header-15) Editar Usuário
- O administrador irá para tela de edição de usuários.
- Se o administrador não acessar a tela pela URL, ele irá para a tela de menu de usuários e logo em seguida selecionara os itens da lista.
- Se o administrador clicar em um item da lista, o sistema definira o ID do usuário a ser editar como o ID do item clicado na lista e logo em seguida, redirecionara para a tela de edição de usuário enviando o ID como parâmetro.
- Se o administrador clicar no botão editar, o sistema definira o ID do usuário a ser editado como ID do primeiro item selecionado na lista e logo em seguida, redirecionara para a tela de edição de usuário enviando o ID como parâmetro.
- Se o administrador for acessar a tela pela URL ou retornar de uma página posterior, o sistema verificará se o ID recebido como parâmetro corresponde a um usuário válido.
- O sistema verificará se o ID recebido como parâmetro corresponde a um usuário válido.
- Se o ID não for válido, o sistema redireciona para a tela de menu de usuário, interrompendo o processo.
- Se o ID for válido, o sistema recupera os dados do usuário de ID equivalente ao valor recebido como parâmetro.
- O sistema vai popular os campos de edição de dados da tela com os dados atuais do usuário.
- O administrador altera os valores dos campos do usuário conforme desejado.
- Se o administrador clicou em cancelar as alterações, o sistema redireciona para a tela de menu de usuário, interrompendo o processo.
- Se o administrador clicou em confirmar as alterações, o sistema valida os valores dos campos do formulário.
- O sistema valida os valores dos campos do formulário.
- Se os valores dos campos forem inválidos, o sistema vai popular os campos de edição de dados da tela com os dados - atuais do usuário como no item 3.3.
- Se os valores dos campos forem válidos, o sistema verifica se a lotação do usuário foi alterada.
- O sistema salva suas alterações do usuário no banco.
- O sistema redireciona para a tela de menu de usuários e finaliza o processo.

## [4.4](#header-16) Desativar Usuário
- O administrador vai acessar a tela de desativação de usuário.
- Se o administrador não for acessar pela URL, ele vai para a tela de menu de usuários, seleciona os itens da lista e clica em desativar.
- O sistema define a lista de IDs dos usuários a serem desativados como os IDs dos itens selecionados.
- O sistema redireciona para a tela de desativação de usuário enviando a lista de IDs como parâmetro.
- O sistema recupera os dados dos usuários que correspondem com os IDs recebidos como parâmetro no banco.
- O sistema mostra um resumo dos dados dos usuários a serem desativados na tela.
- Se o administrador for acessar pela URL e não reenviar dados pelo formulário, o sistema redireciona para a tela de menu de usuários, interrompendo o processo.
- O sistema mostra um resumo dos dados dos usuários a serem desativados na tela.
- Se o administrador clicou em cancelar, o sistema redireciona para a tela de menu de usuários, interrompendo o processo.
- Se o administrador clicou em confirmar, o sistema desativa os usuários no banco.
- O sistema desativa os usuários no banco.
- O sistema redireciona para a tela de menu de usuários e finaliza o processo.

* * *

# [5.](#header-17) DIAGRAMAS DE ATIVIDADES – CASOS DE USO DO ADMINISTRADOR - FUNCIONÁRIOS
## [5.1](#header-18) Listar Funcionários
- O administrador vai para a tela de menu de funcionários.
- O sistema requisita todos os funcionários do banco.
- O sistema mostra a lista de funcionários recuperados na tela.
- O administrador visualiza a lista de funcionários recuperados e finaliza o processo.

## [5.2](#header-19) Cadastrar Funcionário
- O administrador irá para a tela de cadastro de setores.
- O administrador preencherá os campos do novo setor.
- Se o administrador clicou em cancelar, o sistema redirecionará para a tela de menu de setores e interrompe o processo.
- Se o administrador clicou em confirmar, o sistema validara os campos que ele inseriu.
- O sistema valida os campos pelo administrador.
- Se os campos forem inválidos, o administrador terá que preencher os campos do novo setor, como no item 1.2.
- Se os campos forem validos, o sistema verificara se o novo funcionário já começará com lotação em algum setor.
- O sistema verificara se o novo funcionário já começará com lotação em algum setor.
- Se a lotação do setor for definida, o sistema cadastrara uma nova lotação do funcionário no setor e logo em seguida, salvara as alterações do funcionário no banco.
- Se a lotação não for definida, o sistema salvara as alterações do funcionário no banco.
- O sistema redirecionara para a tela de menu de setores e finaliza o processo.

## [5.3](#header-20) Editar Funcionário
- O administrador irá para tela de edição de funcionários.
- Se o administrador não acessar a tela pela URL, ele irá para a tela de menu de funcionários e logo em seguida selecionara os itens da lista.
- Se o administrador clicar em um item da lista, o sistema definira o ID do funcionário a ser editar como o ID do item clicado na lista e logo em seguida, redirecionara para a tela de edição de funcionário enviando o ID como parâmetro.
- Se o administrador clicar no botão editar, o sistema definira o ID do funcionário a ser editado como ID do primeiro item selecionado na lista e logo em seguida, redirecionara para a tela de edição de funcionário enviando o ID como parâmetro.
- Se o administrador for acessar a tela pela URL ou retornar de uma página posterior, o sistema verificará se o ID recebido como parâmetro corresponde a um funcionário válido.
- O sistema verificará se o ID recebido como parâmetro corresponde a um funcionário válido.
- Se o ID não for válido, o sistema redireciona para a tela de menu de funcionário, interrompendo o processo.
- Se o ID for válido, o sistema recupera os dados do funcionário de ID equivalente ao valor recebido como parâmetro e logo em seguida, ele vai popular os campos de edição de dados da tela com os dados atuais funcionário. Depois, administrador altera os valores dos campos do funcionário conforme desejado.
- O administrador altera os valores dos campos do funcionário conforme desejado.
- Se o administrador clicou em cancelar as alterações, o sistema redireciona para a tela de menu de funcionário, interrompendo o processo.
- Se o administrador clicou em confirmar as alterações, o sistema valida os valores dos campos do formulário.
- O sistema valida os valores dos campos do formulário.
- Se os valores dos campos forem inválidos, o sistema recupera os dados do funcionário de ID equivalente ao valor recebido como parâmetro.
- Se os valores dos campos forem válidos, o sistema verifica se a lotação do funcionário foi alterada.
- O sistema verifica se a lotação do funcionário foi alterada.
- Se a lotação do funcionário foi alterada, o sistema cadastra uma nova lotação do funcionário no novo setor e salva suas alterações do usuário no banco.
- Se a lotação do funcionário foi alterada, o sistema salva suas alterações do usuário no banco.
- O sistema salva suas alterações do usuário no banco e finaliza o processo.

##[5.4](#header-21) Desativar Funcionário
- O administrador vai acessar a tela de desativação de funcionários.
- Se o administrador não for acessar pela URL, ele vai para a tela de menu de funcionários, seleciona os itens da lista e clica em desativar.
- O sistema define a lista de IDs dos funcionários a serem desativados como os IDs dos itens selecionados.
- O sistema redireciona para a tela de desativação de funcionário enviando a lista de IDs como parâmetro.
- O sistema recupera os dados dos funcionários que correspondem com os IDs recebidos como parâmetro no banco.
- O sistema mostra um resumo dos dados dos funcionários a serem desativados na tela.
- Se o administrador for acessar pela URL e não reenviar dados pelo formulário, o sistema redireciona para a tela de menu de funcionários, interrompendo o processo.
- O sistema mostra um resumo dos dados dos funcionários a serem desativados na tela.
- Se o administrador clicou em cancelar, o sistema redireciona para a tela de menu de funcionários, interrompendo o processo.
- Se o administrador clicou em confirmar, o sistema desativa os funcionários no banco.
- O sistema desativa os funcionários no banco.
- O sistema redireciona para a tela de menu de funcionários e finaliza o processo.

* * *

# [6.](#header-22) DIAGRAMAS DE ATIVIDADES – CASOS DE USO DO ADMINISTRADOR - SETORES
## [6.1](#header-23) Listar Setores
- O administrador vai para a tela de menu de setores.
- O sistema requisita todos os setores do banco.
- O sistema mostra a lista de setores recuperados na tela.
- O administrador ver a lista de setores recuperados e finaliza o processo.
## [6.2](#header-24) Cadastrar Setor
- O administrador vai para a tela de cadastro de setores preencher os campos do novo setor.
- Se o administrador clicou em cancelar, o sistema redireciona para a tela de menu de setores, interrompendo o processo.
- Se o administrador clicou em confirmar, o sistema valida os campos inseridos pelo setor.
- O sistema valida os campos inseridos pelo setor.
- Se os campos forem inválidos, o administrador terá de preencher os campos do novo setor.
- Se os campos forem válidos, o sistema cadastra o novo setor no banco.
- O sistema cadastra o novo setor no banco.
- O sistema redireciona para a tela de menu de setor e finaliza o processo.
## [6.3](#header-25) Editar Setor
- O administrador irá para tela de edição de setores.
 Se o administrador não acessar a tela pela URL, ele irá para a tela de menu de setores e logo em seguida selecionara os itens da lista.
- Se o administrador clicar em um item da lista, o sistema definira o ID do setor a ser editar como o ID do item clicado na lista e logo em seguida, redirecionara para a tela de edição de setor enviando o ID como parâmetro.
- Se o administrador clicar no botão editar, o sistema definira o ID do setor a ser editado como ID do primeiro item selecionado na lista e logo em seguida, redirecionara para a tela de edição de setor enviando o ID como parâmetro.
- Se o administrador for acessar a tela pela URL ou retornar de uma página posterior, o sistema verificará se o ID recebido como parâmetro corresponde a um setor válido.
- O sistema verificará se o ID recebido como parâmetro corresponde a um setor válido.
- Se o ID não for válido, o sistema redireciona para a tela de menu de setor, interrompendo o processo.
- Se o ID for válido, o sistema recupera os dados do setor de ID equivalente ao valor recebido como parâmetro e logo em seguida, ele vai popular os campos de edição de dados da tela com os dados atuais do setor. Depois, o administrador altera os valores dos campos do setor conforme desejado.
- O administrador altera os valores dos campos do setor conforme desejado.
- Se o administrador clicou em cancelar as alterações, o sistema redireciona para a tela de menu de setor, interrompendo o processo.
- Se o administrador clicou em confirmar as alterações, o sistema valida os valores dos campos do formulário.
- O sistema valida os valores dos campos do formulário.
- Se os valores dos campos forem inválidos, o sistema recupera os dados do setor de ID equivalente ao valor recebido como parâmetro.
- Se os valores dos campos forem válidos, o sistema verifica se a lotação do setor foi alterada.
- O sistema salva suas alterações do setor no banco e finaliza o processo.
## [6.4](#header-26) Desativar Setor
- O administrador vai acessar a tela de desativação de setor.
- Se o administrador não for acessar pela URL, ele vai para a tela de menu de setores, seleciona os itens da lista e clica em desativar.
- O sistema define a lista de IDs dos setores a serem desativados como os IDs dos itens selecionados.
- O sistema redireciona para a tela de desativação de setores enviando a lista de IDs como parâmetro.
- O sistema recupera os dados dos setores que correspondem com os IDs recebidos como parâmetro no banco.
- O sistema mostra um resumo dos dados dos setores a serem desativados na tela.
- Se o administrador for acessar pela URL e não reenviar dados pelo formulário, o sistema redireciona para a tela de menu de setores, interrompendo o processo.
- O sistema mostra um resumo dos dados dos setores a serem desativados na tela.
- Se o administrador clicou em cancelar, o sistema redireciona para a tela de menu de setores, interrompendo o processo.
- Se o administrador clicou em confirmar, o sistema desativa os setores no banco.
- O sistema desativa os setores no banco.
- O sistema redireciona para a tela de menu de setores e finaliza o processo.
