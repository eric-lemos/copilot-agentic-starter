---
description: Use ao criar ou alterar código e ao avaliar legibilidade, tipagem, tratamento de erros, dependências e manutenção.
---

# Instruções de Qualidade de Código

Produza código simples de compreender, modificar, testar e remover.

## Clareza

Prefira código explícito sobre código excessivamente inteligente.

Use nomes que expressem intenção.

Evite abbreviations ambíguas.

Código deve explicar principalmente o que faz.

Comentários devem explicar por que uma decisão não evidente foi necessária.

---

## Funções

Funções devem possuir responsabilidade clara.

Evite:

- muitos níveis de nesting;
- muitos efeitos colaterais;
- parâmetros booleanos ambíguos;
- funções excessivamente longas;
- retorno com múltiplos significados implícitos.

Não divida funções apenas para atingir uma métrica arbitrária de tamanho.

---

## Duplicação

Remova duplicação de conhecimento, não necessariamente toda repetição textual.

Não introduza abstração antes de entender o padrão real de reuso.

Uma pequena repetição pode ser preferível a uma abstração incorreta.

---

## Tipagem

Quando a linguagem possuir type system:

- utilize tipos específicos;
- modele estados relevantes;
- trate nullability conscientemente;
- evite escapes inseguros;
- evite `any` ou equivalentes quando houver alternativa adequada.

Não crie tipos excessivamente complexos apenas para demonstrar precisão.

---

## Imutabilidade

Prefira imutabilidade quando ela simplificar o raciocínio.

Não force imutabilidade quando dificultar desnecessariamente a implementação.

---

## Error Handling

Não ignore erros silenciosamente.

Preserve contexto útil.

Evite:

- catch genérico sem tratamento;
- retorno de sucesso após falha;
- exceptions usadas como controle de fluxo normal sem necessidade.

Use padrões idiomáticos da linguagem e do framework.

---

## Configuração

Evite valores específicos de ambiente diretamente no código.

Utilize mecanismos de configuração existentes.

Defaults devem ser seguros e previsíveis.

---

## Dead Code

Remova código:

- não utilizado;
- obsoleto;
- comentado sem finalidade;
- experimentos abandonados.

Version control deve preservar histórico.

---

## Dependencies

Uma dependência adicional deve justificar seu custo.

Antes de adicionar:

1. verifique capacidades existentes;
2. considere standard library;
3. considere manutenção;
4. considere segurança;
5. considere impacto operacional.

---

## Refactoring

Refactoring deve possuir objetivo.

Não combine refactoring amplo com feature ou bug fix pequeno sem necessidade.

Preserve comportamento quando o objetivo for exclusivamente refactoring.

Use testes para proteger mudanças estruturais relevantes.

---

## Consistência

Prefira consistência local às preferências pessoais.

Siga:

- formatter;
- linter;
- naming conventions;
- directory structure;
- framework idioms;
- project patterns.

Não introduza um segundo padrão para resolver o mesmo problema sem
justificativa.