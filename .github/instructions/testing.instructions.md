---
description: Use ao planejar, criar, alterar ou revisar unit, integration, component, contract, regression ou end-to-end tests.
applyTo: "**/*.{test,spec}.*,**/*_{test,spec}.*,**/test_*.py,**/*{Test,Tests,Spec,Specs}.*,**/{test,tests,__tests__,spec,specs}/**"
---

# Instruções de Testes

Escreva testes orientados a comportamento e risco.

Use as ferramentas de testes já estabelecidas no projeto.

## Test Pyramid

Prefira, conforme aplicável:

```text
       E2E
    Component
   Integration
      Unit
```

Utilize o nível mais baixo capaz de validar o comportamento com confiança.

Não implemente tudo como E2E.

---

## Qualidade dos Testes

Testes devem ser:

- deterministic;
- repeatable;
- independent;
- readable;
- behavior-oriented;
- focused.

Evite:

- arbitrary sleeps;
- execution-order dependencies;
- shared mutable state;
- external production dependencies;
- excessive mocking;
- implementation-detail assertions.

---

## Cenários

Considere:

- happy path;
- boundaries;
- invalid input;
- missing input;
- dependency errors;
- authentication;
- authorization;
- empty states;
- retries;
- regression scenarios.

Não gere combinações irrelevantes apenas para aumentar coverage.

---

## Regression Tests

Para bug fixes:

1. reproduza o problema quando possível;
2. crie teste que proteja o comportamento esperado;
3. aplique a correção;
4. execute o teste;
5. execute testes relacionados.

Não faça o teste refletir apenas os detalhes da implementação corrigida.

---

## Mocking

Mock boundaries quando necessário.

Evite mockar toda a cadeia interna.

Prefira testar comportamento real quando isso puder ser realizado de forma
rápida, determinística e isolada.

---

## Test Data

Nunca utilize secrets ou dados pessoais reais desnecessariamente.

Prefira dados:

- synthetic;
- deterministic;
- minimal;
- self-contained.

Realize cleanup quando necessário.

---

## UI Testing

Prefira selectors baseados em:

- accessible role;
- label;
- visible text;
- stable test identifier quando necessário.

Evite selectors dependentes da estrutura interna do DOM.

---

## API Testing

Considere:

- contracts;
- status codes;
- validation;
- authentication;
- authorization;
- pagination;
- error schemas;
- protected fields.

---

## Falhas

Quando um teste falhar, determine se a causa é:

- product defect;
- test defect;
- environment;
- configuration;
- dependency;
- flakiness.

Não enfraqueça assertions legítimas apenas para obter um resultado verde.

---

## Coverage

Coverage é indicador, não objetivo absoluto.

Priorize:

- critical paths;
- business rules;
- authorization;
- failure paths;
- regressions.

Não adicione testes sem valor apenas para aumentar percentual.