---
name: refactor
description: Analisa uma aplicação existente e prepara uma proposta de refatoração para revisão. Use ao invocar /refactor.
argument-hint: "[caminho da aplicação] [objetivo]"
disable-model-invocation: true
---

# Refactor

Este comando prepara uma refatoração; não implementa a aplicação nem altera
seu código durante a análise. Siga as regras globais, o modelo de orquestração,
[Code Refactoring](../agentic-software-delivery/references/code-refactoring.md)
e o fluxo de proposta, avaliação das instruções, refinamento e aprovação de
[Discovery](../discovery/SKILL.md), adaptados a uma aplicação existente.
Ao retomar uma proposta existente, leia o ROADMAP indicado, ou `ROADMAP.md` na
raiz por padrão, e use a origem registrada. Preserve o conteúdo e as
alterações existentes; informe se o documento estiver ausente ou for inválido.

1. Identifique a aplicação e o objetivo descritos pelo usuário. Use `project/`
   como caminho de origem padrão apenas se ali houver uma aplicação existente;
   se não houver, ou se o caminho for ambíguo, solicite o caminho. Aceite
   caminhos explícitos dentro do workspace e registre-os relativos à sua raiz.
   Não confunda os arquivos agentic deste starter com a aplicação sem
   confirmação do usuário.
2. Examine o código e a organização relevantes, manifests, stack e versões,
   pontos de entrada, dependências, contratos, comportamento, dados, testes,
   configuração, segurança e operação conforme aplicável. Identifique
   evidências, lacunas, limitações de acesso e mudanças existentes. Não
   execute operações destrutivas nem altere código durante o diagnóstico.
3. Examine cada arquivo `*.instructions.md` em `.github/instructions/`,
   inclusive os não carregados automaticamente. Avalie aplicabilidade,
   seções e rastreabilidade conforme o contrato de discovery. Recomende
   melhorias e opções de stack proporcionais ao problema, preservando a stack
   existente quando adequada e sem presumir migração ou tecnologias novas.
4. Avalie a estrutura prevista em
   [project.structure.instructions.md](../../instructions/project.structure.instructions.md)
   como padrão para a entrega em `project/`. Compare-a com a aplicação
   existente, proponha a adequação quando viável e explique exceções e impacto
   em imports, dados, configurações, workflows e contratos. Não mova arquivos,
   repositórios ou dados durante esta etapa; preserve o comportamento e as
   mudanças do usuário.
5. Apresente uma proposta consolidada com estado atual e evidências, objetivo,
   escopo, comportamento e contratos a preservar, etapas de refatoração,
   decisões de stack e estrutura, riscos, alternativas, critérios de aceite e
   estratégia de testes. Distinga fatos, recomendações, assumptions e
   decisões pendentes. Não apresente funcionalidades novas ou mudanças de
   comportamento como mera refatoração.
6. Salve um rascunho em `ROADMAP.md` na raiz do workspace, ou no caminho
   explicitamente solicitado, seguindo o
   [contrato de discovery](../agentic-software-delivery/references/discovery-contract.md)
   versão `1.4` e `work_type: "refactor"`. Registre a aplicação de origem, a
   raiz de entrega proposta, estado atual, preservação e estratégia de
   validação. Se o destino existir, leia-o e peça confirmação antes de
   substituí-lo; ao retomar um rascunho indicado, preserve alterações alheias.
7. Solicite aceite da proposta inteira ou ajustes, refine conforme o feedback
   e atualize o mesmo documento. Só marque como aprovado após aceite explícito
   e resolução de questões bloqueantes, incluindo qualquer mudança material
   de estrutura, stack, dados ou contratos. Valide o documento com o comando
   local previsto no contrato após cada gravação; relate falhas e não alegue
   verificação bem-sucedida sem evidência.
8. Informe o caminho e o estado do ROADMAP e que a implementação começa com
   `/delivery` após aprovação. Não interprete silêncio ou `/delivery` como
   aceite explícito.
