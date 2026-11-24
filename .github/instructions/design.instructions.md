---
description: Use ao definir ou alterar a direção visual de interfaces e produtos digitais.
applyTo: "**/*.{html,css,scss,sass,less,jsx,tsx,vue,svelte,astro}"
---

# Instruções de Direção Visual

Crie interfaces adequadas ao produto, ao público e à tarefa, sem impor uma
estética única. Preserve acessibilidade, responsividade, legibilidade e
clareza, sem sacrificar desempenho para obter um efeito visual.

## Contexto e identidade existente

Antes de propor uma direção visual, identifique o objetivo do produto, seu
público, conteúdo, contexto de uso e requisitos confirmados. Inspecione
identidade, referências, componentes, tokens e padrões visuais existentes.

Uma identidade pode estar expressa nos próprios padrões da interface, mesmo
sem um Design System formal. Preserve-a em ajustes e evoluções; alinhe com o
usuário mudanças que divirjam materialmente dela antes de implementá-las.

## Nova direção visual

Quando a tarefa exigir uma direção visual e não houver identidade existente ou
direção previamente aprovada:

1. Identifique lacunas relevantes de contexto; quando possível, apresente
   alternativas com assumptions explícitas e agrupe as questões para o usuário.
2. Apresente alternativas visualmente distintas, adequadas ao produto e
   proporcionais ao escopo.
3. Explique para cada alternativa a intenção e as principais escolhas de
   composição, hierarquia, tipografia, escala, ritmo, cor, contraste,
   superfícies, espaçamento, densidade, imagens, ícones e elementos gráficos,
   considerando interação e movimento quando relevantes.
4. Recomende uma alternativa, explicando seus trade-offs e como atende ao
   público e à tarefa.
5. Aguarde a aprovação explícita do usuário antes de implementar a interface
   nessa direção. Se ele solicitar ajustes ou rejeitar as alternativas,
   refine a proposta antes de prosseguir.

Não trate uma recomendação, silêncio ou pedido genérico de implementação como
aprovação de uma direção visual específica. A aprovação explícita de uma
proposta consolidada que recomende uma direção para adoção também aprova essa
direção; alternativas não recomendadas e decisões pendentes não são aprovadas.

## Escolhas visuais

Evite recorrer automaticamente a fórmulas genéricas, como hero com gradiente,
cards uniformes, bordas arredondadas e efeitos decorativos. Esses recursos são
aceitáveis quando fizerem sentido para o produto e a tarefa.

Use componentes e padrões existentes quando apropriado. Não introduza uma
dependência, uma biblioteca visual ou uma camada global de tokens apenas para
produzir diferenciação estética.

A escolha de um Design System e a definição de foundations são obrigatórias
para interfaces; siga `.github/instructions/design.stacks.instructions.md`.

### Tipografia

Reutilize as fontes e os padrões tipográficos existentes quando adequados.
Quando for necessário pesquisar alternativas, catálogos como
[Google Fonts](https://fonts.google.com/) e [Fontsource](https://fontsource.org/)
podem servir como referência pública; não presuma que toda fonte tenha a mesma
licença. Verifique as condições de uso e distribuição da fonte escolhida,
além de legibilidade e cobertura dos idiomas do produto.

Prefira fontes já disponíveis no projeto ou alternativas do sistema quando
atenderem à direção visual. Não introduza carregamento por serviços externos em
runtime; respeite as restrições de rede e de dependências do workspace ao
obter ou incorporar arquivos de fontes.

### Temas claro e escuro

Preserve os temas e mecanismos existentes. Suporte a temas claro e escuro
quando fizer parte dos requisitos do produto; não introduza um seletor ou um
novo tema apenas por padrão.

Quando ambos forem suportados:

- mantenha contraste, legibilidade, estados de interação e foco visível em
  cada tema, sem depender apenas de cor para transmitir informação;
- reutilize tokens e componentes existentes, mantendo a identidade visual;
- respeite a preferência explícita do usuário e, na ausência dela, considere
  `prefers-color-scheme` conforme o comportamento definido para o produto;
- se houver seletor, garanta nome acessível e operação por teclado; persista a
  escolha apenas quando necessário e conforme os requisitos do produto;
- verifique a aparência inicial e a troca de tema, evitando mudanças visuais
  inesperadas e respeitando preferências de movimento reduzido.

Siga também as instruções de frontend e acessibilidade aplicáveis. Para
ajustes locais que preservem a identidade existente, adapte a profundidade da
análise ao impacto, sem exigir uma proposta visual formal.
