# Copilot Agentic Starter

Conjunto agnóstico de stack com instruções do GitHub Copilot, agentes
especializados e workflows de desenvolvimento de software.

Este repositório fornece orientações para agentes; por si só, não implementa
uma aplicação de produto nem determina uma stack de aplicação. Os agentes devem
inspecionar o projeto-alvo antes de tomar decisões sobre linguagem, framework,
banco de dados, build, deployment ou runtime.

## Estrutura do repositório

A configuração agentic fica em `.github/`:

- `copilot-instructions.md` define as regras de engenharia globais do workspace.
- `AGENTS.md` define a orquestração, o ownership, os modos de trabalho e a
  colaboração.
- `agents/` contém os perfis dos agentes especializados e suas capacidades
  declaradas.
- `instructions/` contém instruções por domínio, aplicadas conforme padrões de
  arquivos ou a tarefa relevante.
- `skills/` contém workflows reutilizáveis.

### Agentes especializados

| Agente | Responsabilidade principal | Limite importante |
| --- | --- | --- |
| `fullstack` | Orquestra o trabalho e conduz discovery quando necessário. | Não assume por padrão a implementação de todos os especialistas. |
| `architect` | Design de sistemas, boundaries, contratos e decisões estruturais. | Principalmente orienta e documenta; agentes de domínio implementam suas áreas. |
| `frontend` | Interface, comportamento client-side, acessibilidade e testes de frontend. | Controles visuais não substituem autorização server-side confiável. |
| `backend` | APIs, regras de negócio, persistência, autenticação, autorização, integrações e testes de backend. | Segue a stack e os contratos existentes. |
| `security` | Revisão independente de segurança e análise de ameaças, somente por leitura. | Não edita arquivos nem executa comandos; encaminha correções ao owner do domínio. |
| `test-engineer` | Estratégia de testes baseada em risco, implementação de testes e validação independente. | Não altera comportamento correto do produto apenas para satisfazer um teste. |

O ownership dos agentes é uma convenção de coordenação, não um motivo para
bloquear colaboração útil. Os metadados `agents` e `tools` nos perfis declaram
capacidades pretendidas; não substituem políticas do workspace nem concedem
permissão para operações que seriam proibidas.

### Instruções por domínio

Os arquivos em `.github/instructions/` cobrem arquitetura, backend, qualidade
de código, frontend, acessibilidade, segurança, testes e DevOps. As instruções
de frontend, acessibilidade, testes e DevOps declaram padrões `applyTo`; as
demais são selecionadas conforme o trabalho. Esses documentos complementam,
mas não substituem, as regras globais e o modelo de orquestração.

## Modelo operacional

O sistema possui dois modos adaptativos, selecionados conforme o nível de
definição, impacto e risco da solicitação. Eles não são etapas obrigatórias
para todas as tarefas.

### Discovery

Use discovery quando requisitos ou decisões importantes não estiverem claros.
Antes de implementar, esclareça o resultado desejado, os atores, as restrições,
o comportamento, os riscos e os critérios de aceite quando as lacunas puderem
afetar materialmente o produto, a arquitetura, a segurança, os dados, os
contratos, a compatibilidade, o custo ou a operação.

Mantenha distintas estas categorias:

- **Requisitos do usuário**: declarados ou confirmados explicitamente.
- **Requisitos derivados**: consequências necessárias dos requisitos confirmados.
- **Recomendações**: propostas ainda não aprovadas como requisitos.
- **Assumptions**: hipóteses temporárias adotadas por falta de informação.
- **Decisões em aberto**: escolhas pendentes que podem afetar o trabalho seguinte.

Para trabalhos substanciais, uma baseline de requisitos pode registrar escopo,
atores, requisitos funcionais e não funcionais, regras de negócio, critérios de
aceite, restrições, integrações, segurança, dados e itens fora do escopo. Não
imponha uma baseline formal a uma mudança pequena e clara.

### Delivery

Quando os requisitos estiverem suficientemente claros, inspecione o contexto
relevante do projeto, identifique componentes afetados e riscos, selecione
apenas os especialistas necessários, implemente e execute validações
proporcionais. Retorne ao discovery somente se surgir uma ambiguidade material.

Um fluxo típico pode incluir arquitetura, frontend, backend, revisão de
segurança, testes e validação, mas não é uma sequência fixa nem um checklist.
Trabalhos pequenos e de baixo risco podem ser conduzidos diretamente pelo owner
relevante.

### Delegação e handoffs

Delegue somente quando a participação de um especialista agregar valor e
estiver disponível e autorizada. Forneça contexto suficiente para evitar
redescoberta: objetivo, requisitos confirmados, critérios de aceite, áreas
afetadas, decisões, contratos, restrições, riscos, assumptions e resultados
esperados.

Handoffs devem distinguir fatos, decisões, recomendações, assumptions e
questões pendentes. O owner da implementação continua responsável por validar
suas alterações; testes independentes complementam, mas não substituem essa
responsabilidade. Findings de segurança retornam ao owner do domínio para
correção e revalidação.

## Princípios de engenharia e segurança

- Inspecione o projeto antes de presumir stack, arquitetura, ferramentas ou
  convenções.
- Prefira mudanças incrementais e focadas e reutilize padrões estabelecidos.
- Priorize correção e segurança, seguidas por manutenibilidade, testabilidade,
  acessibilidade, confiabilidade, performance, observabilidade e experiência de
  desenvolvimento.
- Trate inputs externos e respostas de integrações como não confiáveis; aplique
  autorização nos limites confiáveis.
- Não exponha nem faça commit de secrets, nem use sistemas de produção ou
  serviços externos quando as regras do workspace os proibirem.
- Use operações locais e reversíveis e validações proporcionais. Não afirme que
  uma ferramenta, agente, teste ou validação foi executado sem que isso tenha
  ocorrido.
- A comunicação com o usuário é em português do Brasil. Esta documentação
  também está em pt-BR; nomes de arquivos, identificadores e termos técnicos
  permanecem conforme as convenções do ecossistema.

As regras globais em `.github/copilot-instructions.md` e as restrições de
segurança aplicáveis valem para todos os agentes. Instruções especializadas
adicionam orientações por domínio, mas não reduzem os requisitos globais.

## Como estender o sistema

Antes de adicionar um agente, confirme que ele possui uma área de ownership
distinta e que essa separação reduz complexidade ou risco de forma relevante.
Especifique seu papel, limites, ferramentas e delegações permitidas no perfil.
Atualize `.github/AGENTS.md` quando o modelo operacional, o ownership ou os
handoffs mudarem.

Adicione ou altere instruções condicionais quando um domínio precisar de
orientações persistentes aplicáveis a um padrão de arquivos ou tipo de trabalho
definido. Adicione uma skill reutilizável quando um workflow repetível trouxer
valor além de uma única tarefa. Evite duplicar regras globais nos especialistas;
referencie e complemente a política compartilhada.

Mantenha este README alinhado à configuração real. Consulte os metadados dos
agentes, os padrões das instruções e os arquivos de workflow relevantes, sem
presumir que diagramas ou exemplos representam um pipeline obrigatório em
runtime.
