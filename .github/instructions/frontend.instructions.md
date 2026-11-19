---
description: Use ao criar, alterar ou revisar interfaces, frontend, componentes, estado client-side, UX, responsividade ou consumo de APIs.
applyTo: "**/*.{html,css,scss,sass,less,jsx,tsx,vue,svelte}"
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

Use inglês para código, identifiers, comments e technical outputs.

Siga o formatter, linter e type system existentes.

Evite tipos genéricos inseguros quando a linguagem oferecer alternativas
melhores.

Não ignore erros do type checker sem justificativa.