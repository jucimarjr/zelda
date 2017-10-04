var casos = {
    "uc000": {
        id: "UC000", nome: "Logout do administrador", descricao: "O sistema deve encerrar a sessão do administrador", 
        ator: "Administrador.", prioridade: "Desenvolvido como uma função da tela pós-login do administrador.", rnfs: "RNF007.",
        precondicoes: ["O ator precisa estar autenticado como administrador."], 
        poscondicoes: ["O sistema deve encerrar a sessão do administrador"], 
        fluxo: "administrador-logout-fluxo-principal.png"
    },
    "uc001": {
        id: "UC001", nome: "Login do administrador", descricao: "O sistema deve permitir ao usuario que entre no sistema por meio do seu login unico e senha determinado",
        ator: "Administrador.", prioridade: "Primeira tela a ser desenvolvida.", rnfs: "RNF007",
        precondicoes: [ /*"Ator não está com sessão ativa no sistema", "Ator deve estar cadastrado no sistema", "Ator deve estar na página de Login"*/
            "O ator precisa saber e entrar com os dados de login (usuário e senha)."],
        poscondicoes: [/* "Ator estará com sessão ativa no sistema", "Ator poderá visualizar suas informações"*/
            "O sistema deve oferecer uma tela para acessar funcionalidades de gerência."],
        fluxo: /*"assets/img/ad-login.jpg"*/ "administrador-login-fluxo-principal.png"
    },
    "uc002": {
        id: "UC002", nome: "Visualizar dados do Admin", descricao: "", 
        ator: "", prioridade: "", rnfs: "",
        precondicoes: ["O ator precisa estar autenticado como administrador."], 
        poscondicoes: ["Os dados do Administrador devem ser exibidos."], 
        fluxo: "ad-visualizar-dados-usuario.jpg"
    },
    "uc003": { /**/
        id: "UC003", nome: "Listar Funcionários", descricao: "Permite ao administrador visualizar os funcionários cadastrados.",
        ator: "Administrador.", prioridade: "Precisa ser feito antes dos casos de uso de remover e editar funcionário", rnfs: "nenhum",
        precondicoes: ["O ator precisa estar autenticado como administrador."], 
        poscondicoes: ["Poderá cadastrar novos, editar ou remover funcionários."], 
        fluxo: "ad-listar-funcionarios.jpg"
    },
    "uc004": { /**/
        id: "UC004", nome: "Cadastrar Funcionários", descricao: "Permite ao administrador cadastrar novos funcionários.", 
        ator: "Administrador.", prioridade: "nenhuma.", rnfs: "nenhum.",
        precondicoes: ["O ator precisa estar autenticado como administrador.", "O ator precisa estar na página de listagem de funcionários."], 
        poscondicoes: ["Não podem haver dois funcionários com o mesmo nome;", "Não podem haver funcionários com campos inválidos."], 
        fluxo: "ad-cadastrar-funcionario.jpg"
    },
    "uc005": { /**/
        id: "UC005",
        nome: "Editar Funcionário",
        descricao: "O caso de uso inicia-se quando o administrador desejar mudar algum dado de um determinado funcionário",
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar com sessão ativa no sistema;", "O ator precisa estar na página de listagem de funcionários ou conhece o id do funcionário a ser editado."],
        poscondicoes: ["Os dados alterados dos funcionários editados serão atualizados no banco do sistema e na lista de funcionários."],
        fluxo: "ad-editar-funcionario.jpg"
    },
    "uc006": { /**/
        id: "UC006", nome: "Desativar Funcionários", descricao: "O caso de uso inicia-se quando o administrador desejar remover um determinado funcionário do sistema",
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar com sessão ativa no sistema;", "O ator precisa estar na página de listagem de funcionários."],
        poscondicoes: ["A situação de cada funcionário desativado será alterada no banco do sistema."],
        fluxo: "ad-desativar-funcionarios.jpg"
    },
    "uc007": {
        id: "UC007",
        nome: "Listar Setores",
        descricao: "Caso de uso que representa a listagem de todos os setores já cadastrados na base de dados do sistema.",
        ator: "AT001", prioridade: "", rnfs: "",
        precondicoes: ["Ator está logado no sistema como administrador."],
        poscondicoes: ["Poderá editar os setores, desativar setores e cadastrar novos setores."],
        fluxo: "assets/img/ad-listar-setores.jpg"
    },
    "uc008": {
        id: "UC008", nome: "Cadastrar Setor", descricao: "Permite ao administrador cadastrar um novo setor no sistema.", 
        ator: "", prioridade: "", rnfs: "",
        precondicoes: ["O ator precisa estar autenticado como administrador;", "O ator precisa estar na página de listagem de Setores."], 
        poscondicoes: ["Não podem haver dois setores com o mesmo nome;", "Não podem haver setores com campos inválidos."], 
        fluxo: "ad-cadastrar-setor.jpg"
    },
    "uc009": {
        id: "UC009", nome: "Editar Setor", descricao: "Caso de uso que representa a funcionalidade de editar os campos de um setor já existente na base de dados do sistema.",
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator está logado no sistema como administrador;", "O ator conhece o id do setor ou está na tela de listagem de setores."],
        poscondicoes: ["Não podem haver setores com o mesmo nome;", "Os dados editados serão atualizados na base de dados do sistema e na lista de setores."],
        fluxo: "ad-editar-setor.jpg"
    },
    "uc010": {
        id: "UC010", nome: "Desativar Setor", descricao: "Consiste em que o administrador tem o a autorização em desativar algum setor do sistema.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator precisa estar autenticado como administrador;", "O ator precisa estar na página de listagem de Setores."], 
        poscondicoes: ["Não podem haver funcionários nos setores desativados;", "A situação de cada Setor deve ser alterada no banco do sistema."], 
        fluxo: "ad-desativar-setores.jpg"
    },
    "uc011": {
        id: "UC011", nome: "Listar Usuários", descricao: "O administrador pode visualizar a lista dos usuários com seus campos de id, login, senha e tipo. Também, pode selecionar as funcionalidades de adicionar, editar e remover usuário.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["Estar logado como administrador."], 
        poscondicoes: ["Os usuários do sistema foram visualizados."], 
        fluxo: "ad-listar-usuarios.jpg"
    },
    "uc012": {
        id: "UC012", nome: "Cadastrar Usuário", descricao: "O administrador pode inserir dados do usuário como login, senha e se ele é administrador ou não para fazer o cadastro do usuário.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["Estar logado como administrador;", "Possuir os dados do usuário (login e senha)."], 
        poscondicoes: ["Não podem haver usuários com o mesmo login;", "O usuário deve estar cadastrado no sistema."], 
        fluxo: "ad-cadastrar-usuario.jpg"
    },
    "uc013": {
        id: "UC013", nome: "Editar Usuário", descricao: "O administrador pode editar dados do usuário como login, senha e tipo do usuário (administrador ou usuário comum).", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["Estar logado como administrador, possuir os dados do usuário a serem alterados (login, senha, tipo)."], 
        poscondicoes: ["Não podem haver usuários com o mesmo login;", "Os dados do usuário foram alterados."], 
        fluxo: "ad-editar-usuario.jpg"
    },
    "uc014": {
        id: "UC014", nome: "Remover Usuário", descricao: "O administrador pode remover um usuário retirando seus dados do sistema.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["Estar logado como administrador;", "O ator precisa estar na listagem de Usuários."], 
        poscondicoes: ["Os usuários deletados devem ser removidos do banco de dados."], 
        fluxo: "ad-desativar-usuarios.jpg"
    },
    "uc015": {
        id: "UC015", nome: "Login do Usuário", descricao: "Autenticação do usuário no sistema", 
        ator: "Usuário Comum", prioridade: "Primeira página desenvolvida.", rnfs: "",
        precondicoes: ["Deve haver ao menos um usuário cadastrado no banco de dados;", "O ator deve estar na página Inicial de Login."],
        poscondicoes: ["O ator pode visualizar suas informações"], 
        fluxo: "ad-login.jpg"
    },
    "uc016": {
        id: "UC016", nome: "Logout do Usuário", descricao: "Encerra a sessão do usuário no sistema",
        ator: "Usuário Comum", prioridade: "Desenvolvido como uma função da tela pós-login do usuário.", rnfs: "",
        precondicoes: [ /* "Ator deve estar com sessão ativa no sistema" */ "O ator deve estar com o login ativo no sistema Zelda."],
        poscondicoes: [ /* "Ator não está mais com sessão ativa no sistema"*/ "Após apertar o botão de logout o ator é direcionado para a página inicial de Login."],
        fluxo: "ad-logout.jpg"
    },
    "uc017": {
        id: "UC017", nome: "Visualizar dados do Usuário", descricao: "Tela carregada pós-login do usuário comum.", 
        ator: "Usuário Comum", prioridade: "", rnfs: "",
        precondicoes: ["O ator precisa estar autenticado como Usuário do sistema."], 
        poscondicoes: ["Os dados do usuário devem ser exibidos."], 
        fluxo: "ad-visualizar-dados-usuario.jpg"
    }
};
