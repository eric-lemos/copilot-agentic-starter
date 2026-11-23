---
description: Use ao trabalhar com Design Systems adotados ou avaliar referências para uma direção visual.
applyTo: "**/*.{html,css,scss,sass,less,js,jsx,mjs,cjs,ts,tsx,mts,cts,vue,svelte,astro}"
---

# Instruções para Stacks de Design

Estas orientações se aplicam a interfaces. Siga também
`.github/instructions/design.instructions.md` e as instruções de frontend e
acessibilidade.

Identifique primeiro o Design System, a implementação e a versão usados pela
área afetada. Aplique uma seção quando o sistema já for adotado ou quando o
usuário tiver aprovado seu uso. Caso contrário, as referências podem apoiar uma
proposta, mas não determinam a identidade do produto nem autorizam a adoção
de componentes ou dependências.

Verifique a licença da implementação e da versão escolhidas, incluindo seus
avisos e obrigações. Documentação, fontes, ícones, marcas e outros assets podem
ter termos próprios: não presuma que tenham a mesma licença do código nem copie
conteúdo sem autorização. Respeite as restrições de pesquisa e execução do
workspace; não introduza serviços externos em runtime.

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
