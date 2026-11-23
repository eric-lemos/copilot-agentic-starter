# Product Discovery

## Objetivo

Transformar uma ideia em requisitos implementáveis sem iniciar código prematuramente.

## Workflow

1. Identificar problema, atores, resultado esperado e constraints.
2. Separar requisitos confirmados, requisitos derivados, recomendações, assumptions e decisões pendentes.
3. Propor MVP, post-MVP e out-of-scope quando útil.
4. Recomendar somente itens que resolvam necessidades identificáveis.
5. Apresentar uma proposta consolidada, agrupando decisões materiais para reduzir interações.
6. Refinar os pontos alterados ou pendentes conforme o feedback, sem repetir decisões já confirmadas.
7. Consolidar uma Requirements Baseline quando houver clareza suficiente.

## Baseline

Incluir, conforme aplicável: objetivo, escopo, atores, requisitos funcionais e
não funcionais, regras de negócio, dados, integrações, segurança, critérios
de aceite, restrições, itens fora do escopo, decisões em aberto e decisões
confirmadas de experiência, idiomas, temas e direção visual, quando aplicáveis.
Preserve essas decisões na baseline proporcional e nos handoffs relevantes,
sem exigir um documento formal.

Não tratar silêncio como aprovação. Não escolher stack durante discovery, salvo constraint explícita. Se persistida em `docs/requirements/`, escrever a documentação em pt-BR, conforme `.github/copilot-instructions.md`.

## Proposta para revisão

Prefira uma única resposta abrangente, adaptada à ideia, em vez de uma sequência
de perguntas. Quando a informação disponível for insuficiente, sinalize as
lacunas e proponha alternativas com trade-offs, sem inventar requisitos ou
escolher uma stack prematuramente.

Use o modelo abaixo como orientação, não como formulário rígido. Identifique
explicitamente requisitos confirmados, requisitos derivados e sua justificativa,
recomendações, assumptions e decisões pendentes:

1. **Entendimento:** problema, público, resultado esperado e restrições conhecidas.
2. **Escopo:** MVP proposto, critérios de aceite, possíveis etapas posteriores e
   itens fora do escopo.
3. **Fundamentos:** conforme aplicável, acessibilidade, idiomas, temas, segurança,
   dados, integrações, operação e outras necessidades não funcionais. Diferencie
   necessidades identificadas de sugestões e pontos ainda não definidos.
4. **Direção visual:** quando houver interface, preserve a identidade existente.
   Se uma nova direção for necessária, apresente alternativas e recomende uma,
   incluindo tipografia, cores, componentes e referências de Design System,
   conforme `.github/instructions/design.instructions.md`. Não imponha biblioteca.
5. **Decisões técnicas:** opções e trade-offs relevantes, sem fixar stack durante
   discovery, exceto quando for uma constraint explícita.
6. **Revisão e decisões:** identifique o que está recomendado para adoção,
   distinguindo-o das questões que exigem resposta específica. Agrupe essas
   questões e destaque as bloqueantes. Convide o usuário a aprovar a proposta
   inteira ou indicar ajustes.

Não exija tópicos que não se apliquem, como direção visual em uma API sem
interface. A aprovação explícita da proposta abrange as escolhas recomendadas
para adoção, não as alternativas nem os itens ainda pendentes. Não trate silêncio
como aprovação; esclareça respostas ambíguas e resolva decisões bloqueantes antes
de implementar.
