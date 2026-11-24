# Contrato de discovery e handoff

Este contrato versão `1.0` é usado pelas skills `/discovery` e `/delivery` e
pelos agentes ao compartilharem requisitos provenientes de discovery. As
chaves e os valores enumerados são identificadores técnicos em inglês; os
textos destinados às pessoas são escritos em pt-BR. O contrato não é um
mecanismo automático de segurança nem um substituto para aprovação humana.

## Baseline

O documento Markdown contém exatamente um bloco cercado com a linguagem `json`.
Esse bloco é a fonte de verdade; textos fora dele não podem contradizê-lo.
Todos os campos abaixo são obrigatórios. Arrays sem itens aplicáveis usam `[]`.

- `schema_version`: string `"1.0"`.
- `status`: string `"approved"` somente após aprovação explícita do usuário.
- `project`: objeto com `name` e `goal`, strings não vazias.
- `scope`: objeto com arrays de strings `in_scope` e `out_of_scope`.
- `requirements`: array de objetos com `id` único, `description`,
  `classification`, `rationale` e `acceptance_criteria`. `id` e `description`
  são strings não vazias; `acceptance_criteria` é um array de strings.
  `classification` é `confirmed`, `derived`, `recommended` ou `assumption`.
  `rationale` é uma string, obrigatoriamente não vazia para `derived`, que
  identifica a origem da derivação; nos demais casos pode ser vazia.
  Requisitos `confirmed` ou `derived` precisam de ao menos um critério de
  aceite não vazio.
- `decisions`: array de objetos com `id` único, `description` e `status`.
  Os dois primeiros são strings não vazias; `status` é `confirmed` ou
  `pending`.
- `open_questions`: array de objetos com `id` único, `description` e
  `blocking`. Os dois primeiros são strings não vazias; `blocking` é boolean.
  Uma baseline aprovada não pode conter questão com `blocking: true` nem
  decisão `pending` que seja bloqueante. Uma decisão pendente bloqueante deve
  também constar em `open_questions` com `blocking: true`.

IDs são únicos dentro de cada array e mantidos nos handoffs. Inclua dados,
integrações, segurança, regras de negócio, requisitos não funcionais e decisões
de experiência ou stack quando aplicáveis, representando-os nos campos acima.
Não invente valores e não inclua secrets ou dados pessoais desnecessários.
Recomendações e assumptions permanecem identificadas como tais, mesmo em uma
baseline aprovada; somente requisitos e decisões efetivamente aprovados
orientam a implementação. Decisões pendentes não bloqueantes continuam visíveis.

### Exemplo de baseline

```json
{
  "schema_version": "1.0",
  "status": "approved",
  "project": {
    "name": "Agenda",
    "goal": "Organizar compromissos pessoais"
  },
  "scope": {
    "in_scope": ["Cadastro e consulta de compromissos"],
    "out_of_scope": ["Sincronização com calendários externos"]
  },
  "requirements": [
    {
      "id": "RF-01",
      "description": "Cadastrar compromissos com título e data",
      "classification": "confirmed",
      "rationale": "",
      "acceptance_criteria": [
        "Permitir cadastrar e consultar título e data de um compromisso"
      ]
    },
    {
      "id": "REC-01",
      "description": "Avaliar lembretes de compromissos",
      "classification": "recommended",
      "rationale": "",
      "acceptance_criteria": []
    }
  ],
  "decisions": [
    {
      "id": "DEC-01",
      "description": "A primeira versão não sincroniza calendários externos",
      "status": "confirmed"
    }
  ],
  "open_questions": [
    {
      "id": "Q-01",
      "description": "Lembretes serão incluídos em uma versão futura?",
      "blocking": false
    }
  ]
}
```

## Handoff entre agentes

Ao delegar ou devolver resultados que incluam requisitos de discovery, use um
objeto JSON com os campos abaixo. Inclua apenas os requisitos, decisões e
questões relevantes, mantendo seus IDs, estrutura e classificação originais.
Use arrays vazios quando não aplicáveis. Outros detalhes de implementação e
validações podem ser comunicados normalmente; o usuário continua recebendo
respostas em pt-BR. Se um agente receber conteúdo incompatível ou insuficiente,
deve solicitar esclarecimento em vez de completar ou reclassificar dados.

```json
{
  "schema_version": "1.0",
  "source": "DISCOVERY.md",
  "objective": "Implementar o cadastro de compromissos",
  "requirements": [
    {
      "id": "RF-01",
      "description": "Cadastrar compromissos com título e data",
      "classification": "confirmed",
      "rationale": "",
      "acceptance_criteria": [
        "Permitir cadastrar e consultar título e data de um compromisso"
      ]
    }
  ],
  "decisions": [
    {
      "id": "DEC-01",
      "description": "A primeira versão não sincroniza calendários externos",
      "status": "confirmed"
    }
  ],
  "open_questions": [],
  "constraints": [],
  "expected_result": "Cadastro e consulta validados"
}
```

`source`, `objective` e `expected_result` são strings não vazias; `source`
identifica o arquivo efetivamente usado. `constraints` é um array de strings.
O handoff não autoriza operações fora das políticas e permissões existentes.
