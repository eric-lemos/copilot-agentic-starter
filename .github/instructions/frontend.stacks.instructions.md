---
description: Use ao implementar interfaces web com linguagens, frameworks e ferramentas frontend identificados no projeto.
applyTo: "**/*.{html,css,scss,sass,less,js,jsx,mjs,cjs,ts,tsx,mts,cts,vue,svelte,astro}"
---

# Instruções para Tecnologias de Interface

Estas orientações se aplicam a código de interface web. Siga também
`.github/instructions/frontend.instructions.md`,
`.github/instructions/design.instructions.md` e as instruções de acessibilidade.

Antes de escolher uma seção de framework, inspecione as dependências, a
configuração e os componentes relevantes do projeto. Uma extensão de arquivo
por si só não identifica o framework. Em projetos com várias aplicações, use
a stack e as versões da aplicação afetada. Aplique apenas as seções pertinentes
e respeite as APIs e convenções existentes, sem impor migração ou biblioteca.
Em projetos novos, após alinhar as escolhas materiais, aplique as seções das
tecnologias escolhidas também à configuração inicial, aos componentes e à
validação; não dependa de padrões preexistentes para usá-las.
Se a área afetada incluir código server-side, inclusive em JSX ou TSX, leia
também `.github/instructions/backend.stacks.instructions.md` e
`.github/instructions/backend.instructions.md`; não dependa apenas da extensão
para identificar o boundary.
Para interface ou tema em JavaScript ou TypeScript, leia
`.github/instructions/frontend.instructions.md`,
`.github/instructions/design.instructions.md` e
`.github/instructions/accessibility.instructions.md` quando pertinentes e
ainda não estiverem no contexto. Para interface ou tema, leia também
`.github/instructions/design.stacks.instructions.md`, incluindo a escolha
obrigatória do sistema e suas foundations.

Para mudanças relevantes, valide comportamento, estados, acessibilidade e build
afetados com as ferramentas disponíveis. Não afirme qualidade visual sem
evidência; siga a verificação de Design System em
`.github/instructions/design.stacks.instructions.md` quando aplicável.

## HTML

- Use elementos semânticos adequados à função e preserve a estrutura de
  headings, landmarks, formulários e nomes acessíveis.
- Prefira controles nativos e não use elementos interativos aninhados.
- Associe labels e mensagens aos campos; mantenha a ordem de leitura coerente
  com o conteúdo apresentado.

## CSS e pré-processadores

- Reutilize tokens, temas e mecanismos de estilo existentes quando disponíveis.
- Organize estilos conforme o projeto e evite especificidade excessiva,
  overrides globais e `!important` sem necessidade.
- Prefira layouts adaptáveis, respeite zoom e conteúdo variável, e verifique
  contraste, foco visível e movimento reduzido quando aplicável.
- Use recursos e pré-processadores já suportados pela stack; não introduza
  biblioteca de estilos ou sistema de tokens apenas por preferência.

### Tailwind CSS

- Siga a versão, o tema e as convenções de classes do projeto; reutilize
  tokens e componentes existentes antes de adicionar valores ou estilos.
- Mantenha nomes de classes detectáveis pelo processo de build adotado; para
  variantes dinâmicas, prefira mapear opções conhecidas para classes completas.
- Use variantes responsivas, de foco e de movimento conforme necessário e
  confirme que as combinações preservam contraste e legibilidade.

### Bootstrap

- Siga a versão e os componentes, utilitários e mecanismos de tema existentes.
  Prefira estender a configuração adotada a criar overrides globais.
- Use os recursos responsivos da versão instalada e verifique comportamento,
  contraste, foco e semântica; classes visuais não garantem acessibilidade.
- Para componentes interativos, siga a integração existente e evite duplicar o
  controle de estado ou eventos entre Bootstrap e o framework da aplicação.

### Sass

- Siga a versão, organização de arquivos e mecanismos de tema do projeto.
  Reutilize variáveis e mixins existentes quando forem apropriados.
- Evite nesting excessivo e estilos globais que dificultem a manutenção.

### CSS Modules

- Siga as convenções do projeto para nomes, composição e integração com
  componentes; preserve o escopo local dos estilos quando aplicável.
- Use estilos globais e tokens compartilhados pelos mecanismos existentes,
  sem depender de nomes de classes gerados pelo build.

## JavaScript e TypeScript

- Separe comportamento de apresentação quando isso melhorar a manutenção e
  preserve os contratos e a estratégia de estado existentes.
- Em código controlado por framework, use os mecanismos da stack em vez de
  manipular diretamente o DOM que ela gerencia, salvo necessidade justificada.
- Trate eventos, estado assíncrono e limpeza de listeners ou recursos conforme
  o ciclo de vida aplicável. Em TypeScript, use tipos específicos e preserve
  as verificações existentes.
- Não desative escaping nem renderize HTML não confiável sem o tratamento
  seguro apropriado à stack.

## React

- Siga as versões e os padrões de componentes e estado do projeto.
- Use keys estáveis para listas e mantenha estado no menor escopo adequado.
- Respeite as regras de Hooks; use effects para sincronização necessária e
  limpe recursos quando aplicável. Não adicione memoization sem necessidade.

## Vue

- Siga a versão e os padrões de componentes, reatividade e templates do projeto.
- Use keys estáveis em listas e mantenha estado derivado nos mecanismos
  apropriados da stack, evitando watchers desnecessários.
- Preserve atributos e eventos necessários para semântica, foco e acessibilidade
  ao compor componentes.

## Angular

- Siga a versão e os padrões de componentes, templates e reatividade do projeto.
- Preserve os mecanismos de binding e sanitização do framework; não contorne
  verificações de segurança para renderizar conteúdo externo.
- Ao renderizar listas dinâmicas, use identificação estável quando apropriado.
  Gerencie subscriptions e recursos conforme o ciclo de vida e as APIs em uso.

## Svelte

- Siga a versão e os padrões de componentes, reatividade e estado do projeto.
- Use identificação estável em listas dinâmicas quando apropriado e preserve a
  semântica dos elementos ao compor componentes.
- Limpe subscriptions e recursos quando necessário, usando os mecanismos
  compatíveis com a versão adotada.

## Frameworks de aplicação

Siga o roteamento, a renderização e a separação entre server e client já
adotados pelo projeto. Mantenha autorização no server-side e não exponha
secrets ou dados internos no HTML, nos dados serializados ou no bundle.
Use APIs e convenções compatíveis com a versão instalada.

### Next.js

- Identifique o router e os padrões de renderização usados pela aplicação;
  respeite os boundaries entre código de servidor e de cliente.
- Evite transferir dados ou dependências server-side ao cliente sem necessidade.

### Nuxt

- Siga os padrões de rotas, carregamento de dados e renderização existentes.
- Use configuração e dados disponíveis ao cliente apenas para informações
  públicas; preserve os limites server-side da aplicação.

### SvelteKit

- Siga as convenções de rotas e carregamento de dados da versão adotada.
- Mantenha código e configuração exclusivos do servidor em seus boundaries e
  exponha ao cliente somente dados necessários.

### Astro

- Siga os padrões de componentes, rotas e renderização do projeto.
- Limite a hidratação a componentes que precisem de interatividade, quando
  compatível com os requisitos e a arquitetura existentes.

## Performance e qualidade de interface

- Quando a alteração puder afetar performance, use as ferramentas disponíveis
  no projeto para comparar antes e depois em ambiente local seguro, com
  condições e fluxos equivalentes. Registre contexto, resultados e limitações.
- Considere LCP, CLS e responsividade das interações. Use INP de usuários reais
  somente quando dados agregados apropriados estiverem disponíveis localmente
  e autorizados, sem dados sensíveis; medições locais de interação não comprovam
  o INP de campo.
- Investigue, conforme o problema observado, tamanho e carregamento de imagens
  e fontes, estabilidade de layout, JavaScript, tarefas longas, renderizações
  e recursos de terceiros. Reserve espaço para conteúdo que possa deslocar o
  layout e não atrase recursos essenciais sem avaliar o impacto.
- Para minificação de JavaScript e CSS, verifique primeiro o build de produção
  existente; evite minificar fontes versionadas ou duplicar etapas. Preserve
  comportamento e a política existente de source maps.
- Avalie compressão, formatos suportados e imagens responsivas conforme o
  conteúdo e os browsers atendidos. Preserve qualidade visual, proporções e
  alternativas textuais; mantenha os originais quando necessários.
- Analise o tamanho dos bundles e dependências com as ferramentas existentes;
  considere code splitting e carregamento sob demanda quando houver benefício
  medido, sem comprometer interações ou compatibilidade.
- Avalie formatos, subsets e carregamento de fontes respeitando licenças e
  cobertura de caracteres. Use fallbacks adequados e verifique legibilidade e
  deslocamento de layout.
- Priorize recursos necessários ao conteúdo inicial e considere lazy loading
  para conteúdo fora da área visível. Não adie imagens críticas nem adicione
  preload indiscriminadamente; confirme o impacto no fluxo afetado.
- Siga a política de cache existente. Para assets versionados por conteúdo,
  considere cache de longa duração com invalidação adequada; não compartilhe em
  cache respostas privadas ou dados sensíveis.
- Aplique otimizações proporcionais à evidência e verifique regressões; não
  adicione instrumentação, serviços ou dependências apenas para obter métricas.
- Compare tamanhos e métricas antes e depois com builds equivalentes; informe
  resultados observados e limitações sem presumir ganhos não medidos.
- Valide os fluxos e estados afetados em viewports representativos, incluindo
  teclado, foco visível, legibilidade, zoom e movimento reduzido quando
  aplicáveis. Considere loading, empty e error states quando relevantes.
- Combine verificações automatizadas disponíveis com inspeção manual apropriada;
  não trate testes automáticos ou uma pontuação isolada como prova de
  acessibilidade ou qualidade. Informe validações que não puderem ser feitas.

## Build e testes

### Vite

- Siga a configuração de build, plugins e variáveis de ambiente do projeto.
- Trate variáveis expostas ao client, inclusive as com prefixo `VITE_` no
  padrão do Vite, como públicas; não inclua secrets no bundle.

### Vitest

- Use a configuração, os ambientes e as ferramentas de teste existentes.
- Prefira testes isolados e orientados a comportamento; limpe mocks e recursos
  quando necessário, sem depender de ordem de execução.

### Playwright

- Siga a configuração de browsers, ambientes e fixtures do projeto.
- Prefira locators acessíveis e esperas por condições observáveis a sleeps
  arbitrários; use dados sintéticos e ambientes locais seguros.

Siga também `.github/instructions/testing.instructions.md` ao criar ou alterar
testes. Não adicione ferramentas de build ou teste apenas por estarem listadas.
