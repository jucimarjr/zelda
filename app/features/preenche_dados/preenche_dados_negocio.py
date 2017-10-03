class PreencheDadosNegocio:
    def preenche_dados_atuais(form, func, lotacao):
        # Preenche o formulário com os dados atuais do funcionário

        if lotacao is not None:
            form.setor_id.default = int(lotacao.setor_id)
            form.lotacao_id.data = lotacao.id

        form.process()

        form.funcionario_nome.data = func.nome
        form.funcionario_id.data = func.id