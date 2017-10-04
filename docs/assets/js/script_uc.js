var casos = {
    "uc000": {
        id: "UC000", nome: "Logout do Administrador", descricao: "O sistema deve encerrar a sessão do ator", 
        ator: "Administrador.", prioridade: "Desenvolvido como uma função da tela pós-login do administrador.", rnfs: "RNF007.",
        precondicoes: ["O ator estar logado no sistema."], 
        poscondicoes: ["O sistema deve encerrar a sessão do ator."], 
        fluxo: "administrador-logout-fluxo-principal.png"
    },
    "uc001": {
        id: "UC001", nome: "Login do Administrador", descricao: "O sistema deve permitir ao ator entrar no sistema por meio do seu login unico e senha determinado",
        ator: "Administrador.", prioridade: "Primeira tela a ser desenvolvida.", rnfs: "RNF007",
        precondicoes: ["O ator não estar com sessão ativa no sistema;", "O ator estar cadastrado no sistema;", "O ator estar na página de Login"],
        poscondicoes: ["O ator deve estar com sessão ativa no sistema;", "O ator deve poder visualizar suas informações;"
            "O sistema deve oferecer uma tela para acessar funcionalidades de gerência."],
        fluxo: /*"assets/img/ad-login.jpg"*/ "administrador-login-fluxo-principal.png"
    },
    "uc002": {
        id: "UC002", nome: "Visualizar dados do Administrador", descricao: "O sistema deve permitir ao ator visualizar os seus dados e acessar as opções funcionário, setor e usuário.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema."], 
        poscondicoes: ["O ator deve poder visualizar seus dados, acessar as opções funcionário, setor e usuário ."], 
        fluxo: "ad-visualizar-dados-usuario.jpg"
    },
    "uc003": { /**/
        id: "UC003", nome: "Listar Funcionários", descricao: "O sistema deve permitir ao ator visualizar os funcionários cadastrados.",
        ator: "Administrador.", prioridade: "Precisa ser feito antes dos casos de uso de remover e editar funcionário", rnfs: "nenhum",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela de visualizar dados do ator."], 
        poscondicoes: ["O ator deve poder visualizar a lista de funcionários, acessar as opções cadastrar, editar ou desativar um funcionário."], 
        fluxo: "ad-listar-funcionarios.jpg"
    },
    "uc004": { /**/
        id: "UC004", nome: "Cadastrar Funcionários", descricao: "Permite ao administrador cadastrar novos funcionários.", 
        ator: "Administrador.", prioridade: "nenhuma.", rnfs: "nenhum.",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar funcionários."], 
        poscondicoes: ["O funcionário deve estar cadastrado no sistema."], 
        fluxo: "ad-cadastrar-funcionario.jpg"
    },
    "uc005": { /**/
        id: "UC005",
        nome: "Editar Funcionário",
        descricao: "O ator deve poder editar dados de um funcionário",
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar funcionários."],
        poscondicoes: ["Os dados do funcionário devem estar editados no sistema."],
        fluxo: "ad-editar-funcionario.jpg"
    },
    "uc006": { /**/
        id: "UC006", nome: "Desativar Funcionários", descricao: "O caso de uso inicia-se quando o administrador desejar remover um determinado funcionário do sistema",
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar funcionários."],
        poscondicoes: ["O funcionário deve estar desativado no sistema."],
        fluxo: "ad-desativar-funcionarios.jpg"
    },
    "uc007": {
        id: "UC007",
        nome: "Listar Setores",
        descricao: "O sistema deve permitir ao ator visualizar a tela listar setores e acessar as opções cadastar, editar e desativar um setor.",
        ator: "Administrador", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;","O ator estar na tela de visualizar dados do ator."],
        poscondicoes: ["O ator deve poder visualizar a lista de setores, cadastrar, editar e desativar um setor."],
        fluxo: "assets/img/ad-listar-setores.jpg"
    },
    "uc008": {
        id: "UC008", nome: "Cadastrar Setor", descricao: "Permite ao administrador cadastrar um novo setor no sistema.", 
        ator: "", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar setores."], 
        poscondicoes: ["O setor deve estar cadastrado no sistema."], 
        fluxo: "ad-cadastrar-setor.jpg"
    },
    "uc009": {
        id: "UC009", nome: "Editar Setor", descricao: "O ator deve poder editar dados de um setor.",
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar setores."],
        poscondicoes: ["Os dados do setor devem estar editados no sistema."],
        fluxo: "ad-editar-setor-principal.jpg"
    },
    "uc010": {
        id: "UC010", nome: "Desativar Setor", descricao: "Consiste em que o administrador tem o a autorização em desativar algum setor do sistema.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar setores."], 
        poscondicoes: ["O setor deve estar desativado no sistema."], 
        fluxo: "ad-desativar-setores.jpg"
    },
    "uc011": {
        id: "UC011", nome: "Listar Usuários", descricao: "O sistema deve permitir ao ator visualizar a tela listar usuários e acessar as opções cadastar, editar e remover um usuário.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela de visualizar dados do ator."], 
        poscondicoes:["O ator deve poder visualizar a lista de usuários, acessar as opções cadastrar, editar e remover usuário."], 
        fluxo: "ad-listar-usuarios.jpg"
    },
    "uc012": {
        id: "UC012", nome: "Cadastrar Usuário", descricao: "O administrador pode inserir dados do usuário como login, senha e se ele é administrador ou não para fazer o cadastro do usuário.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar usuário."], 
        poscondicoes: ["O usuário deve estar cadastrado no sistema."], 
        fluxo: "ad-cadastrar-usuario.jpg"
    },
    "uc013": {
        id: "UC013", nome: "Editar Usuário", descricao: "O ator deve poder editar dados de um usuário.", 
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
