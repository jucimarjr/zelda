from ...tables.processo.processo_interface import ProcessoInterface
from ...tables.processo.processo_modelo import Processo
from flask import render_template

class ProcessoListarNegocio:
    def exibir():
        processos_ids = ProcessoInterface.get_processos_ids()

        processos = []
        for linha in processos_ids:
            processo = Processo(linha['processo_id'])
            processos.append(processo)

        return render_template('equipe1_processo_listar.html', processos = processos)