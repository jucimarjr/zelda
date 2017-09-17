INSERT INTO `setor` (setor_id, setor_nome, setor_pai) VALUES
(1, 'Reitoria', NULL),
(2, 'Gabinete do Reitor', 1),
(3, 'Gabinete do Vice-Reitor', 1),
(4, 'Pró-Reitoria de Planejamento', 1),
(5, 'Pró-Reitoria de Adminstração', 1),
(6, 'Pró-Reitoria de Ensino de Graduação', 1),
(7, 'Pró-Reitoria de Pesquisa e Pós-Graduação', 1),
(8, 'Pró-Reitoria de Extensão e Assuntos Comunitários', 1),
(9, 'Pró-Reitoria de Interiorização', 1),
(10, 'Diretoria - Escola Superior de Tecnologia', 1),
(11, 'Conselho Acadêmico', 1),
(12, 'Secretaria Acadêmica / Pronto Atendimento ao Estudante', 10),
(13, 'Gabinete da Diretoria', 10),
(14, 'Coordenação de Qualidade do Ensino', 10),
(15, 'Coordenação de Estágio Supervisionado', 10),
(16, 'Coordenação Pós-Graduação', 10),
(17, 'Gerência de Núcleo de Práticas Jurídicas', 10),
(18, 'Assistente de Gabinete', 10),
(19, 'Assessoria Técnica Nível III', 10),
(20, 'Asessoria Técnica Nível IV', 10),
(21, 'CTIC - Coordenadoria de Tecnologia da Informação e Comunicação', 10),
(22, 'Administração do Prédio', 10),
(23, 'Núcleo de Tecnologia Assistiva', 10),
(24, 'Coordenação Ciclo Básico', 10),
(25, 'Coordenação Licenciatura em Informática', 10),
(26, 'Coordenação Tecnologia em Manutenção Mecânica', 10),
(27, 'Coordenação Tecnologia em Processamento de Dados', 10),
(28, 'Coordenação Engenharia Civil', 10),
(29, 'Coordenação Engenharia de Computação', 10),
(30, 'Coordenação Engenharia Elétrica', 10),
(31, 'Coordenação Engenharia Mecânica', 10),
(32, 'Coordenação Engenharia Mecatrônica', 10),
(33, 'Coordenação Engenharia de Produção', 10),
(34, 'Coordenação Bacharelado em Meteorologia', 10),
(35, 'Coordenação Engenharia Química', 10),
(36, 'Coordenação Tecnologia em Automação Industrial', 10),
(37, 'Coordenação Tecnologia em Análise e Desenvolvimento de Sistemas', 10),
(38, 'Coordenação Engenharia de Controle e Automação', 10),
(39, 'Coordenação Tecnologia em Agrimensura', 10),
(40, 'Coordenação Engenharia Naval', 10),
(41, 'Coordenação Licenciatura em Física', 10),
(42, 'Coordenação Licenciatura em Computação', 10),
(43, 'Coordenação Engenharia de Materiais', 10),
(44, 'Coordenação Engenharia Eletrônica', 10),
(45, 'Coordenação Bacharelado em Sistema de Informação', 10),
(46, 'Coordenação Tecnologia em Jogos Digitais', 10),
(47, 'Coordenação Bacharelado em Química', 10);

--
-- Indexes for table `setor`
--
ALTER TABLE `setor`
  ADD PRIMARY KEY (`setor_id`);

--
-- AUTO_INCREMENT for table `setor`
--
ALTER TABLE `setor`
  MODIFY `setor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;COMMIT;
