---
description: Use ao definir ou alterar a direção visual de interfaces e produtos digitais.
applyTo: "**/*.{html,css,scss,sass,less,jsx,tsx,vue,svelte}"
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

1. Identifique lacunas relevantes de contexto e esclareça-as com o usuário.
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
aprovação de uma direção visual específica.

## Escolhas visuais

Evite recorrer automaticamente a fórmulas genéricas, como hero com gradiente,
cards uniformes, bordas arredondadas e efeitos decorativos. Esses recursos são
aceitáveis quando fizerem sentido para o produto e a tarefa.

Use componentes e padrões existentes quando apropriado. Não introduza uma
dependência, uma biblioteca visual ou uma camada global de tokens apenas para
produzir diferenciação estética.

Siga também as instruções de frontend e acessibilidade aplicáveis. Para
ajustes locais que preservem a identidade existente, adapte a profundidade da
análise ao impacto, sem exigir uma proposta visual formal.
