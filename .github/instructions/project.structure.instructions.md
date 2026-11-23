---
description: Use ao definir ou alterar a estrutura de arquivos e diretórios de um projeto.
applyTo: "**"
---

# Instruções de Estrutura de Projeto

Organize arquivos de forma previsível e compatível com a stack, o escopo e as
convenções do projeto. Esta estrutura-base é adaptável, não uma árvore
obrigatória para todas as tecnologias.

## Projetos existentes

- Inspecione a organização, os manifests, as ferramentas e os pontos de entrada
  existentes antes de adicionar ou mover arquivos.
- Preserve os padrões consolidados e coloque arquivos próximos aos componentes
  ou funcionalidades relacionados, respeitando os boundaries existentes.
- Não reorganize diretórios apenas para aderir a esta estrutura-base.
  Mudanças estruturais relevantes exigem justificativa, alinhamento com o
  usuário e validação de imports, build, testes e contratos afetados.

## Projetos novos

- Identifique requisitos, stack, ferramentas e convenções do framework antes
  de definir nomes ou diretórios. Respeite caminhos exigidos pela ferramenta.
- Organize, conforme necessário, código, testes, documentação e configuração.
  Prefira uma raiz clara, com manifests e pontos de entrada nos locais esperados
  pela stack; não crie diretórios ou camadas vazios por antecipação.
- Na ausência de uma convenção mais apropriada, considere `src/` para código,
  `tests/` para testes e `README.md` para orientações do projeto. Adapte ou
  dispense esses nomes quando a stack ou o escopo indicar outra organização,
  inclusive quando os testes forem colocados próximos ao código.
- Para decisões estruturais relevantes ou sem convenção clara, proponha uma
  organização e alinhe-a com o usuário antes de criar a estrutura.

## Organização interna

- Siga as convenções da stack e agrupe por funcionalidade quando isso melhorar
  coesão e localização do código. Mantenha juntos os arquivos relacionados,
  sem misturar responsabilidades que exijam boundaries distintos.
- Use organização por camadas ou outros padrões quando forem a convenção do
  projeto ou resolverem uma necessidade concreta. Não imponha arquitetura,
  monorepo, packages compartilhados ou abstrações sem justificativa.
- Mantenha arquivos compartilhados em locais com responsabilidade clara; não
  crie diretórios genéricos apenas para acomodar código sem ownership definido.
- Coloque configuração, arquivos gerados, dados de teste e documentação
  conforme as ferramentas existentes. Não versione secrets, caches ou outputs
  gerados que o projeto não deva compartilhar.

## Validação

Após mudanças estruturais, execute as verificações pertinentes disponíveis,
incluindo imports, build e testes afetados. Informe limitações e não afirme
compatibilidade sem evidência.
