---
description: Use ao criar, alterar ou revisar infraestrutura, configuração operacional, containers, CI/CD, deployment ou observabilidade.
applyTo: "**/Dockerfile*,**/Containerfile*,**/{compose,docker-compose}*.{yml,yaml},.github/workflows/**/*.{yml,yaml},**/*.{tf,tfvars,hcl}"
---

# Instruções de DevOps e Operação

Aplique estas instruções a infraestrutura, containers, pipelines,
configuração operacional e deployment.

Não presuma cloud provider, container platform ou CI/CD específico.

## Configuration

Separe configuração do código quando apropriado.

Não inclua secrets em configuração versionada.

Forneça exemplos seguros para variáveis obrigatórias.

Falhe de maneira clara quando configuração essencial estiver ausente.

---

## Containers

Ao trabalhar com containers:

- prefira imagens oficiais ou confiáveis;
- use versões controladas;
- minimize packages desnecessários;
- execute como non-root quando possível;
- mantenha build context pequeno;
- use `.dockerignore`;
- considere multi-stage builds;
- não copie secrets para images;
- não deixe credentials em layers.

Evite `latest` quando reprodutibilidade for importante.

---

## CI/CD

Pipelines devem:

- ser reproduzíveis;
- falhar corretamente;
- possuir steps claros;
- limitar permissions;
- evitar exposição de secrets;
- executar validações relevantes;
- produzir artifacts de forma controlada.

Aplique least privilege aos tokens do pipeline.

Não conceda write permissions sem necessidade.

---

## Dependencies e Builds

Prefira builds reproduzíveis.

Utilize lockfiles quando o ecossistema suportar.

Evite downloads arbitrários sem controle de origem ou integridade.

Não use padrões como:

```text
curl <remote-script> | shell
```

sem necessidade explícita e avaliação de segurança.

---

## Deployment

Considere:

- readiness;
- health;
- rollback;
- backward compatibility;
- migrations;
- configuration;
- graceful shutdown;
- startup behavior;
- dependency availability.

Não confunda process running com application ready.

---

## Health Checks

Health checks devem responder perguntas operacionais claras.

Diferencie quando necessário:

- liveness;
- readiness;
- dependency health.

Evite health checks caros ou que gerem carga excessiva.

Não exponha informações sensíveis.

---

## Logging

Logs devem usar inglês e ser adequados para processamento automatizado quando
o projeto possuir structured logging.

Considere:

- timestamp;
- severity;
- service;
- correlation ID;
- operation;
- relevant context.

Não registre secrets.

---

## Metrics

Instrumente comportamento operacional relevante.

Prefira métricas relacionadas a:

- workload;
- errors;
- latency;
- saturation;
- dependencies.

Evite cardinalidade não controlada.

Não use valores como:

- user ID;
- request ID;
- full URL with dynamic identifiers;

como labels de métricas sem avaliar cardinalidade.

---

## Tracing

Quando distributed tracing estiver disponível:

- preserve trace context;
- instrumente boundaries relevantes;
- evite atributos sensíveis;
- mantenha naming consistente.

Não instrumente cada função indiscriminadamente.

---

## Secrets

Use o mecanismo de secret management apropriado ao ambiente.

Nunca:

- hardcode secrets;
- faça commit de credentials;
- exponha secrets em CI logs;
- inclua secrets em container images;
- copie `.env` real para artifacts.

---

## Infrastructure as Code

Para IaC:

- prefira mudanças pequenas;
- preserve state;
- avalie destruição de recursos;
- revise plans;
- minimize privileges;
- trate mudanças irreversíveis explicitamente.

Não aplique alterações em produção.

---

## Ambientes

Diferencie claramente:

- local;
- development;
- test;
- staging;
- production.

Não utilize produção como ambiente de teste.

Defaults de desenvolvimento não devem enfraquecer produção silenciosamente.

---

## Observabilidade

Para serviços operacionalmente relevantes, considere:

```text
Logs
Metrics
Traces
Health
Alerts
```

Não adicione ferramentas novas quando a plataforma já fornecer mecanismo
adequado.

Siga os padrões de observabilidade existentes no ambiente.