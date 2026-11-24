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
| `devops` | Infraestrutura, CI/CD, containers, IaC, deployment e observabilidade. | Não acessa produção, usa credenciais reais nem altera estado remoto ou compartilhado. |
| `security` | Revisão independente de segurança e análise de ameaças, somente por leitura. | Não edita arquivos nem executa comandos; encaminha correções ao owner do domínio. |
| `testing` | Estratégia de testes baseada em risco, implementação de testes e validação independente. | Não altera comportamento correto do produto apenas para satisfazer um teste. |

O ownership dos agentes é uma convenção de coordenação, não um motivo para
bloquear colaboração útil. Os metadados `agents` e `tools` nos perfis declaram
capacidades pretendidas; não substituem políticas do workspace nem concedem
permissão para operações que seriam proibidas.

Documentações criadas ou atualizadas pelos agentes neste workspace devem ser
escritas em pt-BR, incluindo documentação técnica e ADRs. Código, identificadores
e termos técnicos permanecem em inglês quando essa for a convenção do
ecossistema.

### Instruções por domínio

Os arquivos em `.github/instructions/` cobrem arquitetura, backend, frontend,
direção visual, acessibilidade, segurança, testes e DevOps. As regras gerais
de qualidade de código ficam em `.github/copilot-instructions.md`.
As instruções de estrutura de projeto, stacks de backend e design, frontend,
tecnologias de interface, direção visual, acessibilidade, testes e DevOps
declaram padrões `applyTo`. As demais podem ser consultadas conforme a tarefa.
A descoberta e a inclusão dependem do runtime; esses documentos complementam,
mas não substituem, as regras globais e o modelo de orquestração.
Arquivos JSX e TSX não ativam automaticamente as instruções de stack backend:
quando houver código server-side nesses arquivos, as instruções de tecnologias
de interface orientam a consultar as regras de backend. A inclusão por
referência não é garantida; confira a leitura efetiva na sessão.
As instruções de Design System são ativadas por arquivos de interface; para
JavaScript e TypeScript sem JSX, as instruções de tecnologias de interface
orientam consultá-las quando a tarefa envolver interface ou tema.

As orientações em
[frontend.stacks.instructions.md](.github/instructions/frontend.stacks.instructions.md)
cobrem HTML, CSS, JavaScript, TypeScript, React, Vue, Angular, Svelte, Next.js,
Nuxt, SvelteKit, Astro, Tailwind CSS, Bootstrap, Sass, CSS Modules, Vite, Vitest
e Playwright. Suas seções específicas dependem da stack identificada, não apenas
da extensão do arquivo, e não impõem bibliotecas ou estilos visuais. Elas também
orientam escolha e fidelidade à stack, diagnóstico de performance e validação
de qualidade de interface.

As orientações em
[design.stacks.instructions.md](.github/instructions/design.stacks.instructions.md)
cobrem Material Design, Fluent 2, Carbon, Ant Design e Spectrum, respeitando a
identidade do produto e os termos de cada implementação e asset. Essas opções
devem ser avaliadas prioritariamente nas recomendações, sem constituir uma
lista fechada: a escolha deve considerar o produto e a stack, preservando
sistemas já adotados. Para construir ou alterar interfaces, o fluxo exige um
Design System escolhido e foundations aplicáveis antes da implementação visual;
se não houver escolha, orienta propor alternativas e obter aprovação. A escolha
não impõe uma biblioteca ou migração. Para mudanças visuais relevantes, orienta
identificar implementação, versão, tema e tokens, consultar as fontes pertinentes
e verificar a interface renderizada quando possível. A configuração orienta o
agente, mas não garante cumprimento ou fidelidade visual em runtime.

As orientações em
[backend.stacks.instructions.md](.github/instructions/backend.stacks.instructions.md)
cobrem Python, Go, Node.js, Java, C#, PHP e Ruby, com orientações para seus
frameworks e para PostgreSQL, MySQL, MongoDB e Redis. Elas se aplicam conforme
a stack identificada, orientam escolha e fidelidade à stack, diagnóstico de
performance e qualidade e não impõem frameworks, bibliotecas ou bancos de dados.

As orientações em
[devops.stacks.instructions.md](.github/instructions/devops.stacks.instructions.md)
cobrem GitHub Actions, GitLab CI, Jenkins, Docker, Podman, Kubernetes, Helm,
Terraform, OpenTofu, Ansible, Prometheus, Grafana, OpenTelemetry e Argo CD.
Elas se aplicam às ferramentas identificadas, sem ampliar os limites de execução
local nem exigir serviços externos, e orientam escolha e fidelidade à stack,
diagnóstico de performance e qualidade operacional.

Ao recomendar tecnologias para projetos novos ou existentes, avalie primeiro
as opções documentadas pertinentes e justifique a escolha. A lista não é
fechada: quando as opções não forem adequadas, outra alternativa pode ser
proposta com justificativa. Relacione cada escolha a uma necessidade e avalie
compatibilidade, sem adicionar tecnologias apenas por estarem listadas.
Preserve tecnologias já adotadas e decisões explícitas do usuário; não proponha
migração apenas por uma tecnologia não estar listada. Em projetos novos, as
práticas das seções escolhidas orientam também a configuração inicial, mesmo
sem padrões preexistentes. Os fluxos orientam consultar documentação compatível
com as versões adotadas e relatar fontes e validações, sem presumir
compatibilidade nem substituir testes reais.

As orientações em
[project.structure.instructions.md](.github/instructions/project.structure.instructions.md)
definem uma estrutura-base adaptável para projetos novos e preservam as
convenções de projetos existentes. Novos projetos solicitados devem ser criados
sob `src/`, relativo à raiz do workspace, preferencialmente em `src/frontend/`
ou `src/backend/` conforme a responsabilidade. O nome do projeto não é obrigatório;
preserve a unidade de frameworks fullstack integrados e diferencie aplicações
independentes quando necessário. Cada aplicação mantém sua estrutura interna e
manifests; projetos existentes não são movidos automaticamente.
Incluem referências por tecnologia e regras
para separar assets processados, arquivos públicos, recursos de runtime e
outputs gerados, sem exigir uma árvore única ou diretórios vazios.

Para evitar divergência, use `.github/copilot-instructions.md` como fonte das
regras transversais; `.github/AGENTS.md` para orquestração, ownership e
handoffs; `instructions/` para regras duráveis de domínio; perfis em `agents/`
para papel, capacidades declaradas e limites próprios; e `skills/` para etapas
de workflows reutilizáveis. Preserve instruções de segurança específicas
quando protegerem um boundary distinto, mesmo que reforcem uma regra global.

## Validar a configuração agentica

Execute o validador local com Python 3, sem dependências adicionais:

```powershell
python scripts\validate_agentic_config.py
```

O validador confere o frontmatter dos perfis, os identificadores e referências
de delegação entre agentes, os campos `applyTo`, metadados de interface em
YAML e referências locais encontradas na documentação. Ele valida a sintaxe
básica dos padrões `applyTo`, mas não simula sua interpretação pelo runtime do
VS Code.

Para executar os testes do validador:

```powershell
python -m unittest discover -s tests -p test_validate_agentic_config.py
```

Se novos formatos YAML forem adicionados em `.github/`, registre também como
eles devem ser validados pelo script.

O GitHub Actions executa o validador e seus testes em pull requests e em pushes
para `main`. Consulte o resultado na aba **Actions** do repositório; as falhas
podem ser reproduzidas localmente com os dois comandos acima. A checagem é
estática e não avalia o comportamento dos agentes em sessões do runtime. A
sintaxe dos workflows em `.github/workflows/` é interpretada pelo GitHub
Actions; o validador local não faz validação semântica desses arquivos.

### Avaliar comportamento e consumo

Para comparar uma revisão da configuração com sua baseline, use o mesmo
harness, modelo, ferramentas e permissões, em sessões novas e com cópias
locais equivalentes e descartáveis dos projetos de teste. Repita cada cenário
nas duas configurações, sem incluir as regras no prompt:

| Cenário | Solicitação de teste | Evidência a verificar |
| --- | --- | --- |
| Escolha de tecnologia | Propor uma stack para um projeto novo com requisitos suficientes. | Avaliação das opções documentadas pertinentes, justificativa, trade-offs e distinção entre recomendação e decisão aprovada. |
| Stack existente | Propor uma melhoria em um projeto que usa tecnologia não listada. | Preservação da stack existente e ausência de migração proposta apenas por ela não estar documentada. |
| Interface | Ajustar um formulário TSX de um produto com Design System adotado. | Reuso de componentes e tema, estados, acessibilidade e inspeção visual quando disponível; stack backend não precisa ser carregada para uma mudança exclusivamente client-side. |
| Tema | Ajustar um tema em TypeScript de um produto com Design System adotado. | Consulta às instruções de Design System e fidelidade aos tokens e à versão, mesmo sem ativação automática por extensão. |
| API TypeScript | Ajustar uma rota server-side em TypeScript sem interface. | Aplicação das regras de backend; orientações detalhadas de Design System não precisam ser carregadas. |
| Boundary server-side | Alterar uma ação server-side em TSX que acessa dados protegidos. | Consulta às instruções de backend, autorização server-side, teste relevante e ausência de exposição de dados. |
| Backend | Corrigir uma validação em uma API existente. | Compatibilidade com a stack, teste de regressão e tratamento de entrada e erro. |
| DevOps | Alterar uma etapa local de validação de CI. | Permissões mínimas, validação local e ausência de operações remotas. |

Use dados sintéticos e não execute operações remotas, deployments ou acessos a
produção. Para cada execução, registre resultado, validações, instruções
efetivamente incluídas ou lidas, chamadas de ferramentas e tempo. Quando o
runtime disponibilizar contadores, registre tokens de entrada, saída e cache
separadamente; marque dados indisponíveis em vez de estimá-los por bytes.
Consulte as referências da resposta e os
[Agent Debug Logs do VS Code](https://code.visualstudio.com/docs/agents/agent-troubleshooting/chat-debug-view)
para distinguir descoberta, inclusão e comportamento. Compare pelo menos três
execuções por cenário e configuração, sem tratar uma execução isolada como
prova. Não declare economia ou equivalência de qualidade sem esses resultados.

## Habilitar o sandbox de agentes no VS Code

No VS Code, o sandbox limita o acesso ao sistema de arquivos e à rede de
comandos executados pelo terminal e por seus processos filhos. Ele é
independente das permissões de execução do agente e, por padrão, **não bloqueia
conexões de saída à rede**.

Para habilitá-lo na sessão atual:

1. Abra uma sessão do Copilot Chat.
2. No seletor de permissões da sessão, habilite **Sandboxing for terminal**.
3. Execute `/sandbox policy` no chat para conferir as restrições efetivas.

Para definir o padrão de novas sessões, abra as configurações do VS Code e
defina `chat.agent.sandbox.enabled` como `"on"`. A configuração padrão é
`"off"`; alterar esse valor não muda uma sessão existente que já tenha uma
seleção explícita.

O controle acima se aplica ao harness do Copilot, não configura o sandbox de
sessões Claude ou Codex e não cobre todas as ferramentas do agente. A
disponibilidade depende do sistema operacional e do ambiente onde os comandos
rodam; consulte os pré-requisitos e limitações atualizados na
[documentação oficial de sandbox de agentes do VS Code](https://code.visualstudio.com/docs/agents/run/agent-sandboxing).

### Capacidades declaradas pelos perfis

Os campos `tools` e `agents` dos perfis declaram capacidades e delegações
pretendidas para o agente no VS Code. Eles não são uma política de sandbox e
não provam que uma ferramenta está disponível ou autorizada na sessão atual.
Os controles efetivos dependem do harness, do host de execução, das políticas
da organização e das permissões da sessão.

| Agente | `tools` declaradas | `agents` declarados |
| --- | --- | --- |
| `architect` | `read`, `search`, `edit` | nenhum |
| `backend` | `read`, `search`, `edit`, `execute` | nenhum |
| `devops` | `read`, `search`, `edit`, `execute` | nenhum |
| `frontend` | `read`, `search`, `edit`, `execute` | nenhum |
| `fullstack` | `execute`, `read`, `edit`, `search`, `agent` | `architect`, `frontend`, `backend`, `devops`, `security`, `testing` |
| `security` | `read`, `search` | nenhum |
| `testing` | `read`, `search`, `edit`, `execute` | nenhum |

A delegação em `agents` limita os especialistas listados no perfil; não
concede permissões de sistema operacional nem garante que cada especialista
esteja habilitado no runtime. Verifique os controles próprios da sessão
delegada quando precisar confirmar seu acesso efetivo.

### Como verificar os controles efetivos

Na sessão do Copilot que executará os comandos:

1. Confirme o harness e a máquina onde os comandos serão executados. Em sessões
   remotas, WSL ou containers, caminhos e políticas referem-se ao host de
   execução, não necessariamente ao desktop local.
2. No seletor de permissões, confira o nível de aprovação. **Manual**,
   **Assisted** e **Allow all** controlam quando ações pedem aprovação; não
   ampliam o acesso imposto pelo sandbox nem substituem políticas da
   organização.
3. Execute `/sandbox policy` e confira se o sandbox está ativo, quais caminhos
   são legíveis ou graváveis e qual política de rede está efetiva. Repita após
   alterar permissões; para conferir defaults, use uma nova sessão.
4. Verifique os controles das sessões delegadas. Para outros harnesses, consulte
   seus controles próprios de sandbox e permissões. Não infira que o estado de
   uma sessão se aplica às demais.

O sandbox do Copilot restringe comandos de terminal e seus processos filhos;
alguns MCP servers e language servers gerenciados pela sessão também podem ser
isolados. Outras ferramentas têm controles próprios, portanto uma política de
terminal não comprova o limite de ferramentas que não iniciam processos do
sistema operacional. Aprovar uma ação não expande os caminhos ou destinos de
rede permitidos pelo sandbox.

No Copilot, o workspace é gravável por padrão e outros caminhos podem ser
acessíveis conforme os defaults do runtime e as permissões configuradas.
Conexões de saída à rede são permitidas por padrão; acesso à rede local é
controlado separadamente. Consulte a política efetiva em vez de inferir
isolamento a partir de uma configuração declarada.

Como recomendações de least privilege, habilite o sandbox em ambientes
suportados, mantenha cada perfil com apenas as ferramentas necessárias,
prefira aprovações e permissões de caminho com escopo mínimo, restrinja
destinos de rede quando a tarefa não exigir acesso amplo e só permita acesso à
rede local quando necessário. Não use **Allow all** como controle de
isolamento.

Consulte também a [documentação de aprovações e permissões do VS Code](https://code.visualstudio.com/docs/agents/run/approvals).

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

Para ideias que precisem de discovery, prefira apresentar uma proposta
consolidada com escopo, fundamentos aplicáveis, alternativas relevantes e
decisões agrupadas para revisão. Quando houver interface, identifique o Design
System e suas foundations; se a escolha estiver em aberto, proponha opções para
aprovação. Quando uma nova identidade visual for necessária, inclua alternativas
de direção visual. O usuário pode
aprovar a proposta ou indicar ajustes antes da implementação. Uma aprovação
explícita abrange as escolhas recomendadas para adoção, não as alternativas nem
decisões pendentes; preserve as escolhas confirmadas no delivery.

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
