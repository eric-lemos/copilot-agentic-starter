---
name: discovery
description: Propõe requisitos a partir de uma ideia em linguagem natural e registra o discovery. Use ao invocar /discovery.
argument-hint: "[descrição do projeto]"
disable-model-invocation: true
---

# Discovery

Use a descrição fornecida após o comando como ponto de partida. Se estiver
ausente, solicite a ideia ao usuário. Siga
[Product Discovery](../agentic-software-delivery/references/product-discovery.md),
as regras globais e o modelo de orquestração do workspace.
Se o usuário solicitar a continuação de um discovery existente, leia o
documento indicado, ou `DISCOVERY.md` na raiz quando não houver indicação,
e retome a revisão sem criar uma proposta independente. Se ele não puder ser
lido ou for inválido, informe o problema.

1. Investigue o contexto relevante e elabore uma proposta consolidada em pt-BR,
   com MVP, requisitos, critérios de aceite, alternativas e trade-offs.
   Recomende a stack necessária, sua finalidade e compatibilidade e, quando
   houver interface, o Design System e as foundations aplicáveis. Considere
   segurança, dados, integrações, operação e testes quando relevantes, sem
   incluir tecnologias ou tópicos desnecessários. Reutilize a stack existente
   e siga as instruções de stacks pertinentes. Diferencie informações
   confirmadas, propostas, alternativas, assumptions e decisões pendentes.
   Não implemente o projeto durante discovery.
   Examine explicitamente cada arquivo `*.instructions.md` em
   `.github/instructions/`, inclusive os que não forem carregados
   automaticamente por `applyTo`. Registre sua aplicabilidade, as seções
   consultadas, justificativa e IDs relacionados conforme o contrato. Não
   transforme toda regra de engenharia em requisito de produto.
2. Identifique explicitamente as recomendações para adoção, separando-as das
   alternativas e das questões que exigem resposta específica. Registre
   dúvidas materiais sem inventar confirmações. Apresente uma proposta
   consolidada para o usuário aceitar de uma vez ou indicar ajustes, em vez
   de uma sequência de perguntas.
3. Monte o JSON a partir da ideia e do contexto, sem exigir que o usuário escreva JSON,
   seguindo o [contrato de discovery](../agentic-software-delivery/references/discovery-contract.md).
   Em novos documentos, use a versão `1.3` e `status: "proposed"` até o aceite
   explícito. Ao continuar um documento anterior, preserve sua versão, salvo
   se o usuário solicitar migração. Preserve recomendações, alternativas,
   critérios de aceite e pendências relevantes.
4. Salve o rascunho em `DISCOVERY.md` na raiz do workspace, ou no
   caminho de arquivo explicitamente solicitado pelo usuário. O documento deve
   conter um único bloco cercado `json` com o contrato completo e pode conter
   explicações em Markdown consistentes com esse bloco. O JSON é a fonte de
   verdade para delivery e handoffs.
5. Se o destino já existir antes de um novo discovery, leia-o e peça
   confirmação antes de substituí-lo. Na continuação solicitada pelo usuário,
   atualize o rascunho existente sem descartar conteúdo alheio às mudanças
   solicitadas. Não sobrescreva conteúdo existente sem autorização. Se não
   for possível gravar, informe a falha.
6. Se o usuário solicitar ajustes, refine a proposta e atualize o rascunho;
   preserve decisões já confirmadas e apresente novamente o que mudou. Ao
   receber aceite explícito e inequívoco da proposta e resolver as questões
   bloqueantes, atualize o mesmo arquivo para `status: "approved"` conforme o
   contrato. O aceite abrange as recomendações para adoção, não alternativas,
   assumptions ou questões pendentes. Se o arquivo tiver mudado externamente,
   leia e preserve as alterações antes de atualizá-lo.
7. Após criar ou atualizar o documento, execute a verificação de avaliações
   descrita no contrato, passando o caminho escolhido de forma segura como
   argumento. Corrija problemas do documento e reexecute; se a ferramenta
   estiver indisponível ou falhar, informe o bloqueio e não afirme que a
   avaliação foi verificada. Uma baseline aprovada não pode ter avaliações
   pendentes na versão `1.3`. Em documentos anteriores, informe o aviso de que
   a avaliação não é verificável. A verificação não confirma que a análise
   está correta.
8. Informe o caminho e o estado do documento. Não interprete silêncio ou a
   invocação de `/delivery` como aprovação explícita; somente a baseline
   aprovada pode orientar a implementação.
