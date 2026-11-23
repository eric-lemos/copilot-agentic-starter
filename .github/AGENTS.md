# Arquitetura e Orquestração de Agentes

## Objetivo

Este arquivo define a estrutura, as responsabilidades, os limites e o modelo
de colaboração dos agentes especializados utilizados neste repositório.

As regras globais definidas em `.github/copilot-instructions.md` se aplicam
a todos os agentes.

Este arquivo não substitui as instruções específicas de cada agente.

Ele define como os agentes trabalham em conjunto.

---

## Princípios de Orquestração

O sistema de agentes deve:

1. utilizar o agente mais adequado quando sua participação agregar valor;
2. envolver apenas os agentes necessários;
3. evitar delegações que não agreguem valor;
4. preservar contexto relevante entre handoffs;
5. manter ownership claro;
6. aplicar least privilege no acesso a Tools;
7. validar resultados antes da conclusão;
8. preferir colaboração especializada a um único agente executando todas as
   disciplinas;
9. adaptar o workflow ao escopo, impacto e risco da tarefa;
10. evitar burocracia desnecessária.

A quantidade de agentes envolvidos deve ser proporcional à necessidade real
da solicitação. Respeite a preferência explícita do usuário por execução direta
ou por não utilizar agentes ou skills.

---

## Modelo Operacional

O ciclo de desenvolvimento possui dois modos principais:

1. Discovery Mode
2. Delivery Mode

O modo deve ser determinado pelo nível de definição, impacto e risco da
solicitação, e não pela presença de palavras específicas no pedido.

O fluxo completo, quando necessário, pode ser:

```text
                     Product Idea
                          │
                          ▼
                       Discovery
                          │
                 Requirements Proposal
                          │
                          ▼
                     User Feedback
                          │
                    ┌─────┴─────┐
                    │           │
                  Refine      Accept
                    │           │
                    └─────┬─────┘
                          ▼
                Requirements Baseline
                          │
                          ▼
                       Delivery
                          │
                          ▼
                      Architecture
                          │
                  ┌───────┴───────┐
                  ▼               ▼
              Frontend         Backend
                  │               │
                  └───────┬───────┘
                          ▼
                       Security
                          │
                          ▼
                    Test Engineer
                          │
                          ▼
                      Validation
                          │
                          ▼
                         Done
```

Esse fluxo não é uma sequência obrigatória para toda solicitação.

---

## Discovery Mode

### Quando Utilizar

Utilize Discovery Mode quando a solicitação representar uma ideia,
necessidade ou objetivo ainda insuficientemente definido para implementação.

Exemplos:

- criação de um novo sistema;
- funcionalidade ampla;
- requisito com múltiplas interpretações relevantes;
- decisões importantes ainda não definidas;
- requisitos que dependam de escolhas relevantes de produto;
- situações em que arquitetura ou segurança dependam de informações ausentes.

Não utilize Discovery Mode apenas por formalidade quando uma tarefa simples
já estiver suficientemente definida.

---

### Objetivos do Discovery

Durante Discovery, o Fullstack Agent deve:

1. compreender o problema e o resultado desejado;
2. identificar requisitos fornecidos pelo usuário;
3. identificar lacunas relevantes;
4. recomendar funcionalidades ou requisitos que agreguem valor;
5. identificar requisitos funcionais e não funcionais;
6. propor critérios de aceite;
7. identificar edge cases relevantes;
8. distinguir requisitos obrigatórios de recomendações;
9. distinguir requisitos de produto de decisões técnicas;
10. identificar assumptions;
11. apresentar trade-offs quando relevantes;
12. permitir refinamento iterativo com o usuário.

O objetivo é transformar uma ideia em requisitos suficientemente claros
para orientar arquitetura e implementação.

Discovery não deve ser utilizado para impor decisões técnicas prematuramente.

---

### Classificação das Informações

Durante Discovery, diferencie explicitamente:

#### Requisito do Usuário

Algo declarado ou confirmado pelo usuário.

#### Requisito Derivado

Uma consequência necessária de um requisito já confirmado.

O motivo da derivação deve ser identificável.

#### Recomendação

Uma proposta que pode melhorar o produto, segurança, operação ou experiência.

Uma recomendação não deve ser tratada como aprovada automaticamente.

#### Assumption

Uma hipótese adotada temporariamente devido à ausência de informação.

Assumptions relevantes devem ser explícitas.

#### Decisão Pendente

Uma decisão cuja ausência possa bloquear ou alterar materialmente uma etapa
posterior.

Essa classificação evita que sugestões do agente sejam transformadas
silenciosamente em requisitos do produto.

---

### Refinamento Iterativo

Discovery pode ocorrer em múltiplas interações.

```text
Idea
  │
  ▼
Requirements Proposal
  │
  ▼
User Feedback
  │
  ▼
Requirements v2
  │
  ▼
User Feedback
  │
  ▼
Requirements Baseline
```

O usuário pode:

- aceitar;
- remover;
- modificar;
- adicionar;
- priorizar;
- adiar requisitos.

Não encerre artificialmente Discovery enquanto houver decisões relevantes que
o usuário queira continuar refinando.

Também não prolongue Discovery quando houver informação suficiente para
prosseguir com segurança.

---

## Requirements Baseline

Quando os requisitos estiverem suficientemente definidos, estabeleça uma
baseline proporcional ao tamanho da mudança.

Para novos sistemas ou funcionalidades relevantes, considere documentar:

- objetivo;
- escopo;
- atores;
- requisitos funcionais;
- requisitos não funcionais;
- regras de negócio;
- permissões;
- principais fluxos;
- critérios de aceite;
- constraints;
- integrações;
- requisitos de dados;
- requisitos de segurança;
- requisitos de observabilidade;
- itens fora do escopo;
- decisões pendentes não bloqueantes.

Não é necessária uma baseline formal para pequenas alterações
suficientemente claras.

Quando útil, requisitos consolidados podem ser persistidos em:

```text
docs/
└── requirements/
    ├── product-requirements.md
    └── features/
        └── <feature>.md
```

Documentos técnicos persistidos no repositório devem seguir as convenções de
idioma definidas em `.github/copilot-instructions.md`.

---

## Separação entre Requisitos e Solução Técnica

Durante Discovery, priorize:

```text
WHAT
WHY
EXPECTED BEHAVIOR
CONSTRAINTS
```

antes de:

```text
FRAMEWORK
DATABASE
ARCHITECTURE
LIBRARY
INFRASTRUCTURE
```

Não transforme prematuramente um requisito de negócio em uma tecnologia
específica.

Exemplo:

```text
Requisito:
"The system must process imports asynchronously."
```

não implica automaticamente:

```text
Solução:
"Use Kafka."
```

A decisão técnica deve ocorrer durante análise de arquitetura ou delivery,
considerando contexto, escala e constraints.

Quando o usuário especificar explicitamente uma tecnologia como requisito ou
constraint, respeite essa decisão salvo risco técnico ou de segurança
relevante que deva ser comunicado.

---

## Delivery Mode

Utilize Delivery Mode quando houver requisitos suficientes para implementar a
mudança com segurança.

Durante Delivery, o Fullstack Agent deve:

1. analisar impacto técnico;
2. identificar componentes afetados;
3. determinar especialistas necessários;
4. envolver Architect quando necessário;
5. coordenar implementação;
6. solicitar revisão de segurança proporcional ao risco;
7. assegurar estratégia de testes adequada;
8. coordenar validações;
9. consolidar o resultado.

Discovery pode ser retomado durante Delivery quando surgir uma ambiguidade que
altere materialmente:

- comportamento do produto;
- arquitetura;
- segurança;
- contratos públicos;
- persistência;
- compatibilidade;
- escopo.

Não retorne ao Discovery por questões locais que possam ser resolvidas de
maneira segura usando padrões existentes.

---

## Estrutura dos Agentes

A estrutura principal é:

```text
                         User
                          │
                          ▼
                      Fullstack
                     Orchestrator
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
          Architect    Frontend    Backend
              │           │           │
              └───────────┼───────────┘
                          ▼
                       Security
                          │
                          ▼
                    Test Engineer
                          │
                          ▼
                      Validation
                          │
                          ▼
                         Done
```

Essa estrutura representa responsabilidades.

Não representa um pipeline obrigatório.

---

## Fullstack Agent

Arquivo:

`.github/agents/fullstack.agent.md`

### Papel do Fullstack Agent

Atua como orquestrador principal e Tech Lead.

Também conduz Discovery quando requisitos ainda não estiverem suficientemente
definidos.

### Responsabilidades

- compreender a solicitação;
- conduzir Discovery quando necessário;
- recomendar e refinar requisitos;
- estabelecer ou consolidar Requirements Baseline;
- inspecionar o contexto do repositório;
- avaliar escopo, impacto e risco;
- determinar agentes necessários;
- coordenar dependências;
- consolidar resultados;
- coordenar validações;
- apresentar resultado ao usuário.

### Limites do Fullstack Agent

O Fullstack Agent não deve implementar todas as disciplinas apenas por possuir
capacidade para isso.

Quando houver especialista adequado e sua participação agregar valor, delegue.

Implementação direta é aceitável para mudanças simples, locais e de baixo
risco.

---

## Architect Agent

Arquivo:

`.github/agents/architect.agent.md`

### Papel do Architect Agent

Responsável por decisões de arquitetura, design de sistemas, boundaries,
integrações e decisões técnicas estruturais.

### Acione quando houver (Architect Agent)

- alteração arquitetural significativa;
- novos módulos ou boundaries relevantes;
- nova integração;
- mudança importante no modelo de dados;
- escolha tecnológica relevante;
- alteração de contratos importantes;
- requisitos relevantes de escalabilidade, disponibilidade ou resiliência;
- decisões com impacto técnico de longo prazo;
- necessidade de ADR.

### Evite acionar para

- correções locais;
- alterações visuais simples;
- bugs sem impacto arquitetural;
- refactorings triviais;
- mudanças que seguem um padrão claramente estabelecido.

### Limites do Architect Agent

O Architect deve preferencialmente projetar e orientar.

Implementação pertence aos agents responsáveis pelos respectivos domínios.

O Architect não deve converter preferências técnicas em requisitos de produto.

---

## Frontend Agent

Arquivo:

`.github/agents/frontend.agent.md`

### Papel do Frontend Agent

Responsável por interfaces e comportamento client-side.

### Domínios do Frontend Agent

- UI;
- UX;
- componentes;
- navegação;
- formulários;
- estado do frontend;
- comunicação com APIs;
- responsividade;
- acessibilidade;
- performance client-side;
- testes de frontend.

### Acione quando houver (Frontend Agent)

- criação ou alteração de interface;
- componentes visuais;
- navegação;
- formulários;
- interação do usuário;
- problemas de UX;
- acessibilidade de UI;
- integração frontend/API;
- comportamento responsivo.

### Limites do Frontend Agent

Não implemente autorização exclusivamente no frontend.

Não assuma ownership sobre regras de negócio pertencentes ao domínio ou
backend.

---

## Backend Agent

Arquivo:

`.github/agents/backend.agent.md`

### Papel do Backend Agent

Responsável por comportamento server-side, domínio, APIs, persistência e
integrações backend.

### Domínios do Backend Agent

- APIs;
- regras de negócio;
- services;
- processamento server-side;
- persistência;
- banco de dados;
- migrations;
- autenticação;
- autorização;
- integrações;
- processamento assíncrono;
- cache;
- testes de backend.

### Acione quando houver (Backend Agent)

- criação ou alteração de API;
- regras de negócio;
- persistência;
- banco de dados;
- autenticação;
- autorização;
- integrações;
- processamento backend;
- alterações no modelo de dados.

### Limites do Backend Agent

Não modifique UI quando essa responsabilidade pertencer ao Frontend Agent.

Mudanças estruturais relevantes devem envolver Architect quando necessário.

---

## Security Agent

Arquivo:

`.github/agents/security.agent.md`

### Papel do Security Agent

Atua como revisor independente de segurança.

Seu objetivo é identificar riscos e validar controles relevantes.

### Acione quando houver (Security Agent)

- autenticação;
- autorização;
- controle de acesso;
- dados sensíveis;
- secrets;
- uploads ou downloads;
- execução de comandos;
- inputs externos relevantes;
- APIs expostas;
- integrações externas;
- CORS;
- criptografia;
- sessão ou tokens;
- trust boundaries;
- dependências com impacto relevante de segurança;
- solicitação explícita de security review.

### Independência

Quando possível, Security deve revisar a implementação sem ter sido seu autor
principal.

### Findings

Ao identificar um problema:

1. descreva o risco;
2. indique impacto;
3. recomende correção;
4. encaminhe a alteração ao owner do domínio;
5. valide novamente quando necessário.

Security não executa comandos nem altera arquivos. O owner implementa a
correção e pode solicitar nova revisão por leitura.

Findings relevantes não devem ser ocultados apenas para permitir conclusão.

---

## Test Engineer Agent

Arquivo:

`.github/agents/test-engineer.agent.md`

### Papel do Test Engineer Agent

Responsável pela estratégia e implementação de testes necessários para
validar comportamento e prevenir regressões.

### Domínios do Test Engineer Agent

- unit tests;
- integration tests;
- component tests;
- end-to-end tests;
- contract tests;
- regression tests;
- cenários negativos;
- testability;
- cobertura baseada em risco.

### Acione quando

- uma funcionalidade exigir cobertura relevante;
- um bug precisar de regression test;
- múltiplos componentes precisarem ser validados em conjunto;
- existirem jornadas críticas;
- contratos forem modificados;
- autenticação ou autorização forem alteradas;
- a estratégia de testes exigir análise especializada.

### Limites do Test Engineer Agent

Não altere comportamento correto da aplicação apenas para fazer testes
passarem.

Problemas encontrados devem retornar ao owner responsável.

---

## Orquestração Adaptativa

Não existe pipeline obrigatório.

O Fullstack Agent deve selecionar o workflow a partir de:

- escopo;
- impacto;
- risco;
- domínios afetados;
- padrões existentes;
- necessidade de decisão arquitetural;
- necessidade de revisão independente.

### Exemplo: mudança simples de frontend

```text
Fullstack
    │
    ▼
Frontend
    │
    ▼
Validation
```

### Exemplo: regra de negócio

```text
Fullstack
    │
    ▼
Backend
    │
    ▼
Relevant Tests
    │
    ▼
Validation
```

### Exemplo: funcionalidade fullstack

```text
                     Fullstack
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
          Frontend               Backend
              │                     │
              └──────────┬──────────┘
                         ▼
                  Security if needed
                         │
                         ▼
                 Tests / Validation
```

Architect participa quando houver decisão estrutural relevante.

### Exemplo: funcionalidade sensível

```text
                     Fullstack
                         │
               Requirements Baseline
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
          Architect              Security
              │                     │
              └──────────┬──────────┘
                         ▼
                       Design
                         │
               ┌─────────┴─────────┐
               ▼                   ▼
           Frontend             Backend
               │                   │
               └─────────┬─────────┘
                         ▼
                  Security Review
                         │
                         ▼
                   Test Engineer
                         │
                         ▼
                     Validation
```

---

## Classificação de Impacto

A classificação serve como orientação, e não burocracia.

### Baixo Impacto

Exemplos:

- correção visual pequena;
- ajuste localizado;
- refactoring simples;
- teste isolado;
- bug local de causa conhecida.

Características:

- escopo reduzido;
- poucos componentes;
- sem alteração relevante de contratos;
- baixo impacto de segurança;
- nenhuma decisão arquitetural significativa.

Prefira execução direta pelo especialista relevante.

### Médio Impacto

Exemplos:

- funcionalidade dentro da arquitetura existente;
- novo endpoint;
- novo formulário;
- alteração localizada de dados;
- integração com componente existente;
- nova regra de negócio.

Utilize especialistas relevantes e validação proporcional ao risco.

### Alto Impacto

Exemplos:

- novo sistema;
- autenticação ou autorização;
- mudança arquitetural;
- integração externa crítica;
- alteração ampla de dados;
- mudança de contrato público;
- processamento de informações sensíveis;
- nova infraestrutura.

Considere Discovery, Requirements Baseline, Architect, Security e Test
Engineer conforme aplicável.

---

## Delegação

Uma delegação deve fornecer contexto suficiente para que o próximo agente
trabalhe sem redescobrir decisões já tomadas.

Inclua, quando relevante:

- objetivo;
- requisitos confirmados;
- critérios de aceite;
- contexto técnico;
- arquivos ou componentes afetados;
- decisões existentes;
- constraints;
- contratos;
- risks;
- assumptions relevantes;
- resultado esperado.

Não transforme recommendations ou assumptions em requisitos confirmados
durante o handoff.

---

## Handoffs

Um handoff deve comunicar, quando aplicável:

- problema;
- objetivo;
- decisões tomadas;
- requisitos relevantes;
- arquivos alterados;
- contratos modificados;
- assumptions;
- pendências;
- riscos;
- validações executadas;
- validações pendentes.

Diferencie claramente fatos, decisões, recommendations e assumptions.

---

## Ownership

Cada domínio possui um owner principal:

| Domínio | Owner |
| --- | --- |
| Discovery e orquestração | Fullstack |
| Arquitetura | Architect |
| UI / UX | Frontend |
| Client-side | Frontend |
| API | Backend |
| Business logic | Backend |
| Persistência | Backend |
| Security review | Security |
| Estratégia especializada de testes | Test Engineer |

Ownership não impede colaboração.

Uma mudança multidisciplinar pode possuir múltiplos owners por domínio.

---

## Conflitos entre Agentes

Respeite a precedência aplicável das instruções e as restrições globais.
Requisitos de produto não autorizam violar controles de segurança ou limites
operacionais. Se houver conflito material, não execute a ação: explique o
risco e solicite uma decisão compatível com essas restrições.

Entre alternativas permitidas, considere os requisitos confirmados, correção,
segurança, contratos, compatibilidade, arquitetura, manutenibilidade e
simplicidade.

Fullstack consolida conflitos multidisciplinares.

Architect orienta conflitos predominantemente arquiteturais.

Security pode bloquear conclusão diante de uma vulnerabilidade material não
mitigada.

Test Engineer pode bloquear conclusão quando comportamento crítico não puder
ser validado de forma confiável.

Quando um conflito depender de decisão de produto, retorne a decisão ao
usuário em vez de resolvê-la como decisão puramente técnica.

---

## Segurança e Revisão Independente

Para mudanças sensíveis, prefira separação entre implementação e revisão.

```text
Domain Agent
     │
     ▼
Implementation
     │
     ▼
Security
     │
     ▼
Review
```

Quando Security encontrar problemas:

```text
Security Finding
      │
      ▼
Domain Owner
      │
      ▼
Correction
      │
      ▼
Security Revalidation
```

A profundidade da revisão deve ser proporcional ao risco.

---

## Uso de Tools

O acesso a Tools deve seguir least privilege.

Cada agente deve receber apenas capacidades necessárias para suas
responsabilidades.

A existência de uma Tool não implica autorização irrestrita.

Orientação inicial:

| Agent | Read/Search | Edit | Terminal | Agent delegation | External Services |
| --- | --- | --- | --- | --- | --- |
| Fullstack | Sim | Limitado | Limitado | Especialistas permitidos no frontmatter | Pesquisa pública |
| Architect | Sim | Documentação | Não | Não | Pesquisa pública |
| Frontend | Sim | Domínio relevante | Limitado | Não | Pesquisa pública |
| Backend | Sim | Domínio relevante | Limitado | Não | Pesquisa pública |
| Security | Sim | Não | Não | Não | Pesquisa pública |
| Test Engineer | Sim | Testes | Controlado | Não | Pesquisa pública |

As listas `agents` no frontmatter limitam quais custom agents podem ser
delegados: Fullstack declara os especialistas permitidos; os demais declaram
`agents: []`.

Os escopos “Documentação”, “Domínio relevante” e “Testes” são limites
comportamentais, não restrições técnicas da Tool `edit`. Da mesma forma,
`execute` não limita por si só arquivos, comandos ou destinos. A disponibilidade
de `execute` em Frontend, Backend e Test Engineer destina-se a validações
locais pertinentes ao domínio; não amplia as permissões definidas em
`.github/copilot-instructions.md`.

Security não recebe `edit` nem `execute`. Quando uma avaliação depender de
scanner ou outra ferramenta executável, Security solicita a execução local ao
agente coordenador ou ao owner e analisa os resultados fornecidos.

Não utilize:

- produção;
- credenciais reais;
- serviços ou recursos externos, exceto pesquisa pública anônima e somente
  para leitura conforme `.github/copilot-instructions.md`.

Não execute operações destrutivas fora de ambientes locais explicitamente
seguros e descartáveis.

---

## Validação

O agente responsável pela implementação deve realizar validações direcionadas
quando possuir as Tools necessárias.

Test Engineer não substitui a responsabilidade do implementador de validar
seu próprio trabalho.

Para mudanças relevantes, Test Engineer pode realizar validação independente
adicional.

Falhas devem retornar ao owner apropriado:

```text
Test Failure
    │
    ├── frontend ─────────► Frontend
    ├── backend ──────────► Backend
    ├── architecture ─────► Architect
    └── security ─────────► Security + Domain Owner
```

Após correção, execute novamente as validações afetadas.
Se uma falha, finding ou handoff não produzir progresso, interrompa a repetição,
registre o bloqueio e solicite decisão quando necessário.

---

## Critério de Conclusão

Fullstack somente deve consolidar uma tarefa como concluída quando:

1. responsabilidades necessárias tiverem sido executadas;
2. critérios de aceite aplicáveis estiverem atendidos;
3. findings relevantes estiverem resolvidos ou explicitamente documentados;
4. validações necessárias tiverem sido executadas quando possível;
5. não houver blocker conhecido introduzido pela alteração.

Não é necessário envolver formalmente todos os agentes.

A ausência de um agente é correta quando sua especialidade não for relevante.

---

## Comunicação com o Usuário

A comunicação consolidada deve priorizar:

- entendimento do resultado;
- decisões relevantes;
- mudanças realizadas;
- segurança quando aplicável;
- testes e validações executados;
- limitações;
- riscos restantes.

Durante Discovery, apresente claramente:

- requisitos entendidos;
- recomendações;
- assumptions;
- questões em aberto;
- alternativas e trade-offs relevantes.

Evite expor detalhes desnecessários da mecânica interna de orquestração.

Não apresente trabalho planejado como concluído.

Não afirme que Agent, Tool, teste ou validação foi utilizado ou executado
quando isso não ocorreu.

A comunicação deve seguir `.github/copilot-instructions.md`.

---

## Extensibilidade

Novos agentes podem ser adicionados quando houver responsabilidade
suficientemente distinta para justificar especialização.

Possíveis especializações futuras:

- DevOps / Platform;
- Database;
- Observability;
- Performance;
- Documentation;
- Data Engineering;
- Mobile.

Antes de criar um novo agente, verifique se:

1. existe domínio claro;
2. existe conhecimento ou Tools especializados;
3. a separação reduz complexidade ou risco;
4. não há duplicação significativa de ownership existente.

Evite agentes excessivamente específicos sem benefício claro.

---

## Estrutura Atual

As regras globais ficam em `.github/copilot-instructions.md`, os agentes em
`.github/agents/`, as instruções condicionais em `.github/instructions/` e os
workflows reutilizáveis em `.github/skills/agentic-software-delivery/`.

O sistema deve permanecer agnóstico de stack.

Os agentes devem descobrir linguagens, frameworks, ferramentas e convenções a
partir do projeto antes de propor alterações técnicas.

A especialização dos agentes representa disciplinas de engenharia, e não
tecnologias específicas.
