var casos = {
    "uc000": {
        id: "UC000", nome: "Logout do Administrador", descricao: "O sistema deve encerrar a sessão do ator no sistema", 
        ator: "Administrador.", prioridade: "Desenvolvido como uma função da tela pós-login do administrador.", rnfs: "RNF007.",
        precondicoes: ["O ator estar logado no sistema."], 
        poscondicoes: ["O sistema deve encerrar a sessão do ator;", "O ator deve estar na tela de login."], 
        fluxo: "administrador-logout-fluxo-principal.png"
    },
    "uc001": {
        id: "UC001", nome: "Login do Administrador", descricao: "O sistema deve permitir ao ator entrar no sistema.",
        ator: "Administrador.", prioridade: "Primeira tela a ser desenvolvida.", rnfs: "RNF007",
        precondicoes: ["O ator não estar com sessão ativa no sistema;", "O ator estar cadastrado no sistema;", "O ator estar na página de Login"],
        poscondicoes: ["O ator deve estar com sessão ativa no sistema;", "O ator deve poder visualizar suas informações;",
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
        id: "UC003", nome: "Listar Funcionários", descricao: "O sistema deve permitir ao ator visualizar a tela listar funcionários e acessar as opções cadastar, editar e desativar um funcionário.",
        ator: "Administrador.", prioridade: "Precisa ser feito antes dos casos de uso de remover e editar funcionário", rnfs: "nenhum",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela de visualizar dados do ator."], 
        poscondicoes: ["O ator deve poder visualizar a lista de funcionários, acessar as opções cadastrar, editar ou desativar um funcionário."], 
        fluxo: "ad-listar-funcionarios.jpg"
    },
    "uc004": { /**/
        id: "UC004", nome: "Cadastrar Funcionários", descricao: "O ator deve poder cadastrar um funcionário no sistema.", 
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
        id: "UC006", nome: "Desativar Funcionários", descricao: "O ator deve poder desativar um funcionário no sistema.",
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
        id: "UC008", nome: "Cadastrar Setor", descricao: "O ator deve poder cadastrar um setor no sistema.", 
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
        id: "UC010", nome: "Desativar Setor", descricao: "O ator deve poder desativar um setor no sistema.", 
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
        id: "UC012", nome: "Cadastrar Usuário", descricao: "O ator deve poder cadastrar um usuário no sistema.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar usuários."], 
        poscondicoes: ["O usuário deve estar cadastrado no sistema."], 
        fluxo: "ad-cadastrar-usuario.jpg"
    },
    "uc013": {
        id: "UC013", nome: "Editar Usuário", descricao: "O ator deve poder editar dados de um usuário.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar usuários."], 
        poscondicoes: ["Os dados do usuário devem estar editados no sistema."], 
        fluxo: "ad-editar-usuario.jpg"
    },
    "uc014": {
        id: "UC014", nome: "Remover Usuário", descricao: "O ator deve poder remover um usuário do sistema.", 
        ator: "Administrador.", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema;", "O ator estar na tela listar usuários."], 
        poscondicoes: ["O usuário deve estar removido do sistema."], 
        fluxo: "ad-desativar-usuarios.jpg"
    },
    "uc015": {
        id: "UC015", nome: "Login do Usuário", descricao: "O sistema deve permitir ao ator entrar no sistema.", 
        ator: "Usuário Comum", prioridade: "Primeira página desenvolvida.", rnfs: "",
        precondicoes: ["O ator não estar com sessão ativa no sistema;", "O ator estar cadastrado no sistema;", "O ator estar na página de Login"],
        poscondicoes: ["O ator deve estar com sessão ativa no sistema;", "O ator deve poder visualizar suas informações."], 
        fluxo: "ad-login.jpg"
    },
    "uc016": {
        id: "UC016", nome: "Logout do Usuário", descricao: "O sistema deve encerrar a sessão do ator no sistema",
        ator: "Usuário Comum", prioridade: "Desenvolvido como uma função da tela pós-login do usuário.", rnfs: "",
        precondicoes: [ "O ator estar logado no sistema."],
        poscondicoes: [ "O sistema deve encerrar a sessão do ator;", "O ator deve estar na tela de login."],
        fluxo: "ad-logout.jpg"
    },
    "uc017": {
        id: "UC017", nome: "Visualizar dados do Usuário", descricao: "O sistema deve permitir ao ator visualizar os seus dados", 
        ator: "Usuário Comum", prioridade: "", rnfs: "",
        precondicoes: ["O ator estar logado no sistema."], 
        poscondicoes: ["O ator deve poder visualizar seus dados."], 
        fluxo: "ad-visualizar-dados-usuario.jpg"
    }
};
