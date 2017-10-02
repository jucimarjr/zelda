/* Pega o canvas do html */
		var canvas = document.getElementById('ucd-canvas');

		/* O contexto � usado para desenhar coisas no canvas */
		var ctx = canvas.getContext('2d');

		/* Objeto que cont�m os dados do diagrama a ser desenhado (caminho da imagem e o elemento imagem carregado) */
		var diagrama = {
			imagemCaminho: "assets/img/ucd-zelda.jpg",
			imagem: new Image()
		}

		/* Quando a imagem for carregada, a fun��o main ser� chamada */
		diagrama.imagem.onload = main;
		
		/* Define o src da imagem, o que dispara seu carregamento */
		diagrama.imagem.src = diagrama.imagemCaminho;

		/* Dicion�rio de casos de uso*/
		var casos = {

			/* Cada item da "lista" tem um id �nico para evitar casos de uso repetidos por erro humano */
			uc000: { /*Logout admin*/

				/* A posi��o do centro da elipse do caso de uso (calculado baseado na imagem inteira - que j� naturalmente tem 14px de borda) */
				x: 485,
				y: 333,

				/* Di�metro horizontal da elipse (largura) e vertical (altura) */
				largura: 140,
				altura: 60,

				/* Link a ser acessado quando o caso de uso for clicado */
				link: "http://www.google.com"
			},
			uc001: { /* Login admin */ x: 746, y: 406, largura: 170, altura: 58},
			uc002: { /* Dados do Admin */ x: 1118, y: 456, largura: 290,	altura: 74},
			uc003: { /* Listar Funcion�rios */ x: 1140, y: 691, largura: 248,	altura: 56},
			uc004: { /* Cadast. Funcion�rios */ x: 1375 + 144, y: 612, largura: 288,	altura: 56},
			uc005: { /* Editar Funcion�rios */ x: 1386 + 113, y: 744, largura: 226,	altura: 56},
			uc006: { /* Desat. Funcion�rios */ x: 1375 + 84, y: 859, largura: 168,	altura: 86},
			uc007: { /* L Setores */ x: 861 + 84, y: 873, largura: 168,	altura: 56},
			uc008: { /* C Setores */ x: 1017 + 112, y: 1008, largura: 224,	altura: 60},
			uc009: { /* E Setores */ x: 606 + 84, y: 969, largura: 168,	altura: 56},
			uc010: { /* D Setores */ x: 785 + 103, y: 1033, largura: 206,	altura: 60},
			uc011: { /* L Usu�rios */ x: 383 + 103, y: 658, largura: 206,	altura: 56},
			uc012: { /* C Usu�rios */ x: 169 + 113, y: 542, largura: 226,	altura: 56},
			uc013: { /* E Usu�rios */ x: 394 - 84, y: 778, largura: 168,	altura: 56},
			uc014: { /* D Usu�rios */ x: 34 + 113, y: 658, largura: 226,	altura: 60},
			uc015: { /* Login Usu�rio */ x: 886 + 84, y: 123, largura: 168,	altura: 56},
			uc016: { /* Logout Usu�rio */ x: 1183 + 63, y: 93, largura: 126,	altura: 56},
			uc017: { /* Dados do Usu�rio */ x: 941 + 158, y: 216, largura: 316,	altura: 74}

		};

		function main(){
			diagrama.largura = diagrama.imagem.width;
			diagrama.altura = diagrama.imagem.height;

			ctx.drawImage(diagrama.imagem, 0, 0, diagrama.largura, diagrama.altura);
		}

		/* Evento disparado quando o mouse sobrevoa o canvas ou clica nele */
		function getCursorPosition(event) {
			
			var x = event.offsetX;
    			var y = event.offsetY;

			/* Calcula a propor��o das dimens�es atuais do canvas para a original da imagem */
			var cs = getComputedStyle(canvas);
    			var largura = parseInt(cs.getPropertyValue('width'), 10);
    			var altura = parseInt(cs.getPropertyValue('height'), 10);
			
			var proporcaoLargura = largura/diagrama.largura;
			var proporcaoAltura = altura/diagrama.altura;

			/* Para cada item do objeto, nesse caso, pegar� cada caso de uso do dicion�rio, mas somente o id */
			for(var id_caso in casos){

				/* usa-se o id para acessar o item do dicion�rio, que como � objeto, tamb�m pode acessar como caso.id_caso*/
				var uc = casos[id_caso];

				/* Calcula o raio menor e maior da elipse */
				var a = uc.largura / 2;
				var b = uc.altura / 2;

				/* Aplica a propor��o nas coordenadas e dimens�es da elipse  */
				var aCalc = a * proporcaoLargura;
				var bCalc = b * proporcaoAltura;
		
				var xCalc = uc.x * proporcaoLargura;
				var yCalc = uc.y * proporcaoAltura;

				/* Verifica se o ponto clicado do mouse est� dentro da �rea da elipse conforme a f�rmula (x-x0)/(a^2) + (y-y0)/(b^2) <= 1 */
				if(Math.pow(x - xCalc, 2)/Math.pow(aCalc,2) + Math.pow(y - yCalc, 2)/Math.pow(bCalc,2) <= 1){

					if(event.type == "click") {
						/* Se o evento que disparou a fun��o foi o clique, redireciona para o link do caso de uso */
						window.location.href = "caso_de_uso.html?id=" + id_caso;
					}
					else if(event.type == "mousemove"){
						/* Se o mouse est� em cima do caso de uso, exibe um ponteiro indicativo do mouse */
						canvas.style.cursor = "pointer";
					}
					return;
				}
		
				/* Se nenhum caso de uso est� com mouse sobrevoando ou clicado, retorna o ponteiro do mouse para o padr�o*/
				canvas.style.cursor = "initial";
			}
		}
