$(document).on('click', '#Projetos', Projetos); //.load projeto no corpo do home
$(document).on('click', '#editarProjeto', editarProjeto); //Btn editar Projeto
$(document).on('click', '#infoProjeto', infoProjeto); //mostrar todos as informações do projeto no Modal
$(document).on('click', '#NovoProjeto', NovoProjeto); //abrir cadastro de novo projeto
$(document).on('click', '#SalvarNovoProjeto', SalvarNovoProjeto); //.btn salvar projeto novo
$(document).on('click', '#SalvarEditProjeto', SalvarEditProjeto);
$(document).on('click', '#SelecionarProjeto', SelecionarProjeto); //Excluir Usuario
$(document).on('click', '.ExcluirProjeto', ExcluirProjeto); //Excluir Projeto
$(document).on('click', '#modalTarefas', modalTarefas); //Abrir modal Tarefas em Projetos
$(document).on('click', '.BotaoAddTarefa', BotaoAddTarefa); //Botao para adicionar Tarefa no Projeto
$(document).on('click', '.descricaoModulo', descricaoModulo); //Botao para abrir descricao Modulo Proejto
$(document).on('click', '.descricaoTarefa', descricaoTarefa); //Botao para abrir descricao tarefaProjeto
$(document).on('click', '.concluirTarefa', concluirTarefa);//Botao para concluir  tarefa
$(document).on('click', '.estornarTarefa', estornarTarefa);//Botao para estornar  tarefa
$(document).on('click', '.removerTarefa', removerTarefa);//Botao para remover tarefa do Projeto

$(document).on('click', '#Usuario', Usuario); //.load usuarios no corpo do Home
$(document).on('click', '#NovoUsuario', NovoUsuario); //.load novoUsuario no corpo do Home
$(document).on('click', '#InfoUsuario', InfoUsuario); //mostrar todos as informações do projeto no Modal
$(document).on('click', '#SalvarNovoUsuario', SalvarNovoUsuario); //.btn salvar Usuario novo
$(document).on('click', '#EditarUsuario', EditarUsuario); //.btn salvar Usuario novo
$(document).on('click', '#SalvarEditarUsuario', SalvarEditarUsuario); //.btn salvar Usuario novo
$(document).on('click', '#ExcluirUsuario', ExcluirUsuario); //Excluir Usuario
$(document).on('click', '.ResetSenhaUsuario', ResetSenhaUsuario); //Excluir Usuario
$(document).on('click', '#SalvarNovaSenha', SalvarNovaSenha); //Excluir Usuario
$(document).on('click', '#NovoLog', NovoLog); //Excluir Usuario
$(document).on('click', '#salvarLog', salvarLog); //Excluir Usuario
$(document).on('click', '#projetoLogoff', projetoLogoff); //Logoff do Sistema
$(document).on('click', '#Modulo', Modulo); //Botao para abrir Gerenciamento dos Modulos
$(document).on('click', '#ModalNovoModulo', ModalNovoModulo); //Botao para abrir modal e cadastrar novo modulo
$(document).on('click', '#SalvarNovoModulo', SalvarNovoModulo); //salvar novo modulo
$(document).on('click', '.info_modulo', info_modulo);//Botao para apresentar informacoes do modulo
$(document).on('click', '.editar_modulo', editar_modulo);//Botao para apresentar informacoes do modulo
$(document).on('click', '.excluir_modulo', excluir_modulo); //Botao para remover o modulo
$(document).on('click', '.salvarEditModulo', salvarEditModulo);//Botao para salvar Editação de Modulo
$(document).on('click', '.nova_tarefa', nova_tarefa);//Botao para salvar nova tarefa
$(document).on('click', '.salvar_novaTarefa', salvar_novaTarefa);
$(document).on('click', '.info_tarefa', info_tarefa);//Botao para apresentar informacoes do tarefa
$(document).on('click', '.editar_tarefa', editar_tarefa);//Botao para apresentar informacoes do tarefa
$(document).on('click', '.salvarEditTarefa', salvarEditTarefa);//Botao para salvar Tarefa editado
$(document).on('click', '.excluir_tarefa', excluir_tarefa);//Botao para apresentar informacoes do tarefa





function Projetos(){
	$("#CorpoHome").load("./Exibir/Projetos.php");
	$("#projeto_btn1").html('<a id="Usuario">Usuarios</a>'); //botão no header
    $("#projeto_btn2").html('<a id="Modulo">Modulos</a>'); //botão no header
};

function zerarInfoProjeto(){
	$("#infoId").html('');
	$("#infoNomeProjeto").html('');
	$("#infoCnpj").html('');
	$("#infoIe").html('');
	$("#infoRazaoSocial").html('');
	$("#infoNomeFantasia").html('');
	$("#infoLogradouro").html('');
	$("#infoBairro").html('');
	$("#infoNumero").html('');
	$("#infoCep").html('');
	$("#infoMunicipio").html('');
	$("#infoEstado").html('');
	$("#infoTelefone").html('');
	$("#infoEmail").html('');
	$("#infoCliResponsavel").html('');
	$("#infoTelResponsavel").html('');
	$("#infoDiaInicio").html('');
	$("#infoDiaFim").html('');
	$("#infoDiaCobranca").html('');
	$("#infoFormaPagamento").html('');
	$("#infoValorContrato").html('');
}

function zerarEditarProjeto(){
	$("#edit_nomeProjeto").val('');
	$("#edit_razaoSocial").val('');
	$("#edit_nomeFantasia").val('');
	$("#edit_cnpj").val('');
	$("#edit_ie").val('');
	$("#edit_logradouro").val('');
	$("#edit_bairro").val('');
	$("#edit_numero").val('');
	$("#edit_cep").val('');
	$("#edit_municipio").val('');
	$("#edit_estado").val('');
	$("#edit_telefone").val('');
	$("#edit_email").val('');
	$("#edit_cliResp").val('');
	$("#edit_telResp").val('');
	$("#edit_diaIni").val('');
	$("#edit_diaFim").val('');
	$("#edit_diaCobranca").val('');
	$("#edit_FormPag").val('');
	$("#edit_ValContra").val('');
}


function editarProjeto(){
	zerarEditarProjeto()


	var idProjeto = Array("infoProjeto", $("#infoId").html());

	$.ajax({
		url: "../Controle/Projetos.php",
		data: JSON.stringify(idProjeto),
		type: "POST",
		dataType: "json",
		success: function(resultado){
			$("#edit_Id").html(resultado['id']);
			$("#edit_nomeProjeto").val(resultado['nome_projeto']);
			$("#edit_cnpj").val(resultado['cnpj']);
			$("#edit_ie").val(resultado['ie']);
			$("#edit_razaoSocial").val(resultado['razao_social']);
			$("#edit_nomeFantasia").val(resultado['nome_fantasia']);
			$("#edit_logradouro").val(resultado['logradouro']);
			$("#edit_bairro").val(resultado['bairro']);
			$("#edit_numero").val(resultado['numero']);
			$("#edit_cep").val(resultado['cep']);
			$("#edit_municipio").val(resultado['municipio']);
			$("#edit_estado").val(resultado['estado']);
			$("#edit_telefone").val(resultado['telefone']);
			$("#edit_email").val(resultado['email']);
			$("#edit_cliResp").val(resultado['cliente_responsavel']);
			$("#edit_telResp").val(resultado['tel_responsavel']);
			$("#edit_diaInic").val(resultado['dia_inicio']);
			$("#edit_diaFim").val(resultado['dia_fim']);
			$("#edit_diaCobranca").val(resultado['dia_cobranca']);
			$("#edit_FormPag").val(resultado['forma_pagamento']);
			$("#edit_ValContra").val(resultado['valor_contrato']);
			$("#modalInfoProjeto").modal("hide");
			$("#modalEditarProjeto").modal("show");

		}

		});

}

function infoProjeto(){
	zerarInfoProjeto();
	var idProjeto = Array("infoProjeto", $(this).closest('tr').find('#identificacao').html());

	$.ajax({
		url: "../Controle/Projetos.php",
		data: JSON.stringify(idProjeto),
		type: "POST",
		dataType: "json",
		success: function(resultado){
			$("#infoId").html(resultado['id']);
			$("#infoNomeProjeto").html(resultado['nome_projeto']);
			$("#infoCnpj").html(resultado['cnpj']);
			$("#infoIe").html(resultado['ie']);
			$("#infoRazaoSocial").html(resultado['razao_social']);
			$("#infoNomeFantasia").html(resultado['nome_fantasia']);
			$("#infoLogradouro").html(resultado['logradouro']);
			$("#infoBairro").html(resultado['bairro']);
			$("#infoNumero").html(resultado['numero']);
			$("#infoCep").html(resultado['cep']);
			$("#infoMunicipio").html(resultado['municipio']);
			$("#infoEstado").html(resultado['estado']);
			$("#infoTelefone").html(resultado['telefone']);
			$("#infoEmail").html(resultado['email']);
			$("#infoCliResponsavel").html(resultado['cliente_responsavel']);
			$("#infoTelResponsavel").html(resultado['tel_responsavel']);
			$("#infoDiaInicio").html(resultado['dia_inicio']);
			$("#infoDiaFim").html(resultado['dia_fim']);
			$("#infoDiaCobranca").html(resultado['dia_cobranca']);
			$("#infoFormaPagamento").html(resultado['forma_pagamento']);
			$("#infoValorContrato").html(resultado['valor_contrato']);
			$("#modalInfoProjeto").modal("show");

		}

		});

}

function NovoProjeto(){
	$("#modalNovoProjeto").modal('show');
}

function SalvarNovoProjeto(){ //.btn salvar projeto novo
	var informacoes = $('#novoProjeto').serializeArray(); //informações do novo projeto
	informacoes.unshift('salvarNovoProjeto');

	$.ajax({
		url: '../Controle/Projetos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(retorno){
			alert(retorno);
			$("#modalNovoProjeto").modal('hide');
			Projetos();


		}//success
	})
};

function SalvarEditProjeto(){
	var informacoes = $('#EditarProjeto').serializeArray(); //informações do novo projeto
	informacoes.unshift($("#edit_Id").html());
	informacoes.unshift('salvarEditarProjeto');

	$.ajax({
		url: '../Controle/Projetos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(retorno){
			alert(retorno);
			$("#modalEditarProjeto").modal("hide");
			Projetos();


		}//success
	})
}

function SelecionarProjeto(){
	var idProjeto = $(this).closest('tr').find('#identificacao').html();
	$("#CorpoHome").load("./Exibir/ExibirProjeto.php", {"idProjeto": idProjeto} );
	$("#projeto_btn1").html('<a id="Projetos">Voltar a Projetos</a>'); //botão no header
    $("#projeto_btn2").html('<a id="Usuario">Usuarios</a>'); //botão no header
}

function ExcluirProjeto(){
	var conf = confirm("Você realmente deseja excluir este Projeto???");

	if (conf == true) {
		var informacoes = Array('excluirProjeto', $(this).closest('tr').find('#identificacao').html())

		$.ajax({
			url: '../Controle/Projetos.php',
			data: JSON.stringify(informacoes),
			dataType: 'JSON',
			type: 'POST',
			success: function(resposta){
				alert(resposta);
				Projetos();
			}
		})
	}


}

function modalTarefas(){
	$("#modalAddTarefa").modal('show');
}



function BotaoAddTarefa(){
	var botao = $(this);
	var informacoes = Array('adicionarTarefa', $("#idProjetoCurrent").html(), $(this).closest("p").attr("data-modulo"), $(this).closest("p").attr("data-id"));

	$.ajax({
		url:'../Controle/Projetos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(msg){
			if (msg == 0) {
				botao.addClass("disabled");
				botao.html("Já Adicionado");
				$("#CorpoTarefas").html('');
				$("#CorpoTarefas").load("./Exibir/ExibirProjeto.php #CorpoTarefas" , {"idProjeto": informacoes[1]} );
			}
			}
	})

	
}

function descricaoModulo(){
	$(".corpoModalDesc").html('');
	$(".corpoModalDesc").html($(this).closest("p").attr("modulo-descricao"));
	$("#modalDescricao").modal("show");
	
}

function descricaoTarefa(){
	$(".corpoModalDesc").html('');
	$(".corpoModalDesc").html($(this).closest("p").attr("tarefa-descricao"));
	$("#modalDescricao").modal("show");
	
}

function concluirTarefa(){
	var botao = $(this).closest("span");
	var informacoes = Array("concluirTarefa", $(this).closest("p").attr("data-id"));

	$.ajax({
		url:'../Controle/Projetos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(msg){
			if (msg == 0) {
				botao.html('<button type="button" class="btn btn-danger estornarTarefa" >Estornar</button>');
			}
			}
	})
}

function estornarTarefa(){
	var botao = $(this).closest("span");
	var informacoes = Array("estornarTarefa", $(this).closest("p").attr("data-id"));

	$.ajax({
		url:'../Controle/Projetos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(msg){
			if (msg == 0) {
				botao.html('<button type="button" class="btn btn-danger concluirTarefa" >Concluir</button>');
			}
			}
	})	
}

function removerTarefa(){
	var verificacao = confirm("Deseja remover a Tarefa do Projeto???");

	if (verificacao == true) {
		var informacoes = Array("removerTarefa", $(this).closest("p").attr("data-id"));
		$.ajax({
		url:'../Controle/Projetos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(msg){
				if (msg == 0) {
					alert("Removido com sucesso");
					$("#allCorpoTarefa").html('');
					$("#allCorpoTarefa").load("./Exibir/ExibirProjeto.php #allCorpoTarefa" , {"idProjeto": $("#idProjetoCurrent").html()} );
				}
			}
		})
	}
}

function zerarInfoUsuario(){
	$("#infoId").html('');
	$("#infoNome").html('');
	$("#infoSobrenome").html('');
	$("#infoEmail").html('');
	$("#infoTelefone").html('');
	$("#infoLogradouro").html('');
	$("#infoBairro").html('');
	$("#infoNumero").html('');
	$("#infoCep").html('');
	$("#infoMunicipio").html('');
	$("#infoEstado").html('');

};

function zerarEditarUsuario(){
	$("#editar_id").html('');
	$("#editar_nome").val('');
	$("#editar_sobrenome").val('');
	$("#editar_email").val('');
	$("#editar_telefone").val('');
	$("#editar_logradouro").val('');
	$("#editar_bairro").val('');
	$("#editar_numero").val('');
	$("#editar_cep").val('');
	$("#editar_municipio").val('');
	$("#editar_estado").val('');

};

function Usuario(){
	$("#CorpoHome").load("./Exibir/Usuarios.php")
	$("#projeto_btn1").html('<a id="Projetos">Voltar a Projetos</a>'); //botão no header
    $("#projeto_btn2").html(''); //botão no header
};

function NovoUsuario(){
	$("#modalNovoUsuario").modal('show');
};

function InfoUsuario(){
	zerarInfoUsuario();
	var idUsuario = Array("infoUsuario", $(this).closest('tr').find('#identificacao').html());

	$.ajax({
		url: '../Controle/Usuarios.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(idUsuario),
		success: function(resultado){
			$("#infoId").html(resultado['id']);
			$("#infoNome").html(resultado['nome']);
			$("#infoSobrenome").html(resultado['sobrenome']);
			$("#infoEmail").html(resultado['email']);
			$("#infoTelefone").html(resultado['telefone']);
			$("#infoLogradouro").html(resultado['logradouro']);
			$("#infoBairro").html(resultado['bairro']);
			$("#infoNumero").html(resultado['numero']);
			$("#infoCep").html(resultado['cep']);
			$("#infoMunicipio").html(resultado['municipio']);
			$("#infoEstado").html(resultado['estado']);
			$("#modalInfoUsuario").modal('show');
		}
	})
}

function SalvarNovoUsuario(){
	var informacoes = $('#FormNovoUsuario').serializeArray(); //informações do novo projeto
	informacoes.unshift('SalvarNovoUsuario');

	$.ajax({
		url: '../Controle/Usuarios.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(retorno){
			alert(retorno);
			$("#modalNovoUsuario").modal('hide');
			Usuario();
		}//success
	})
}

function EditarUsuario(){
	zerarEditarUsuario()


	var idUsuario = Array("infoUsuario", $("#infoId").html());

	$.ajax({
		url: '../Controle/Usuarios.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(idUsuario),
		success: function(resultado){
			$("#editar_id").html(resultado['id']);
			$("#editar_nome").val(resultado['nome']);
			$("#editar_sobrenome").val(resultado['sobrenome']);
			$("#editar_email").val(resultado['email']);
			$("#editar_telefone").val(resultado['telefone']);
			$("#editar_logradouro").val(resultado['logradouro']);
			$("#editar_bairro").val(resultado['bairro']);
			$("#editar_numero").val(resultado['numero']);
			$("#editar_cep").val(resultado['cep']);
			$("#editar_municipio").val(resultado['municipio']);
			$("#editar_estado").val(resultado['estado']);
			$("#modalInfoUsuario").modal('hide');
			$("#modalEditarUsuario").modal('show');


		}
	})


}

function SalvarEditarUsuario(){
	var informacoes = $('#FormEditarUsuario').serializeArray(); //informações do novo projeto
	informacoes.unshift($("#editar_id").html());
	informacoes.unshift('SalvarEditarUsuario');

	$.ajax({
		url: '../Controle/Usuarios.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(retorno){
			alert(retorno);
			$("#modalEditarUsuario").modal('hide');
			Usuario();
		}//success
	})
}

function ExcluirUsuario(){
	var informacoes = Array('ExcluirUsuario', $(this).closest('tr').find('#identificacao').html());
	var conf = confirm("Você realmente deseja Excluir o Usuario "+$(this).closest('tr').find('#exibirUsuario').html()+"?");
    if (conf == true) {
    	$.ajax({
    		url: '../Controle/Usuarios.php',
    		dataType: 'json',
    		type: 'POST',
    		data: JSON.stringify(informacoes),
    		success: function(resultado){
    			alert (resultado);
    			Usuario();

    		}//.Function
    	})
    }
}

function ResetSenhaUsuario(){ // classe para reset de senha de usuario, pendencia de envio de email com senha provisoria
	$("#idUsuario").html($(this).closest('tr').find('#identificacao').html());
	$("#nomeUsuario").html($(this).closest('tr').find('#exibirUsuario').html());
	$("#modalResetSenha").modal('show');
}

function SalvarNovaSenha(){  //Alterar Senha
	var informacoes = Array('alteraSenha', $("#novaSenha").val(), $("#confirmaSenha").val(), $("#idUsuario").html());
	if (informacoes[1] !== informacoes[2] ||  informacoes[1] == '') {
		alert('Senhas não conferem ou em branco');
	}else{
		$.ajax({
			url: '../Controle/Usuarios.php',
			data: JSON.stringify(informacoes),
			dataType: 'JSON',
			type: 'POST',
			success: function(resposta){
				alert(resposta);
				$("#modalResetSenha").modal('hide');
			}
		})
	}
}

function NovoLog(){
	$("#modalNovoLog").modal('show');
}

function salvarLog(){
	var informacoes = Array('salvarLog', $("#idProjetoCurrent").html(), $("#formNovoLog").serializeArray());

	$.ajax({
		url: '../Controle/Projetos.php',
		type: 'POST',
		dataType: 'json',
		data: JSON.stringify(informacoes),
		success: function(msg){
			alert(msg);
			$("#modalNovoLog").modal('hide');
			$("#corpoLogs").load("./Exibir/ExibirProjeto.php #corpoLogs", {"idProjeto": informacoes[1]} );
		}
	})
}

function projetoLogoff(){
	var informacoes = Array('usuarioSair');
	$.ajax({
		url: '../Controle/Usuarios.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(){
			 location.reload();
		}

	})

}

function Modulo(){
	$("#projeto_btn1").html('<a id="Projetos">Voltar a Projetos</a>'); //botão no header
	$("#CorpoHome").load("./Exibir/Modulos.php");

}

function ModalNovoModulo(){
	$('#modalAddModulo').modal('show')
}

function SalvarNovoModulo(){
	var informacoes = $("#formNovoModulo").serializeArray();
	informacoes.unshift("novoModulo");

	$.ajax({
		url:'../Controle/Modulos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(msg){
			if (msg === 1) {
				alert("Já existe um Modulo com este Nome");
			}else{
				alert("Modulo Cadastrado");
				$('#modalAddModulo').modal('hide')
				Modulo();
			}
		}
	})
}

function zerarModalModulo(){
	$("#modalTituloModulo").html("");
	$("modalTituloNome").html("");
	$("#modalCampoNome").html("");
	$("#modalTituloDescricao").html("");
	$("#modalCampoDescricao").html("");
	$("#modalBtn1").html("");
	$("#modalBtn2").html("");
	$("#modalBtn3").html("");

}

var modulo_selecionado;

function info_modulo(){
	zerarModalModulo();
	modulo_selecionado = $(this).closest('#modul');
	var info_modulo = $(this).closest('summary').attr('data-descricao');
	var nome_modulo = $(this).closest('summary').attr('data-nome');
	$("#modalTituloModulo").html("Informações do Modulo");
	$("#modalTituloNome").html("Nome Modulo: ");
	$("#modalCampoNome").html(nome_modulo);
	$("#modalTituloDescricao").html("Descrição Modulo: ");
	$("#modalCampoDescricao").html("<span'>"+info_modulo+"</span>");
	$("#modalBtn1").html('<button type="button" class="btn btn-secondary editar_modulo">Editar</button>');
	$("#modalBtn2").html('<button type="button" class="btn btn-secondary excluir_modulo">Excluir</button>');
	$("#modalBtn3").html('<button type="button" class="btn btn-secondary" data-dismiss="modal">Fechar</button>');
	$("#modalmodulo").modal('show');
}
	
function editar_modulo(){
	var info_modulo = modulo_selecionado.find('summary').attr('data-descricao');
	var nome_modulo = modulo_selecionado.find('summary').attr('data-nome');
	$("#modalBtn1").html('<button type="button" class="btn btn-secondary salvarEditModulo">Salvar</button>');
	$("#modalCampoNome").html("");
	$("#modalCampoNome").html("<input type='text' id='inputnome_modulo'  name='nome_modulo'/>");
	$("#inputnome_modulo").val(nome_modulo);
	$("#modalCampoDescricao").html("");
	$("#modalCampoDescricao").html('<textarea name="descricao_modulo" style="width:99%" rows="5">'+info_modulo+'</textarea>');
}

function excluir_modulo(){
	var conf = confirm("Você realmente deseja excluir este Modulo???");

	if (conf == true) {
		var informacoes = Array('excluirModulo', modulo_selecionado.find('summary').attr('data-id'));
		$.ajax({
			url:'../Controle/Modulos.php',
			dataType: 'json',
			type: 'POST',
			data: JSON.stringify(informacoes),
			success: function(msg){
				alert(msg);
				$("#modalmodulo").modal('hide');
				modulo_selecionado.remove();
				}
			
		})
	}
}

function salvarEditModulo(){
	var informacoes = $("#formModulo").serializeArray();
	informacoes.unshift("salvarEditModulo", modulo_selecionado.find('summary').attr('data-id'));
	$.ajax({
		url:'../Controle/Modulos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(msg){
			alert(msg);
			$("#modalmodulo").modal('hide');
			Modulo();
			}
		
	})
}

function nova_tarefa(){
	modulo_selecionado = $(this).closest('#modul');
	zerarModalModulo();
	$("#modalTituloModulo").html("Nova Tarefa");
	$("#modalTituloNome").html("Nome Tarefa: ");
	$("#modalCampoNome").html("<input type='text' id='inputnome_modulo'  name='nome_modulo'/>");
	$("#modalTituloDescricao").html("Descrição Tarefa: ");
	$("#modalCampoDescricao").html('<textarea name="descricao_modulo" style="width:99%" rows="5"></textarea>');
	$("#modalBtn1").html('<button type="button" class="btn btn-secondary salvar_novaTarefa">Salvar</button>');
	$("#modalBtn2").html('<button type="button" class="btn btn-secondary" data-dismiss="modal">Fechar</button>');
	$("#modalmodulo").modal('show');
}

function salvar_novaTarefa(){
	var informacoes = $("#formModulo").serializeArray();
	informacoes.unshift('salvarNovaTarefa', modulo_selecionado.find('summary').attr('data-id'));
	$.ajax({
		url:'../Controle/Modulos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(msg){
			alert(msg);
			$("#modalmodulo").modal('hide');
			Modulo();
			}
		
	})
}

var tarefa_selecionada;

function info_tarefa(){ //funcao para alimentar o Modal (modalmodulo) e apresentar ao usuario
	zerarModalModulo();
	tarefa_selecionada = $(this).closest('p');
	var info_tarefa = tarefa_selecionada.attr('data-descricao');
	var nome_tarefa = tarefa_selecionada.attr('data-nome');
	$("#modalTituloModulo").html("Informações de Tarefa");
	$("#modalTituloNome").html("Nome Tarefa: ");
	$("#modalCampoNome").html(nome_tarefa);
	$("#modalTituloDescricao").html("Descrição Tarefa: ");
	$("#modalCampoDescricao").html("<span'>"+info_tarefa+"</span>");
	$("#modalBtn1").html('<button type="button" class="btn btn-secondary editar_tarefa">Editar</button>');
	$("#modalBtn2").html('<button type="button" class="btn btn-secondary excluir_tarefa">Excluir</button>');
	$("#modalBtn3").html('<button type="button" class="btn btn-secondary" data-dismiss="modal">Fechar</button>');
	$("#modalmodulo").modal('show');
}

function editar_tarefa(){
	var info_tarefa = tarefa_selecionada.attr('data-descricao');
	var nome_tarefa = tarefa_selecionada.attr('data-nome');
	$("#modalBtn1").html('<button type="button" class="btn btn-secondary salvarEditTarefa">Salvar</button>');
	$("#modalCampoNome").html("");
	$("#modalCampoNome").html("<input id='inputnome_tarefa' type='text' name='nome_tarefa'>");
	$("#inputnome_tarefa").val(nome_tarefa);
	$("#modalCampoDescricao").html("");
	$("#modalCampoDescricao").html('<textarea name="descricao_tarefa" style="width:99%" rows="5">'+info_tarefa+'</textarea>');
}

function salvarEditTarefa(){
	var informacoes = $("#formModulo").serializeArray();
	informacoes.unshift("salvarEditTarefa", tarefa_selecionada.attr('data-id'));
	$.ajax({
		url:'../Controle/Modulos.php',
		dataType: 'json',
		type: 'POST',
		data: JSON.stringify(informacoes),
		success: function(msg){
			alert(msg);
			$("#modalmodulo").modal('hide');
			Modulo();
			}
		
	})
}

function excluir_tarefa(){
	var conf = confirm("Você realmente deseja excluir esta Tarefa???");

	if (conf == true) {

		var informacoes = Array('excluirTarefa', tarefa_selecionada.attr('data-id'));
		$.ajax({
			url:'../Controle/Modulos.php',
			dataType: 'json',
			type: 'POST',
			data: JSON.stringify(informacoes),
			success: function(msg){
				alert(msg);
				$("#modalmodulo").modal('hide');
				tarefa_selecionada.remove();
				}
		})
	}

}

