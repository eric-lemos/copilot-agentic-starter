---
description: Use ao implementar backend e persistência com as stacks identificadas no projeto.
applyTo: "**/*.{py,pyi,go,js,jsx,mjs,cjs,ts,tsx,mts,cts,java,cs,php,rb,erb,sql}"
---

# Instruções para Stacks de Backend

Estas orientações se aplicam a código server-side. Siga também
`.github/instructions/backend.instructions.md` e as instruções de segurança.

Identifique linguagem, runtime, versões suportadas, dependências e convenções
da aplicação afetada antes de escolher uma seção. Uma extensão de arquivo não
determina, por si só, se o código é backend ou qual runtime é utilizado.
Em projetos com várias aplicações, aplique apenas as orientações pertinentes a
cada uma. Não presuma framework, biblioteca ou banco de dados e não imponha
uma migração de stack ou versão.

## Python

- Preserve a compatibilidade com as versões suportadas e siga as convenções de
  imports, tipagem, dependências e ferramentas existentes.
- Trate exceções no limite adequado e preserve contexto; não oculte falhas
  inesperadas. Use context managers para recursos quando apropriado.
- Em fluxos assíncronos, evite operações bloqueantes no event loop e use os
  mecanismos de concorrência e cancelamento adotados pelo projeto.
- Não deserialize dados não confiáveis com mecanismos inseguros, como `pickle`.

### FastAPI

- Siga os padrões de validação, dependências e tratamento de erros existentes;
  mantenha contratos de resposta explícitos e proteja campos sensíveis.
- Respeite os limites entre operações síncronas e assíncronas da aplicação.

### Django

- Preserve os mecanismos existentes de autenticação, autorização e proteção
  CSRF quando aplicáveis; use migrations para mudanças de schema.
- Considere limites de consulta e transações ao usar o ORM, sem expor objetos
  ou campos não autorizados.

### Flask

- Siga os padrões existentes de rotas, extensões, validação e error handlers.
- Respeite os contextos de aplicação e requisição; não suponha que validação
  ou autorização ocorram automaticamente.

## Go

- Siga as versões, módulos, organização de packages e ferramentas do projeto;
  mantenha a formatação idiomática com `gofmt`.
- Trate erros explicitamente e preserve sua causa quando necessário, sem expor
  detalhes internos ao consumidor externo.
- Propague `context.Context` nas operações que precisam de cancelamento ou
  deadlines, conforme os contratos existentes.
- Garanta que goroutines, conexões e outros recursos tenham ciclo de vida e
  encerramento definidos; trate erros de fechamento quando relevantes.

### `net/http`

- Siga a configuração existente de servidores e clientes HTTP, considerando
  timeouts, cancelamento e limites de leitura quando aplicáveis.
- Feche recursos de resposta quando necessário e trate erros sem expor detalhes
  internos.

### Gin e Echo

- Siga a versão e os padrões de rotas, middleware, binding e erros do projeto.
- Valide inputs e autorização no server-side; respeite o ciclo de vida dos
  contextos de requisição ao usar concorrência.

## Node.js

- Identifique a versão de Node.js, o sistema de módulos, o package manager e,
  quando aplicável, a configuração de TypeScript da aplicação.
- Trate rejeições e erros assíncronos no boundary apropriado; evite operações
  bloqueantes no event loop em fluxos de requisição.
- Gerencie o ciclo de vida de conexões, streams e listeners; considere
  backpressure quando processar dados em fluxo.
- Preserve os mecanismos existentes de validação, autorização e tratamento de
  erros, sem expor detalhes internos ou usar input não confiável em comandos.

### Express

- Siga a versão e a ordem de middleware adotadas; encaminhe erros síncronos e
  assíncronos conforme os mecanismos suportados pelo projeto.
- Valide inputs e aplique autorização nas rotas protegidas.

### Fastify

- Siga os padrões existentes de plugins, escopo, schemas e tratamento de erros.
- Quando usar schemas de request e response, mantenha-os alinhados ao contrato
  e evite expor campos sensíveis.

### NestJS

- Preserve os boundaries e padrões existentes de modules, providers e
  controllers, sem mover regras de negócio para o transporte.
- Use os mecanismos de validação e autorização configurados pelo projeto;
  não presuma que DTOs ou guards estejam ativos sem verificá-los.

## Java e Spring Boot

- Siga a versão de Java, o build e as convenções Spring existentes, incluindo
  configuração, dependency injection e tratamento de erros.
- Valide requests e autorize operações no server-side; preserve os limites de
  transação definidos pela aplicação e não exponha detalhes de exceptions.

## C# e ASP.NET Core

- Siga a versão de .NET, a configuração e as convenções existentes de dependency
  injection, endpoints e middleware.
- Preserve a ordem e os controles de autenticação e autorização; trate
  cancelamento e erros conforme os contratos da aplicação.

## PHP e Laravel

- Siga as versões de PHP e Laravel, o gerenciamento de dependências e os
  padrões de rotas, validação e persistência do projeto.
- Proteja campos contra mass assignment indevido, aplique autorização e use
  migrations existentes para alterações de schema.

## Ruby e Ruby on Rails

- Siga as versões de Ruby e Rails e os padrões existentes de controllers,
  models, validação e migrations.
- Restrinja parâmetros e consultas ao escopo autorizado; preserve os controles
  de sessão e CSRF quando aplicáveis.

## Persistência e cache

Use somente os mecanismos já adotados e ambientes locais seguros. Não conecte
a bancos externos nem utilize dados ou credenciais reais para validação.

### PostgreSQL e MySQL

- Use queries parametrizadas ou mecanismos seguros do ORM e respeite o dialeto,
  as versões e as migrations existentes.
- Considere constraints, índices, transações e limites de consulta conforme o
  comportamento e o volume envolvidos.

### MongoDB

- Valide filtros e dados externos, evitando aceitar operadores de consulta
  arbitrários de clientes.
- Considere índices, limites e atomicidade; use transações somente quando
  necessárias e compatíveis com a configuração existente.

### Redis

- Identifique se o uso existente é cache ou possui outra responsabilidade;
  não presuma persistência, consistência ou disponibilidade.
- Defina expiração e invalidação quando apropriado; não use cache como
  substituto da autorização server-side nem registre dados sensíveis.

## Performance e qualidade de backend

- Quando a alteração puder afetar performance, compare antes e depois com as
  ferramentas disponíveis, cargas limitadas e dados sintéticos em ambiente
  local seguro. Mantenha condições equivalentes e registre contexto,
  resultados e limitações.
- Conforme o fluxo, avalie latência, throughput, erros e uso de recursos;
  considere percentis quando houver amostras suficientes. Não extrapole
  resultados locais para produção.
- Investigue gargalos observados em consultas, índices, chamadas repetidas,
  serialização, concorrência e acesso a dependências. Aplique otimizações
  proporcionais à evidência e verifique seu impacto e possíveis regressões.
- Investigue consultas N+1, limites e paginação; avalie planos de consulta e
  índices em ambiente local seguro. Considere o custo de escrita e use o
  mecanismo de migration existente quando alterar índices.
- Se houver cache, avalie expiração, invalidação e consistência. Isole chaves
  por tenant e escopo relevantes e mantenha autorização server-side antes de
  fornecer dados armazenados.
- Reutilize conexões conforme a stack e dimensione pools e concorrência com
  base em medições; limite trabalho simultâneo e preserve timeouts,
  cancelamento e liberação de recursos.
- Reduza processamento e dados desnecessários sem alterar contratos públicos.
  Avalie compressão de respostas apenas quando houver benefício, considerando
  CPU, compatibilidade e riscos ao combinar secrets com input não confiável.
- Ao medir, registre volume de dados, carga, duração e condições do teste;
  compare latência, throughput, erros e recursos com a mesma configuração.
  Repita medições quando necessário e não afirme ganhos não observados.
- Valide contratos, entradas inválidas, autorização, erros e limites relevantes
  ao comportamento alterado. Considere cancelamento, concorrência e falhas de
  dependências quando aplicáveis, usando testes existentes ou testes focados.
- Use apenas recursos locais seguros e descartáveis, sem produção, bancos
  externos, credenciais reais ou dados sensíveis. Não introduza cache,
  instrumentação, serviços ou dependências apenas para melhorar uma métrica.
  Informe validações que não puderem ser executadas.
