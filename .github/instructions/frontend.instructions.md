---
description: Use ao criar, alterar ou revisar interfaces, frontend, componentes, estado client-side, UX, responsividade ou consumo de APIs.
applyTo: "**/*.{html,css,scss,sass,less,jsx,tsx,vue,svelte,astro}"
---

# Instruções de Frontend

Siga a stack, arquitetura, design system e convenções existentes.

Não presuma framework específico.

## Components

Crie componentes:

- focados;
- previsíveis;
- composable;
- testáveis;
- acessíveis.

Evite componentes excessivamente grandes.

Não crie abstrações genéricas antes de existir necessidade real de reuso ou
isolamento.

---

## Design Systems

Antes de criar ou alterar componentes visuais, localize as fontes existentes
no projeto: documentação, componentes compartilhados, temas, tokens, exemplos
e configuração de bibliotecas. Não presuma framework, biblioteca ou que exista
um Design System formal.

É obrigatório identificar um Design System para construir ou alterar
interfaces e definir as foundations aplicáveis antes da implementação visual.
Se ainda não houver escolha, preserve a identidade existente e siga o processo
de escolha e aprovação em `.github/instructions/design.stacks.instructions.md`.

Prefira componentes, tokens e padrões adotados. Se o sistema não cobrir a
necessidade, estenda os mecanismos existentes de forma localizada, sem duplicar
componentes ou divergir do sistema compartilhado. Não introduza uma camada
global de tokens, uma nova linguagem visual ou uma dependência sem necessidade
concreta; alinhe mudanças materiais de identidade ou arquitetura.

Preserve acessibilidade e comportamento responsivo ao usar ou estender
componentes. Siga também as instruções de acessibilidade e de direção visual em
`.github/instructions/design.instructions.md`.

---

## State Management

Diferencie:

- local UI state;
- server state;
- shared application state;
- derived state;
- URL state.

Armazene o estado no menor escopo adequado.

Não duplique server state desnecessariamente.

Não armazene estado que possa ser derivado de forma simples e segura.

---

## Async Behavior

Interfaces assíncronas devem tratar, conforme aplicável:

- loading;
- empty;
- error;
- retry;
- success;
- partial data;
- stale data.

Evite interfaces que pareçam congeladas durante operações longas.

---

## Forms

Formulários devem:

- possuir labels apropriados;
- indicar campos obrigatórios;
- validar input para UX;
- apresentar erros próximos ao contexto relevante;
- preservar input após erros recuperáveis;
- prevenir submissões duplicadas;
- indicar processamento;
- funcionar por teclado.

Client-side validation não substitui server-side validation.

---

## API Consumption

Siga contracts existentes.

Considere:

- cancellation;
- timeout;
- errors;
- authentication failures;
- authorization failures;
- pagination;
- retries;
- unexpected responses.

Não confie em responses apenas porque vieram do backend.

Use runtime validation quando fizer parte do padrão do projeto.

---

## Segurança Client-Side

Nunca considere o frontend uma security boundary confiável.

Não use controles visuais como único mecanismo de autorização.

Evite armazenar informações sensíveis em:

- localStorage;
- sessionStorage;
- URL;
- client-side logs;
- analytics;
- bundles.

Nunca inclua secrets em código client-side.

Preserve escaping fornecido pelo framework.

Evite raw HTML rendering.

---

## Performance

Otimize com base em evidência.

Considere quando relevante:

- bundle size;
- code splitting;
- lazy loading;
- rendering cost;
- large lists;
- request duplication;
- asset optimization.

Evite memoization indiscriminada.

---

## Responsividade

Interfaces devem se adaptar aos viewports suportados pelo produto.

Considere:

- content reflow;
- touch interaction;
- long text;
- zoom;
- localization;
- input methods.

Evite dimensões fixas que prejudiquem adaptação sem necessidade.

---

## Código

Siga as convenções globais de idioma para código, identificadores, comentários
e conteúdo de produto em `.github/copilot-instructions.md`.

Siga o formatter, linter e type system existentes.

Evite tipos genéricos inseguros quando a linguagem oferecer alternativas
melhores.

Não ignore erros do type checker sem justificativa.