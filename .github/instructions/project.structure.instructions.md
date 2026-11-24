---
description: Use ao definir ou alterar a estrutura de arquivos e diretórios de um projeto.
applyTo: "**"
---

# Instruções de Estrutura de Projeto

Organize arquivos de forma previsível e compatível com a stack, o escopo e as
convenções do projeto. Para projetos novos, siga a estrutura abaixo para os
componentes necessários, sem criar diretórios sem finalidade nem impor caminhos
incompatíveis com o framework.

## Projetos existentes

- Inspecione a organização, os manifests, as ferramentas e os pontos de entrada
  existentes antes de adicionar ou mover arquivos.
- Preserve os padrões consolidados e coloque arquivos próximos aos componentes
  ou funcionalidades relacionados, respeitando os boundaries existentes.
- Não reorganize diretórios apenas para aderir a esta estrutura-base.
  Mudanças estruturais relevantes exigem justificativa, alinhamento com o
  usuário e validação de imports, build, testes e contratos afetados.

## Projetos novos

- Crie o projeto em `project/` na raiz do workspace. Essa é a raiz da entrega:
  seu conteúdo deve poder ser transferido para a raiz de um repositório próprio,
  sem depender da configuração agentic deste workspace.
- Use `project/apps/frontend/` para a aplicação frontend e
  `project/apps/backend/` para a aplicação backend quando estiverem no escopo.
  Não crie a aplicação ausente nem seu diretório ou marcador. Preserve a unidade
  de frameworks integrados em vez de separá-los artificialmente.
- Crie `.github/workflows/`, `infra/docker/`, `infra/k8s/`, `infra/terraform/`
  e `scripts/` em `project/` somente quando houver conteúdo correspondente
  necessário. Quando necessário, use esses caminhos para workflows, arquivos
  auxiliares de Docker, recursos Kubernetes, configuração Terraform e scripts,
  respectivamente. Crie `packages/` apenas para código ou configuração
  compartilhados com consumidores reais. Mantenha `.gitignore` e `README.md`
  na raiz. Não crie diretórios vazios ou marcadores para funcionalidades fora
  do escopo; a estrutura não implica adotar tecnologias ou serviços.
- Coloque manifests, configuração, código, testes e assets de cada aplicação
  real em sua raiz. Cada aplicação deve ter seu próprio manifest ou arquivo de
  dependências conforme sua stack; preserve workspaces compartilhados quando
  forem apropriados. Inspecione diretórios existentes antes de criar aplicações
  adicionais, sem sobrescrever ou misturar projetos independentes.
- Cada aplicação implementada deve ter seu próprio Dockerfile e exemplo de
  configuração de ambiente. Mantenha também `.env.example` e um arquivo
  `docker-compose.yml` na raiz de `project/`. Não inclua secrets reais nos
  exemplos; ignore arquivos de ambiente reais e documente apenas as variáveis
  necessárias.
- Configure o Compose para iniciar com `docker compose up` as aplicações e
  dependências locais que existirem no escopo, sem inventar backend, banco de
  dados ou outros serviços. Se não houver serviço executável ou não for possível
  atender a esse comando, explique a limitação e alinhe uma exceção com o
  usuário; não apresente uma configuração não funcional como pronta.
- Para GitHub Actions, crie somente os workflows necessários ao escopo, sem
  jobs ou etapas para aplicações, infraestrutura ou tecnologias ausentes. Se
  nenhum workflow for necessário, não crie `project/.github/workflows/` nem
  seus diretórios ancestrais apenas para preenchimento. Quando necessários,
  coloque os arquivos `.yml` ou `.yaml` diretamente em
  `project/.github/workflows/` e use caminhos relativos à futura raiz do
  repositório do projeto.
- Neste workspace, o GitHub Actions reconhece os workflows em
  `.github/workflows/` na raiz do repositório atual, não os aninhados em
  `project/`. Os workflows da entrega passam a ser reconhecidos quando o
  conteúdo de `project/` for transferido para a raiz de um repositório Git.
  Não sobrescreva a configuração agentic ou os workflows deste repositório.
- Execute scaffolding, instalação e comandos do projeto na raiz correspondente.
  Preserve a estrutura interna exigida pela tecnologia, inclusive um `src/`
  interno quando apropriado. Não confunda o diretório de projetos do workspace
  com o diretório de código de um framework.
- Identifique requisitos, stack, ferramentas e convenções do framework antes
  de definir nomes ou diretórios. Respeite caminhos exigidos pela ferramenta.
- Organize, conforme necessário, código, testes, documentação e configuração.
  Prefira manifests e pontos de entrada nos locais esperados pela stack; não
  crie camadas ou serviços fictícios apenas para preencher a estrutura.
- Na ausência de uma convenção mais apropriada, considere `src/` para código,
  `tests/` para testes e `README.md` para orientações do projeto. Adapte ou
  dispense esses nomes quando a stack ou o escopo indicar outra organização,
  inclusive quando os testes forem colocados próximos ao código.
- Para decisões estruturais relevantes ou sem convenção clara, proponha uma
  organização e alinhe-a com o usuário antes de criar a estrutura.

## Organização interna

- Para os componentes criados em `apps/frontend/`, `apps/backend/` e `infra/`,
  siga os caminhos e as convenções pertinentes definidos nesta instrução.
  Crie os subdiretórios somente quando seu conteúdo for necessário; não use
  marcadores para preencher uma árvore. Respeite caminhos obrigatórios da stack
  ou do framework quando forem diferentes.
- Siga as convenções da stack e agrupe por funcionalidade quando isso melhorar
  coesão e localização do código. Mantenha juntos os arquivos relacionados,
  sem misturar responsabilidades que exijam boundaries distintos.
- Use organização por camadas ou outros padrões quando forem a convenção do
  projeto ou resolverem uma necessidade concreta. A estrutura `apps/` não
  exige camadas internas, packages compartilhados ou abstrações sem justificativa.
- Mantenha arquivos compartilhados em locais com responsabilidade clara; não
  crie diretórios genéricos apenas para acomodar código sem ownership definido.
- Coloque configuração, arquivos gerados, dados de teste e documentação
  conforme as ferramentas existentes. Não versione secrets, caches ou outputs
  gerados que o projeto não deva compartilhar.

## Organização conforme a tecnologia

Aplique as orientações pertinentes à stack e à versão identificadas aos
componentes necessários. Os caminhos abaixo são relativos à raiz de cada
aplicação, não ao workspace. Em projetos existentes, priorize a estrutura
existente; em projetos novos, siga os caminhos indicados quando necessários,
respeitando exigências diferentes do framework. Consulte manifests,
configuração de build e fontes locais; confirme caminhos dependentes de versão
antes de criá-los. As orientações não exigem diretórios sem conteúdo nem
autorizam escolher uma stack.

### Frontend

| Tecnologia | Organização de referência |
| --- | --- |
| HTML, CSS e JavaScript sem framework | Mantenha o ponto de entrada onde o build espera. Separe código, estilos e assets quando houver conteúdo suficiente; em projetos pequenos, poucos arquivos são adequados. |
| React ou Vue com Vite | Use `src/` para código e assets importados e `public/` para arquivos estáticos servidos sem transformação. Agrupe componentes, comportamento e testes por funcionalidade; respeite a configuração do Vite. |
| Angular | Organize funcionalidades em `src/app/` e mantenha templates, estilos e testes próximos aos componentes. Determine diretórios de assets pela configuração de build; não presuma que todas as versões usem `src/assets/`. |
| Next.js | Use `app/` ou `pages/` conforme o router adotado, na raiz ou em `src/` conforme o projeto, e `public/` para arquivos estáticos. Preserve convenções de rotas e boundaries server/client. |
| Nuxt | Respeite os diretórios de aplicação, rotas e servidor da versão adotada. Diferencie assets processados pelo build de arquivos em `public/`; não presuma a mesma estrutura entre versões. |
| SvelteKit | Use `src/routes/` para rotas, `src/lib/` para módulos reutilizáveis e `static/` para arquivos estáticos. Preserve os boundaries de módulos exclusivos do servidor. |
| Astro | Use `src/pages/` para páginas, componentes e layouts próximos às responsabilidades correspondentes, assets importados em `src/` e arquivos estáticos em `public/`. |

Mantenha estilos, tokens e temas do Design System no mecanismo adotado.
Componentes e assets exclusivos de uma funcionalidade devem permanecer próximos
dela; compartilhe apenas o que tiver consumidores reais e responsabilidade clara.

### Backend

| Tecnologia | Organização de referência |
| --- | --- |
| Python | Para packages distribuíveis, considere `src/<package>/` e testes conforme o tooling. Em Django, preserve apps e seus diretórios de migrations, templates e static; em FastAPI ou Flask, organize módulos por responsabilidade sem impor camadas. |
| Go | Preserve packages coesos e testes `*_test.go` próximos ao código. Use `cmd/` para múltiplos executáveis e `internal/` para packages não públicos quando necessário; não crie `pkg/` por padrão. |
| Node.js | Respeite entrypoints e o sistema de módulos. Organize módulos por funcionalidade; em NestJS, mantenha modules, providers, controllers e testes relacionados próximos. |
| Java e Spring Boot | Preserve os source sets do Maven ou Gradle, como `src/main/java`, `src/main/resources` e `src/test/java` quando adotados, e packages por responsabilidade ou funcionalidade. |
| C# e ASP.NET Core | Respeite limites de solution e projects, configuração e localização dos testes. Use `wwwroot/` somente para conteúdo público quando a aplicação o servir; não crie projects por camada sem necessidade. |
| Laravel ou Rails | Preserve os diretórios convencionais do framework para aplicação, rotas, recursos, migrations e testes, conforme a versão e o tooling; não substitua essa estrutura por uma árvore genérica em `src/`. |

Mantenha migrations junto ao mecanismo de persistência e fixtures nos testes.
Templates e recursos de runtime devem seguir as regras de empacotamento da stack,
sem misturar uploads de usuários, configuração privada ou dados reais com fontes.

## Assets e arquivos públicos

- Diferencie assets importados e processados pelo build de arquivos servidos
  diretamente. Use os diretórios e mecanismos da stack, não uma pasta `assets/`
  universal. Arquivos públicos podem ser acessados sem passar pela autorização
  da aplicação; nunca coloque secrets ou conteúdo privado nesses diretórios.
- Agrupe imagens, ícones, fontes e mídia por finalidade ou tipo quando isso
  facilitar localização; não crie subdiretórios vazios. Evite duplicar assets
  compartilhados e preserve avisos de licença e atribuição necessários.
- Prefira imports ou helpers da stack para referências processadas. Para URLs
  públicas, respeite base path, rotas e configuração de deployment; não presuma
  que a aplicação será servida na raiz do domínio.
- Mantenha arquivos-fonte e outputs gerados separados. Inclua assets necessários
  nos artifacts de build e ignore caches e outputs reproduzíveis conforme o
  projeto. Armazene uploads em local próprio, com controles de acesso e ciclo
  de vida definidos, não em diretórios de código versionado.
- Ao mover assets, atualize imports, URLs, CSS, templates, testes e configuração
  dependentes. Preserve nomes e caminhos públicos quando forem contratos ou
  alinhe a mudança de compatibilidade antes de implementá-la.

## Validação

Após mudanças estruturais, execute as verificações pertinentes disponíveis,
incluindo imports, build, empacotamento de recursos e testes afetados. Para
assets de interface, verifique carregamento na aplicação e no build de produção,
respeitando o base path configurado. Informe limitações e não afirme
compatibilidade sem evidência.
