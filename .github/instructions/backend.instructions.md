---
description: Use ao criar, alterar ou revisar backend, APIs, business logic server-side, persistência, integrações, autenticação ou autorização.
---

# Instruções de Backend

Siga a stack, arquitetura e convenções existentes.

Não presuma framework ou linguagem.

## Boundaries

Separe adequadamente:

```text
Transport
    ↓
Application / Use Cases
    ↓
Domain
    ↓
Persistence / Integrations
```

Essa estrutura é conceitual.

Não crie camadas sem benefício real.

---

## Business Logic

Mantenha regras de negócio:

- explícitas;
- testáveis;
- consistentes;
- independentes de UI;
- protegidas no server-side.

Evite business logic complexa dentro de controllers ou routes.

Não duplique regras importantes entre endpoints.

---

## APIs

Defina contracts claros.

Considere:

- request;
- response;
- validation;
- status codes;
- error contract;
- authentication;
- authorization;
- pagination;
- filtering;
- sorting;
- idempotency;
- compatibility.

Não exponha detalhes internos desnecessários.

---

## Input Validation

Valide dados externos no boundary apropriado.

Considere:

- type;
- format;
- range;
- length;
- enum;
- cardinality;
- semantic validity.

Trate responses de integrações externas como input não confiável.

---

## Authentication

Use mecanismos estabelecidos e bibliotecas confiáveis.

Não desenvolva algoritmos criptográficos próprios.

Proteja:

- credentials;
- sessions;
- tokens;
- recovery flows.

Não registre material de autenticação sensível.

---

## Authorization

Toda operação protegida deve possuir autorização server-side adequada.

Considere:

- action;
- role;
- permission;
- ownership;
- tenant;
- resource;
- state.

Evite IDOR.

Campos privilegiados controlados pelo servidor não devem ser aceitos
livremente do cliente.

---

## Persistence

Use queries parametrizadas ou mecanismos seguros do ORM/query layer.

Considere:

- transactions;
- integrity constraints;
- uniqueness;
- indexes;
- concurrency;
- query limits;
- pagination.

Não carregue datasets potencialmente grandes sem limites.

---

## Migrations

Alterações de schema devem usar o mecanismo de migration existente.

Considere:

- existing data;
- defaults;
- nullability;
- compatibility;
- indexes;
- constraints;
- deployment order;
- rollback quando apropriado.

Evite schema changes destrutivas sem estratégia explícita.

---

## External Integrations

Defina comportamento para:

- timeout;
- retry;
- backoff;
- authentication;
- rate limiting;
- dependency failure;
- idempotency;
- observability.

Não faça retry indiscriminado de operações não idempotentes.

---

## Error Handling

Mapeie erros internos para respostas externas seguras.

Não retorne:

- stack traces;
- credentials;
- SQL details;
- filesystem paths;
- internal service topology.

Technical errors e logs devem estar em inglês.