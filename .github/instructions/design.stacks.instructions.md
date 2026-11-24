---
description: Use ao trabalhar com Design Systems adotados ou avaliar referências para uma direção visual.
applyTo: "**/*.{html,css,scss,sass,less,jsx,tsx,vue,svelte,astro}"
---

# Instruções para Stacks de Design

Estas orientações se aplicam a interfaces. Siga também
`.github/instructions/design.instructions.md` e as instruções de frontend e
acessibilidade.

Identifique primeiro o Design System, a implementação e a versão usados pela
área afetada. Aplique uma seção quando o sistema já for adotado ou quando o
usuário tiver aprovado seu uso. As referências apoiam a escolha, mas não
autorizam por si só a adoção de componentes ou dependências.

## Escolha de Design System

Material Design, Fluent 2, Carbon, Ant Design e Spectrum são opções de
referência a avaliar prioritariamente ao recomendar um Design System, não uma
lista fechada nem uma ordem de preferência entre elas. Escolha conforme o
produto, a plataforma, a stack, a acessibilidade e os requisitos; recomende
outra opção justificada se as documentadas não forem adequadas. A existência de
uma seção neste arquivo não significa que a biblioteca esteja instalada ou
seja compatível com o projeto.

A escolha de um Design System é obrigatória para construir ou alterar
interfaces, inclusive protótipos e projetos existentes. Quando houver um sistema
adotado, preserve-o, inclusive sua implementação e versão, salvo mudança
explicitamente solicitada e alinhada. Se houver apenas uma identidade ou padrões
informais, preserve-os e proponha um sistema compatível, sem presumir que já
constituem um Design System escolhido ou exigir uma migração abrangente.

Se a escolha estiver em aberto, antes da implementação visual apresente opções
e trade-offs proporcionais ao escopo, recomende uma alternativa e obtenha a
aprovação do usuário. Uma escolha explícita do usuário ou um sistema já adotado
não exige nova aprovação. Não trate silêncio como aprovação nem confunda a
aprovação de uma direção visual com autorização para instalar uma dependência
diferente da proposta aprovada. A escolha de um sistema não obriga a adoção de
uma biblioteca: use uma implementação compatível com a stack e os requisitos.

Verifique a licença da implementação e da versão escolhidas, incluindo seus
avisos e obrigações. Documentação, fontes, ícones, marcas e outros assets podem
ter termos próprios: não presuma que tenham a mesma licença do código nem copie
conteúdo sem autorização. Respeite as restrições de pesquisa e execução do
workspace; não introduza serviços externos em runtime.

## Foundations para frontend

Antes da construção visual, identifique e alinhe as foundations fornecidas
pelo sistema escolhido e as customizações necessárias ao produto: cores e
contraste, tipografia, espaçamento e escala, layout responsivo, formas e
superfícies, ícones, estados de interação, foco e movimento quando aplicáveis.
Defina temas e tokens semânticos pertinentes, padrões de componentes e
requisitos de acessibilidade. Use as fontes e mecanismos reais do sistema e
da implementação escolhida; não presuma que uma especificação e uma biblioteca
ofereçam as mesmas capacidades.

Registre a escolha, implementação e versão quando houver, foundations
aplicáveis, customizações e lacunas na baseline ou handoff proporcional à
tarefa, sem exigir documento novo. Reutilize mecanismos existentes e defina
somente o necessário para a interface; não crie uma camada global de tokens
ou componentes duplicados apenas por formalidade.

## Fidelidade ao sistema adotado

Para interfaces novas, redesigns e alterações visuais relevantes:

1. Identifique a implementação e a versão reais na área afetada, os componentes
   compartilhados, temas, tokens e customizações do produto. Uma especificação
   como Material Design não identifica, por si só, a biblioteca instalada nem
   sua cobertura de componentes.
2. Para os elementos e estados relevantes da tarefa, consulte primeiro as
   fontes locais e, quando necessário e permitido, a documentação e os exemplos
   públicos correspondentes à implementação e à versão. Não presuma que APIs,
   tokens ou componentes de implementações distintas sejam intercambiáveis.
3. Antes de implementar, associe as principais partes da interface aos
   componentes, variantes e tokens disponíveis. Reutilize padrões de navegação,
   layout, tipografia, cor, espaçamento e interação do produto e do sistema.
   Quando houver uma lacuna, estenda os mecanismos existentes de forma
   localizada; justifique desvios em vez de recriar componentes equivalentes
   ou misturar bibliotecas sem necessidade.
4. Verifique estados e comportamento aplicáveis, incluindo foco, hover,
   disabled, loading, empty e error, além de conteúdo representativo,
   acessibilidade e adaptação aos viewports suportados.
5. Quando houver aplicação executável e ferramentas disponíveis, renderize e
   compare a interface com o tema do produto e as referências pertinentes em
   desktop e mobile; corrija inconsistências observáveis dentro do escopo.
   No handoff, identifique o sistema e a versão utilizados, desvios relevantes,
   fontes consultadas e validações efetivamente realizadas. Informe quando
   documentação, ferramentas ou inspeção visual não estiverem disponíveis;
   não afirme fidelidade visual sem verificá-la.

Adapte a profundidade dessas etapas à tarefa: uma correção visual pequena não
exige um levantamento formal. As referências orientam escolhas e comportamento,
mas não autorizam copiar marcas, textos, imagens ou layouts proprietários.

## Material Design

- Siga a versão e os componentes, tokens e temas Material já adotados.
- Consulte as [diretrizes Material](https://m3.material.io/) para orientar
  escolhas compatíveis com o produto; não presuma que Material Web e outras
  implementações sejam intercambiáveis.
- O repositório [Material Web](https://github.com/material-components/material-web/blob/main/LICENSE)
  declara licença Apache 2.0 para seu código; verifique os termos dos assets.

## Fluent 2

- Siga os padrões de componentes, temas e tokens da implementação usada na
  plataforma e versão do projeto.
- Consulte as [diretrizes Fluent 2](https://fluent2.microsoft.design/) para
  decisões de interface e acessibilidade compatíveis com o produto.
- O repositório [Fluent UI](https://github.com/microsoft/fluentui/blob/master/LICENSE)
  declara licença MIT para seu código e ressalva termos próprios para assets.

## Carbon

- Siga os componentes, temas e tokens Carbon adotados, respeitando a versão e
  os padrões de layout do projeto.
- Consulte a [documentação Carbon](https://carbondesignsystem.com/) para
  orientar componentes e padrões pertinentes à tarefa.
- O repositório [Carbon](https://github.com/carbon-design-system/carbon/blob/main/LICENSE)
  declara licença Apache 2.0 para seu código; verifique os termos dos assets.

## Ant Design

- Siga a versão e os padrões de componentes, formulários e temas existentes;
  preserve semântica, validação e acessibilidade ao compô-los.
- Consulte a [documentação Ant Design](https://ant.design/) para orientar o uso
  da implementação adotada, sem presumir compatibilidade com outras stacks.
- O repositório [Ant Design](https://github.com/ant-design/ant-design/blob/master/LICENSE)
  declara licença MIT para seu código; verifique os termos dos assets.

## Spectrum

- Identifique a implementação Spectrum usada e siga seus componentes, temas e
  tokens conforme a versão e a plataforma do projeto.
- Consulte a [documentação Spectrum](https://spectrum.adobe.com/) para
  decisões de interface compatíveis com os componentes adotados.
- O repositório [React Spectrum](https://github.com/adobe/react-spectrum/blob/main/LICENSE)
  declara licença Apache 2.0 para seu código; verifique os termos dos assets.
