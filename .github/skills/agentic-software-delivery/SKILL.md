---
name: agentic-software-delivery
description: Use para discovery de produto, delivery multidisciplinar, investigação de bugs complexos, refactoring estrutural, revisões amplas ou estratégia de testes quando um workflow explícito agregar valor. Não use apenas por se tratar de uma mudança simples e localizada.
---

# Agentic Software Delivery

Aplicar o workflow correspondente à intenção do usuário. Comunicar-se em pt-BR. Produzir código, identifiers, comments, logs e tests em inglês. Escrever em pt-BR a documentação criada ou atualizada pelos agentes, conforme `.github/copilot-instructions.md`.

## Regras comuns

1. Siga `.github/copilot-instructions.md` e `AGENTS.md` na raiz quando existirem; leia-os se suas instruções ainda não estiverem no contexto. Consulte `.github/AGENTS.md` quando o modelo de discovery ou delivery, a coordenação entre agentes ou seus handoffs forem relevantes; leia apenas as seções necessárias. Se não for possível acessar instruções necessárias, informe a limitação.
2. Consultar os Agents e Instructions relevantes quando necessário, respeitando solicitações explícitas para não utilizá-los.
3. Inspecionar o workspace antes de presumir stack, arquitetura, contracts ou comandos.
4. Manter alterações e execução locais. Permitir pesquisa pública anônima e somente para leitura conforme `.github/copilot-instructions.md`; não usar conectores externos, produção ou credenciais reais.
5. Tratar recomendações, assumptions e requisitos confirmados como categorias distintas.
6. Não afirmar execução, validação ou sucesso sem evidência real.
7. Manter mudanças focadas; evitar overengineering e refactoring não relacionado.
8. Solicitar decisão apenas quando a ambiguidade alterar materialmente produto, arquitetura, segurança, dados, contratos, compatibilidade, custo ou operação.

## Seleção do workflow

- Ideia nova, requisito amplo ou refinamento iterativo: ler `references/product-discovery.md`.
- Feature pronta para implementação ou sistema com baseline suficiente: ler `references/feature-delivery.md`.
- Comportamento incorreto, falha ou regressão: ler `references/bug-resolution.md`.
- Melhoria estrutural preservando comportamento: ler `references/code-refactoring.md`.
- Revisão ampla de alterações sem edição automática: ler `references/code-review.md`.
- Revisão independente de segurança: ler `references/security-review.md`.
- Estratégia, criação ou execução de testes: ler `references/test-creation.md`.

Quando a solicitação combinar workflows, começar pelo que reduz maior incerteza. Exemplo: usar discovery antes de feature delivery para um sistema novo ainda indefinido; usar bug resolution antes de refactoring quando há falha funcional.

## Saída

Responder em pt-BR com estrutura proporcional à tarefa. Incluir somente fatos confirmados, decisões relevantes, validações executadas e limitações. Persistir documentos no workspace apenas quando solicitado ou necessário ao workflow.