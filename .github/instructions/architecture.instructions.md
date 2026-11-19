---
description: Use ao analisar ou alterar arquitetura, design de sistemas, boundaries, dependências, contratos ou decisões estruturais.
---

# Instruções de Arquitetura

Aplique estas instruções quando a alteração envolver decisões estruturais,
design de componentes, integração entre sistemas ou evolução da arquitetura.

Não crie alterações arquiteturais apenas porque estas instruções estão
disponíveis.

## Princípios

Prefira:

- simplicidade;
- alta coesão;
- baixo acoplamento;
- responsabilidades explícitas;
- dependências direcionadas conscientemente;
- contratos estáveis;
- evolução incremental;
- componentes substituíveis;
- decisões reversíveis quando possível.

A arquitetura deve atender aos requisitos atuais sem impedir evolução
razoável.

Não projete antecipadamente para cenários hipotéticos sem evidência.

---

## Existing Architecture First

Antes de propor mudança estrutural:

1. identifique a arquitetura existente;
2. identifique module boundaries;
3. identifique dependências;
4. identifique padrões utilizados;
5. verifique ADRs;
6. determine se o requisito pode ser atendido pelo design existente.

Preserve decisões existentes quando continuarem válidas.

---

## Boundaries

Cada componente deve possuir responsabilidade clara.

Evite:

- shared modules sem ownership;
- dependências circulares;
- acesso direto entre camadas que viola boundaries;
- business logic espalhada;
- infraestrutura contaminando domínio sem necessidade;
- abstrações que ocultem comportamento importante.

Prefira contracts explícitos entre boundaries relevantes.

---

## Dependency Direction

Dependências devem apontar conscientemente para componentes apropriados.

Business rules não devem depender desnecessariamente de:

- UI;
- transport protocols;
- framework internals;
- database implementation;
- vendor-specific integrations.

Não introduza abstrações artificiais exclusivamente para eliminar qualquer
dependência concreta.

Abstraia quando houver benefício real de:

- substituição;
- testabilidade;
- boundary;
- isolamento de vendor;
- redução de acoplamento.

---

## Data Ownership

Defina ownership dos dados.

Evite múltiplos componentes modificando diretamente o mesmo dado sem regras
claras.

Considere:

- source of truth;
- consistency;
- lifecycle;
- retention;
- concurrency;
- transactions;
- synchronization;
- schema evolution.

---

## Distributed Systems

Não distribua o sistema sem necessidade concreta.

Antes de introduzir comunicação remota, considere o custo adicional de:

- network failures;
- latency;
- retries;
- timeouts;
- partial failures;
- observability;
- deployment;
- versioning;
- data consistency;
- security.

Quando um modular monolith atender aos requisitos, considere-o antes de
microservices.

---

## Contracts

Contracts devem definir, conforme aplicável:

- input;
- output;
- validation;
- error behavior;
- authentication;
- authorization;
- versioning;
- compatibility;
- ownership.

Mudanças incompatíveis devem possuir estratégia explícita de evolução.

---

## Architecture Decisions

Decisões importantes devem registrar:

- context;
- decision;
- alternatives considered;
- consequences;
- risks.

Utilize ADR quando o projeto adotar esse mecanismo.

Evite ADRs para decisões triviais ou facilmente reversíveis.

---

## Observability by Design

Componentes operacionalmente relevantes devem permitir compreender:

- health;
- failures;
- latency;
- throughput;
- dependency behavior.

Não adicione telemetria indiscriminadamente.

Instrumente boundaries e operações relevantes.

---

## Resultado

Uma proposta arquitetural deve explicar:

1. problema;
2. arquitetura atual relevante;
3. mudança proposta;
4. responsabilidades;
5. contracts;
6. data flow;
7. security implications;
8. operational implications;
9. trade-offs;
10. migration strategy quando necessária.