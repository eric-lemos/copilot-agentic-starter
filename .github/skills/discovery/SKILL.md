---
name: discovery
description: Conduz discovery a partir de uma ideia em linguagem natural e registra uma baseline aprovada. Use ao invocar /discovery.
argument-hint: "[descrição do projeto]"
disable-model-invocation: true
---

# Discovery

Use a descrição fornecida após o comando como ponto de partida. Se estiver
ausente, solicite a ideia ao usuário. Siga
[Product Discovery](../agentic-software-delivery/references/product-discovery.md),
as regras globais e o modelo de orquestração do workspace.

1. Investigue o contexto relevante e apresente uma proposta consolidada em
   pt-BR. Diferencie requisitos confirmados, derivados, recomendações,
   assumptions e decisões pendentes. Não implemente o projeto durante discovery.
2. Refine a proposta com o usuário. Resolva decisões bloqueantes e obtenha
   aprovação explícita da baseline; não interprete silêncio como aprovação.
3. Monte o JSON a partir da conversa, sem exigir que o usuário escreva JSON,
   seguindo o [contrato de discovery](../agentic-software-delivery/references/discovery-contract.md).
   Preserve decisões, critérios de aceite e pendências relevantes; não
   transforme recomendações ou assumptions em requisitos confirmados.
4. Salve a baseline aprovada em `DISCOVERY.md` na raiz do workspace, ou no
   caminho de arquivo explicitamente solicitado pelo usuário. O documento deve
   conter um único bloco cercado `json` com o contrato completo e pode conter
   explicações em Markdown consistentes com esse bloco. O JSON é a fonte de
   verdade para delivery e handoffs.
5. Se o destino já existir, leia-o e peça confirmação antes de substituí-lo.
   Não sobrescreva conteúdo existente sem autorização. Se não for possível
   gravar, informe a falha e não afirme que a baseline foi salva.
6. Informe o caminho salvo e como iniciar delivery. Se a aprovação não ocorrer
   ou restarem decisões bloqueantes, não salve uma baseline como aprovada.
