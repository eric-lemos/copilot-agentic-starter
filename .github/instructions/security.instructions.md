---
description: Use ao projetar, implementar ou revisar controles de segurança, autenticação, autorização, input, secrets, dados, APIs, arquivos ou integrações.
---

# Instruções de Segurança

Aplique secure by default, least privilege e defense in depth.

Segurança deve ser considerada durante o desenvolvimento, e não apenas após
a implementação.

## Trust

Considere não confiável todo dado proveniente de:

- usuários;
- browsers;
- APIs;
- files;
- headers;
- cookies;
- queues;
- webhooks;
- databases com dados externos;
- third-party services;
- configuration outside the trust boundary.

Valide no boundary apropriado.

---

## Authentication

Use mecanismos estabelecidos.

Considere:

- credential storage;
- secure password hashing;
- session lifecycle;
- token validation;
- expiration;
- rotation;
- revocation;
- recovery;
- brute-force resistance.

Não desenvolva criptografia própria.

---

## Authorization

Verifique autorização server-side.

Considere:

- resource ownership;
- roles;
- permissions;
- tenants;
- organizations;
- privileged operations;
- state transitions.

Autenticação não concede automaticamente acesso aos recursos.

---

## Injection

Nunca construa comandos usando input não confiável sem mecanismo seguro.

Isso inclui:

- SQL;
- shell commands;
- OS paths;
- LDAP;
- templates;
- dynamic queries.

Use parameterization e APIs seguras.

---

## Browser Security

Considere, quando aplicável:

- XSS;
- CSRF;
- CORS;
- clickjacking;
- CSP;
- open redirects;
- cookie security;
- browser storage.

Não desative escaping ou security headers sem justificativa.

---

## SSRF

Ao permitir URLs ou chamadas externas controladas pelo usuário:

- valide schemes;
- valide destinations;
- restrinja networks quando necessário;
- considere redirects;
- bloqueie acesso indevido a internal services e metadata endpoints.

---

## Files

Uploads devem considerar:

- size;
- extension;
- actual content type;
- storage location;
- filename;
- path traversal;
- execution risk;
- authorization;
- malware scanning quando necessário.

Não confie apenas na extensão declarada pelo cliente.

---

## Secrets

Nunca armazene secrets em:

- source code;
- frontend bundles;
- test fixtures compartilhadas;
- logs;
- documentation;
- example configuration.

Utilize secret management ou configuração segura apropriada ao ambiente.

---

## Logging

Não registre:

- passwords;
- access tokens;
- refresh tokens;
- private keys;
- full authorization headers;
- sensitive personal data sem necessidade.

Considere redaction quando valores sensíveis forem necessários para
correlação operacional.

---

## Errors

Não exponha informações que ajudem um atacante a compreender detalhes
internos.

Mantenha detalhes técnicos nos canais internos apropriados.

---

## Dependencies

Antes de introduzir uma dependência, considere:

- maintenance;
- adoption;
- provenance;
- known vulnerabilities;
- transitive dependencies;
- necessity.

Não adicione uma biblioteca para funcionalidades triviais sem necessidade.

---

## Segurança de APIs

Considere:

- object-level authorization;
- function-level authorization;
- resource consumption;
- rate limits;
- mass assignment;
- sensitive field exposure;
- schema validation;
- inventory/versioning;
- unsafe consumption of third-party APIs.

---

## Dados Sensíveis

Colete, armazene e exponha apenas dados necessários.

Considere:

- classification;
- encryption;
- access control;
- retention;
- deletion;
- backup;
- logs;
- exports.

Não copie dados de produção para ambientes de desenvolvimento.

---

## Findings

Não reduza controles de segurança para:

- fazer testes passarem;
- simplificar desenvolvimento;
- contornar configuração;
- acelerar integração.

Quando existir conflito material entre requisito e segurança, torne o
trade-off explícito.