# Roadmap do Sistema Agentico

## Objetivo

Evoluir a configuração agentica com mudanças incrementais, verificáveis e
guiadas por evidências de uso. Este roadmap é um plano de trabalho inicial:
itens são propostas, não requisitos aprovados nem compromissos de prazo.

## Status

- `[ ]` Não iniciado
- `[/]` Em andamento
- `[x]` Concluído
- `[!]` Bloqueado ou aguardando decisão

## Prioridades

### 1. Validar a configuração automaticamente

**Objetivo:** detectar erros estruturais e referências quebradas nos arquivos
de agentes, instruções e skills.

- [x] Inventariar os formatos e relações que precisam de validação.
- [x] Definir verificações para frontmatter, identificadores de agentes,
  referências entre arquivos e padrões `applyTo`.
- [x] Executar as verificações localmente e integrar a checagem à pipeline de
  CI descrita no item 7.

**Critérios de conclusão:**

- Uma única verificação documentada pode ser executada localmente.
- Referências inexistentes e metadados inválidos são reportados com contexto
  suficiente para correção.
- A validação não exige credenciais nem serviços externos.

### 2. Tornar explícitos os controles de segurança no runtime

**Objetivo:** distinguir as regras comportamentais das permissões efetivamente
aplicadas pelo ambiente.

- [ ] Mapear permissões de leitura, edição, terminal, rede e delegação por
  agente e por ambiente.
- [ ] Documentar como verificar os controles ativos e suas limitações.
- [ ] Revisar recomendações de sandbox e permissões mínimas antes de ampliar a
  autonomia dos agentes.

**Critérios de conclusão:**

- A documentação identifica quais limites são instruções e quais são
  enforcement do runtime.
- As recomendações não pressupõem que sandbox de terminal controle todas as
  ferramentas.
- Restrições e limitações conhecidas ficam documentadas sem sugerir acesso a
  produção ou uso de credenciais reais.

### 3. Reduzir duplicação entre instruções

**Objetivo:** diminuir divergência e custo de manutenção sem remover controles
importantes.

- [ ] Identificar regras repetidas entre instruções globais, `AGENTS.md`,
  perfis de agentes e skills.
- [ ] Definir uma fonte canônica para cada regra compartilhada e substituir
  duplicações por referências quando apropriado.
- [ ] Reexecutar as verificações estruturais após
  as consolidações.

**Critérios de conclusão:**

- Regras compartilhadas têm uma fonte principal identificável.
- Handoffs, validação, segurança e ownership continuam cobertos.

### 4. Estabelecer um ciclo de melhoria contínua

**Objetivo:** priorizar mudanças a partir de problemas observados, evitando
métricas ou coleta de dados sem propósito.

- [ ] Definir quais sinais de fricção valem acompanhar, como retrabalho,
  falhas na primeira validação ou delegações sem valor.
- [ ] Definir como registrar resultados sem expor código privado, credenciais
  ou dados pessoais.
- [ ] Revisar periodicamente os cenários e prioridades com base nos resultados.

**Critérios de conclusão:**

- Cada sinal acompanhado tem propósito e forma de coleta definidos.
- Nenhum dado sensível é necessário para avaliar o processo.
- O roadmap é revisado quando evidências novas justificarem mudança de
  prioridade.

### 5. Avaliar a criação de um agente DevOps/Platform

**Objetivo:** decidir se as instruções de DevOps existentes precisam de um
agente especializado com ownership próprio.

- [ ] Revisar os tipos de tarefas cobertos por
  `.github/instructions/devops.instructions.md` e identificar necessidades
  recorrentes que não estejam bem atendidas pelos agentes atuais.
- [ ] Definir o escopo potencial do agente, seus limites de ownership e as
  ferramentas e permissões mínimas necessárias.
- [ ] Comparar os benefícios de um agente dedicado com a manutenção das
  instruções e a colaboração dos agentes existentes.
- [ ] Registrar a decisão e, se aprovada, atualizar os perfis de delegação e
  as referências operacionais relacionadas.

**Critérios de conclusão:**

- A decisão de criar ou não o agente é justificada por tarefas e necessidades
  identificáveis.
- Caso recomendado, o perfil define responsabilidades, limites, ferramentas
  e regras de delegação sem sobreposição desnecessária.
- A proposta respeita os controles de segurança e não depende de acesso a
  produção ou credenciais reais.

### 6. Completar as instruções de Design Systems para Frontend

**Objetivo:** orientar os agentes a trabalhar de forma consistente com o
Design System existente ou, quando não houver um, evitar introduzir padrões
visuais e dependências sem necessidade.

- [ ] Definir como identificar os componentes, tokens, padrões e documentação
  do Design System do projeto.
- [ ] Orientar o uso e a extensão de componentes e tokens existentes, evitando
  duplicação ou overrides desnecessários.
- [ ] Definir como proceder quando o projeto não possui Design System ou quando
  o sistema existente não cobre a necessidade.
- [ ] Alinhar as orientações com acessibilidade, responsividade e direção
  visual já definidas para o agente Frontend.

**Critérios de conclusão:**

- As instruções priorizam os padrões e componentes existentes sem presumir
  biblioteca ou framework específico.
- Novos componentes, tokens ou dependências são propostos somente quando
  necessários e consistentes com a arquitetura do projeto.
- As orientações não conflitam com as instruções de frontend e acessibilidade
  existentes.

### 7. Integrar a validação agentica a uma pipeline

**Objetivo:** detectar erros na configuração agentica antes da integração de
alterações no repositório.

- [x] Usar GitHub Actions em pull requests e pushes para a branch `main`.
- [x] Configurar a pipeline para executar o validador de configuração e seus
  testes.
- [x] Documentar como consultar os resultados e reproduzir falhas localmente.

A pipeline está em
[validate-agentic-config.yml](.github/workflows/validate-agentic-config.yml).

**Critérios de conclusão:**

- Uma falha no validador ou em seus testes resulta em uma execução de CI com
  status de falha.
- A pipeline não exige secrets e utiliza apenas as permissões necessárias.
- A documentação esclarece que a checagem estática não valida o comportamento
  dos agentes em sessões reais.

## Decisões em aberto

- Ferramentas e formato para validar Markdown, YAML e referências.
- Controles de sandbox e permissões compatíveis com o runtime utilizado.
- Necessidade de um agente DevOps/Platform dedicado.
- Sinais de qualidade que serão acompanhados e por quanto tempo.

## Notas de execução

- Começar pela validação estática e pela revisão das prioridades operacionais.
- Não escolher stack, dependências ou provedor de CI antes de inspecionar as
  opções existentes no workspace.
- Atualizar este roadmap quando prioridades, decisões ou critérios mudarem.
