---
description: Use ao implementar ou revisar configurações de ferramentas DevOps, CI/CD, containers, IaC, orquestração e observabilidade.
applyTo: "**/Dockerfile*,**/Containerfile*,**/Jenkinsfile*,**/*.{yml,yaml,json,groovy,tf,tfvars,hcl,promql,gotmpl,tpl}"
---

# Instruções para Stacks de DevOps

Estas orientações se aplicam a infraestrutura e operação. Siga também
`.github/instructions/devops.instructions.md`, as instruções de segurança e os
limites de execução em `.github/copilot-instructions.md`.

Identifique as ferramentas, versões, configuração e convenções da área afetada
antes de aplicar uma seção. A extensão de um arquivo, por si só, não identifica
a ferramenta nem torna seu conteúdo operacional. Não introduza ferramentas,
provedores ou serviços apenas porque estão listados aqui.

Para uma capacidade operacional nova, aplique as seções das ferramentas
escolhidas desde a configuração inicial e valide o que for possível localmente.
Não dependa de convenções preexistentes para aplicar as práticas nem presuma
que uma ferramenta listada esteja instalada ou autorizada.

Restrinja validações a operações locais autorizadas e seguras. Não execute
deployments, alterações de estado remoto, acesso a cloud, SSH, produção ou
recursos compartilhados. Se uma verificação depender desses acessos ou de
credenciais reais, informe a limitação e proponha uma alternativa local.

Para mudanças relevantes, valide sintaxe, configurações, permissões e
comportamento pertinente com ferramentas locais disponíveis e recursos
seguros e descartáveis. Validação local não comprova funcionamento em
ambientes remotos e não autoriza acesso a eles.

## CI/CD

### GitHub Actions

- Limite permissões de tokens e eventos ao necessário; trate conteúdo de pull
  requests e outros inputs externos como não confiáveis.
- Use actions e versões compatíveis com o projeto, considerando referências
  imutáveis verificadas para dependências externas. Não exponha secrets em
  comandos, logs ou artifacts.

### GitLab CI

- Siga os padrões de stages, jobs, runners e includes do projeto; restrinja
  execução e acesso a variáveis protegidas conforme o contexto.
- Trate inputs e artifacts externos como não confiáveis e evite interpolá-los
  diretamente em comandos.

### Jenkins

- Preserve os padrões de pipelines, agents e plugins instalados; limite
  permissões e escopo das credenciais utilizadas pelo pipeline.
- Não execute código de fontes não confiáveis com privilégios ou credenciais
  disponíveis a jobs protegidos.

## Containers e orquestração

### Docker e Podman

- Siga o formato e as ferramentas adotadas; não presuma que opções ou
  comportamentos sejam idênticos entre runtimes ou versões.
- Use imagens de origem confiável e versões controladas; minimize o contexto e
  os privilégios, evitando incluir secrets em imagens ou camadas.

### Kubernetes

- Preserve namespaces, labels, service accounts e políticas existentes;
  considere least privilege, resource requests e limits quando apropriado.
- Avalie readiness, liveness e estratégia de atualização sem expor dados
  sensíveis em manifests. Não aplique manifests nem acesse clusters.

### Helm

- Siga a versão e as convenções do chart; mantenha values, templates e
  dependências compatíveis com os ambientes suportados.
- Verifique os manifests renderizados localmente quando possível, sem instalar
  releases, acessar clusters ou baixar dependências para contornar limites.

## Infraestrutura e configuração

### Terraform e OpenTofu

- Identifique a ferramenta e versão efetivamente usadas; preserve compatibilidade
  de módulos, providers, lockfiles e configuração de state existentes.
- Revise riscos de substituição ou destruição de recursos sem executar `apply`
  nem acessar state remoto. Não suponha que as ferramentas sejam intercambiáveis.

### Ansible

- Siga a versão e as convenções de inventory, roles e playbooks do projeto.
  Prefira módulos e tarefas idempotentes a comandos shell quando apropriado.
- Não registre secrets em arquivos ou logs; não execute playbooks contra hosts
  externos ou compartilhados nem use credenciais reais.

## Observabilidade

### Prometheus

- Mantenha nomes, unidades e labels consistentes com as métricas existentes.
  Evite labels de alta cardinalidade e dados sensíveis.
- Avalie regras e alertas quanto a significado operacional, carga e ruído;
  não presuma acesso a um servidor ou dados reais para validação.

### Grafana

- Siga os padrões de dashboards, datasources e provisioning do projeto.
  Garanta títulos, unidades e consultas compreensíveis, sem incluir secrets.
- Evite depender de cores como única forma de transmitir informação e não
  altere dashboards ou datasources em serviços remotos.

### OpenTelemetry

- Preserve os padrões existentes de propagação de contexto, recursos,
  atributos e instrumentação relevantes aos boundaries.
- Evite atributos sensíveis e cardinalidade desnecessária; não configure
  exporters ou destinos externos sem requisito e autorização aplicáveis.

## Deployment

### Argo CD

- Preserve os padrões declarativos de applications, fontes e ambientes já
  adotados; revise impactos de sincronização e remoção de recursos.
- Não execute sincronização, alterações de cluster ou operações em serviços
  remotos. Analise manifests e configuração localmente quando possível.

## Performance e qualidade operacional

- Quando a alteração puder afetar performance, compare antes e depois usando
  ferramentas existentes e condições locais equivalentes. Considere, conforme
  o caso, duração de builds, tamanho de artifacts e imagens e uso de recursos.
  Registre contexto, resultados e limitações; não extrapole para produção.
- Investigue gargalos observados antes de alterar paralelismo, cache ou recursos.
  Preserve isolamento, reprodutibilidade e segurança de caches e artifacts;
  verifique regressões após otimizações.
- Em CI/CD, identifique etapas lentas e avalie paralelismo apenas entre tarefas
  independentes. Para caches existentes, considere chaves ligadas a versões e
  lockfiles, invalidação e isolamento entre contextos confiáveis e não
  confiáveis; não armazene secrets nem remova validações para acelerar o fluxo.
- Em builds de imagens, avalie tamanho do contexto, camadas e multi-stage builds
  conforme a stack. Preserve versões, integridade, funcionamento e controles de
  segurança; não remova componentes necessários apenas para reduzir tamanho.
- Em configurações de infraestrutura, revise requests, limits e capacidade
  quando aplicáveis com base em evidências disponíveis e requisitos conhecidos.
  Considere saturação e riscos de falta de recursos, sem alterar estado remoto.
- Em observabilidade, priorize métricas e alertas acionáveis relacionados ao
  serviço; avalie unidades, thresholds, ruído e cardinalidade sem incluir dados
  sensíveis. Não introduza coleta ou serviços sem necessidade justificada.
- Valide sintaxe, configurações e comportamento pertinente com as ferramentas
  locais disponíveis, usando fixtures sintéticas e recursos descartáveis quando
  necessário. Considere falhas, permissões, integridade e riscos de rollback.
- Compare duração, tamanho e uso de recursos antes e depois em condições
  equivalentes; verifique reprodutibilidade e caminhos de falha quando possível.
  Registre medições e não afirme melhorias que não tenham sido observadas.
- Uma validação local ou sintática não comprova o comportamento da pipeline,
  do deployment ou da infraestrutura em um ambiente remoto. Informe verificações
  não executadas e não acrescente ferramentas ou serviços apenas por métricas.
- Mantenha os limites de execução local deste arquivo; não use credenciais reais,
  dados sensíveis ou infraestrutura compartilhada em testes de performance.
