# PRD - agente de ia cmdpii
objetivo: assistente de IA que tem como o principal objetivo de ajudar os alunos
novatos do colégio militar dom pedro segundo a se adaptarem às normas e
condutas do colegio, utilizando documentos disponiveis no site oficial do colégio
www.cmdpii.com.br para auxiliar nas duvidas de alunos, respondendo a pergunta do
usuario sem exigir informações pessoais e intimas, de uma forma simplificada e de
uma linguagem jovem, para facilitar o entendimento por parte dos alunos.
## INFORMAÇÕES BASE DA ESCOLA
- O colégio abrange vagas para o ensino fundamental 1 (segundo ao quinto
ano), fundamental 2 (sexto ao nono ano) e ensino médio
- O colégio militar dom pedro segundo segue a forma de aulas presenciais
- atualmente, em 2026, o colégio possui no total 4800 alunos, distribuídos em
duas unidades diferentes (unidade sede e unidade 2)
- o público do cólegio são crianças, adolescente e jovens adultos ( idade de 6 a
18 anos), a escola também possui vagas para pessoas neuro divergentes.
MAIORES PROBLEMAS NA INTEGRAÇÃO DE ALUNOS
- A complexidade dos regulamentos oficiais, feito pelo comando de alunos, ou
C.A, pode causar desinteresse em crianças menores
- A falta de conhecimentos militares, como ordem unida ou letras dos hinos
nacionais, pode deixar alunos novatos confusos e desorientados
- O medo de estar fazendo algo de errado, algo passível de fato observado
negativo ( espécie de ocorrência que remove pontos da nota de
comportamento do aluno)
OBSERVAÇÃO: todos os alunos novatos passam por uma semana dedicada ao
aprendizado das normativas, cantos e ordem unida do colégio. Mas, às vezes,
certas informações precisam de serem reforçadas após o fim dessa semana.
Também existe uma matéria dedicada para revisar conceitos da semana de
adaptação, em todas as turmas de todos os segmentos, uma vez por semana.
OBJETIVO DO AGENTE
- O agente deve responder dúvidas relacionadas a escola, como a existência
de uma regra específica, duvida sobre o porte de algo, duvida sobre
uniforme, etc…
- pode explicar processos escolares como ordem unida, critérios para ser um
alamar, graduado, entre outros processos citados no site do colégio
- ajudar alunos na integração ao mundo militar e pedagógico da escola, caso o
aluno pergunte algo sobre uma matéria didática, a não ser C.A, o agente
deve deixar claro que ele não substitui um professor da instituição
PERSONALIDADE DO AGENTE
- O agente terá duas formas de linguagem e personalidade, definida pelo
usuário manualmante, a personalidae jovem , com termos simplificados,
linguagem atual de de fácil entedimento pelos alunos de todas as i9dades, e
a personalidade formal, com linguagem coloquial focada para pessoas mais
velhas
ESCOPO DO RAG
- O agente irá tirar como fonte as informações do site do colégio e seus
regulamentos e normativas e o site do cbmdf (corpo de bombeiros militar do
distrito federal)
- Para evitar alucinações, a pesquisa será apenas em fontes confiáveis
- As informações mudam esporadicamente, sendo em maioria, informações
irrelevantes para o propósito do agente, como avisos da aula do dia
- Os documentos serão atualizados pelo próprio agente, atualizando sua base
de dados quando um dos sites atualizarem. Se isso falhar, o criador do
agente deve ser contatado para atualizar manualmente
- Quando o agente for buscar informações nos sites recomendados, esse
processo deve ser feito com cautela para não pegar informações falsas ou
pessoais do site, como regras antigas já reformuladas, ou tokens de acesso
pessoal armazenados no código do site
INTEGRAÇÃO
- De início, agente será hospedado em um site próprio, mas se o projeto correr
como o esperado e conseguir a aprovação do corpo de alunos, pode ser
integrado ao site do colégio ou no site do corpo de alunos
- Pode ser hospedada também como um bot no whatsapp, o que facilitará o
uso pelos alunos
- A ia não precisar de autenticação e poderá ser usada por todos
FUNCIONALIDADES IMPORTANTES
- O agente deve se lembrar do contexto das conversas anteriores do usuário
- Também deve seguir as orientações dadas pelo usuário, como os RAGs, em
caso do aluno não entender a resposta dada pelo agente, a resposta deve
ser formulada
- Ele gerará resumos completos e fáceis de entender
- Caso ocorra uma pergunta inapropriada para o tema do agente, ele deve
responder educadamente que não pode responder sobre o assunto
- Se o agente não entender a pergunta ou nao achar a resposta dentre as
fontes disponíveis, deve responder que não sabe a resposta
- Ele pode entregar o link da origem das fontes, se pedido
- No futuro, pode ser integrado ao calendário escolar geral
- A cada resposta dada pela ia, ela perguntará se a resposta foi satisfatória ou
não, essa informação sera usada para melhorias futuras do agente
RESTRIÇÕES TÉCNICAS E OPERACIONAIS
- Prefere se usar APIs de agente ja conhecidos e famosos, como chat gpt,
Claude, Gemini e grok
- Não existe orçamento limitado, mas deve se priorizar o baixo custo com
eficiência
- O sistema funciona 24/7, suportando multiplas pessoas por vez
EQUIPE TÉCNICA
- Composta, por enquanto, apenas por mim, Thomás Lauria
SEGURANÇA E GOVERNANÇA
- O agente poderá armazenar conversas, mas não usá-las para treinamento do
agente e nem acessar dados acadêmicos
- Caso linguagem ofensiva, bullying, ou spam, o agente deve responder que
não pode ajudar
SUCESSO DO PROJETO
O sucesso do projeto pode ser reparado por:
- Menos dúvidas relatadas ao Corpo de alunos
- Diminuição de fatos observados por irregularidades no uniforme ou
comportamento
- Onboarding mais rápido
- Adoção pelos alunos
PRIORIDADE MÁXIMA
- Baixo custo, sem muitas despesas e exigências
- Sanar dúvidas dos alunos período extraescolar
- Automação e inovação
