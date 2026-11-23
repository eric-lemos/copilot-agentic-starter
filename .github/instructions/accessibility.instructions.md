---
description: Use ao criar, alterar ou revisar acessibilidade de interfaces web, navegação por teclado, formulários ou semântica HTML.
applyTo: "**/*.{html,css,scss,sass,less,jsx,tsx,vue,svelte,astro}"
---

# Instruções de Acessibilidade

Trate acessibilidade como requisito funcional da interface.

Quando aplicável, utilize WCAG 2.2 AA como referência.

## Semântica

Prefira elementos HTML nativos.

Utilize:

- `button` para ações;
- `a` para navegação;
- `input`, `select` e `textarea` para controles apropriados;
- headings em uma hierarquia coerente;
- landmarks quando apropriado.

Não recrie controles nativos usando elementos genéricos sem necessidade.

---

## Keyboard

Toda funcionalidade interativa deve ser operável por teclado quando
aplicável.

Garanta:

- focus visible;
- logical focus order;
- ausência de keyboard traps;
- gerenciamento de foco em dialogs e fluxos dinâmicos.

---

## Forms

Campos devem possuir accessible names.

Erros devem:

- identificar o campo;
- explicar o problema;
- ser associados ao controle quando possível.

Não dependa somente de placeholder como label.

---

## Color

Não use cor como único mecanismo para comunicar:

- erro;
- status;
- seleção;
- severidade;
- sucesso.

Mantenha contraste adequado.

---

## Dynamic Content

Atualizações importantes devem ser perceptíveis por assistive technologies.

Use ARIA live regions somente quando apropriado.

Evite anúncios excessivos.

---

## Images

Forneça `alt` significativo para imagens informativas.

Imagens decorativas não devem gerar ruído para screen readers.

---

## Motion

Respeite `prefers-reduced-motion` quando animações puderem impactar
acessibilidade.

Não dependa exclusivamente de animação para transmitir informação.

---

## ARIA

Primeira regra de ARIA:

> Prefira semântica HTML nativa quando ela resolver o problema.

Não adicione roles ou atributos ARIA redundantes ou incorretos.

ARIA não corrige comportamento interativo inexistente.

---

## Testing

Quando ferramentas estiverem disponíveis, combine:

- automated accessibility checks;
- keyboard testing;
- semantic inspection;
- screen reader validation para fluxos críticos quando necessário.

Automated checks não substituem avaliação manual.