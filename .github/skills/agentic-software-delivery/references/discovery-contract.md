# Contrato de discovery e handoff

Este contrato é usado pelas skills `/discovery` e `/delivery` e
pelos agentes ao compartilharem requisitos provenientes de discovery. As
chaves e os valores enumerados são identificadores técnicos em inglês; os
textos destinados às pessoas são escritos em pt-BR. O contrato não é um
mecanismo automático de segurança nem um substituto para aprovação humana.

## Proposta e baseline

O documento Markdown contém exatamente um bloco cercado com a linguagem `json`.
Esse bloco é a fonte de verdade; textos fora dele não podem contradizê-lo.
Todos os campos abaixo são obrigatórios. Arrays sem itens aplicáveis usam `[]`.

- `schema_version`: string `"1.3"` para novos documentos.
- `status`: string `"proposed"` para propostas não aprovadas ou `"approved"`
  somente após aprovação explícita do usuário.
- `project`: objeto com `name` e `goal`, strings não vazias.
- `scope`: objeto com arrays de strings `in_scope` e `out_of_scope`.
- `requirements`: array de objetos com `id` único, `description`,
  `classification`, `rationale` e `acceptance_criteria`. `id` e `description`
  são strings não vazias; `acceptance_criteria` é um array de strings.
  `classification` é `confirmed`, `derived`, `proposed`, `recommended` ou
  `assumption`. `proposed` identifica requisito sugerido para o escopo de
  trabalho, sem confirmação do usuário; `recommended` indica uma sugestão
  fora desse escopo.
  `rationale` é uma string, obrigatoriamente não vazia para `derived`, que
  identifica a origem da derivação; nos demais casos pode ser vazia.
  Requisitos `confirmed`, `derived` ou `proposed` precisam de ao menos um
  critério de aceite não vazio.
- `decisions`: array de objetos com `id` único, `description`, `status`,
  `rationale` e `alternatives`. Os dois primeiros são strings não vazias;
  `status` é `confirmed`, `recommended` ou `pending`. `recommended`
  identifica uma escolha proposta para adoção; `pending`, uma questão sem
  escolha recomendada. `rationale` é uma string não vazia para decisões
  `recommended` e pode ser vazia nos demais casos. `alternatives` é um array
  de strings, que pode ser vazio.
- `open_questions`: array de objetos com `id` único, `description` e
  `blocking`. Os dois primeiros são strings não vazias; `blocking` é boolean.
  Uma proposta pode conter questões com `blocking: true`; elas devem ser
  resolvidas antes da aprovação da baseline. Uma baseline aprovada não pode
  conter questão bloqueante nem decisão `pending` que seja bloqueante. Uma
  decisão pendente bloqueante também deve constar em `open_questions` com
  `blocking: true`.
- `instruction_reviews`: array com uma avaliação para cada arquivo
  `*.instructions.md` diretamente em `.github/instructions/`. Cada objeto
  contém:
  - `instruction`: caminho relativo do arquivo, usando `/`.
  - `applicability`: `applicable`, `not_applicable` ou `pending`. O último
    só é permitido em uma proposta ainda não aprovada.
  - `reviewed_sections`: array não vazio com os títulos exatos de seções
    consultadas no arquivo, sem os marcadores `#`.
  - `rationale`: string não vazia explicando a aplicabilidade e, quando
    pertinente, o que foi considerado.
  - `related_items`: array com IDs de requisitos ou decisões relacionados.
    Pode ser vazio quando a instrução não produzir uma decisão ou requisito
    específico; para `not_applicable`, deve ser vazio.

IDs são únicos dentro de cada array e mantidos nos handoffs. Inclua dados,
integrações, segurança, regras de negócio, requisitos não funcionais e decisões
de experiência ou stack quando aplicáveis, representando-os nos campos acima.
Não invente confirmações e não inclua secrets ou dados pessoais desnecessários.
Na proposta, requisitos `proposed` e decisões `recommended` são recomendações
para adoção, não confirmações. O usuário pode aceitar a proposta inteira ou
pedir ajustes. Após aceite explícito e resolução das questões bloqueantes,
atualize o mesmo documento: altere o status para `approved`, converta os
requisitos `proposed` aceitos para `confirmed` e as decisões `recommended`
aceitas para `confirmed`, preservando IDs, justificativas e alternativas.
Não converta `derived`, `recommended` em `requirements`, `assumption`,
alternativas ou decisões pendentes em escolhas confirmadas. Uma baseline
`1.2` ou `1.3` aprovada não pode conter requisitos `proposed` ou decisões
`recommended`. Se o aceite for parcial ou ambíguo, esclareça-o antes de
registrar a aprovação.

Para compatibilidade, `/delivery` também aceita documentos aprovados das
versões `1.0`, `1.1` e `1.2` anteriores, com aviso de que a avaliação das
instruções não é verificável. A versão `1.2` usa os mesmos campos da `1.3`,
exceto `instruction_reviews`. Na versão `1.0`, as classificações são
`confirmed`, `derived`, `recommended` e `assumption`; na `1.1`, também há
`proposed`. Nessas versões, decisões possuem apenas `id`, `description` e
`status` (`confirmed` ou `pending`); uma baseline `1.1` aprovada pode conter
requisitos `proposed` e eles permanecem escopo sugerido, não confirmação do
usuário. A versão `1.0` não admite status ou classificação `proposed`. Não
converta nem reescreva documentos antigos automaticamente.

### Exemplo de proposta

Este exemplo ilustra uma aplicação de interface simples, sem backend ou
infraestrutura no escopo proposto. As justificativas dependem do projeto real.

```json
{
  "schema_version": "1.3",
  "status": "proposed",
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
      "id": "RF-02",
      "description": "Permitir editar compromissos cadastrados",
      "classification": "proposed",
      "rationale": "",
      "acceptance_criteria": [
        "Permitir alterar título e data de um compromisso existente"
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
      "status": "confirmed",
      "rationale": "",
      "alternatives": []
    },
    {
      "id": "DEC-02",
      "description": "Usar HTML, CSS e JavaScript sem framework para a interface",
      "status": "recommended",
      "rationale": "Atende à interface simples proposta sem adicionar framework.",
      "alternatives": ["Usar um framework de interface após avaliar a necessidade"]
    }
  ],
  "open_questions": [
    {
      "id": "Q-01",
      "description": "Lembretes serão incluídos em uma versão futura?",
      "blocking": false
    },
    {
      "id": "Q-02",
      "description": "Qual Design System e quais foundations serão adotados?",
      "blocking": true
    }
  ],
  "instruction_reviews": [
    {
      "instruction": ".github/instructions/accessibility.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Semântica"],
      "rationale": "A interface deve usar elementos semânticos.",
      "related_items": ["DEC-02"]
    },
    {
      "instruction": ".github/instructions/architecture.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Princípios"],
      "rationale": "A solução deve ter responsabilidades simples e explícitas.",
      "related_items": ["DEC-02"]
    },
    {
      "instruction": ".github/instructions/backend.instructions.md",
      "applicability": "not_applicable",
      "reviewed_sections": ["Boundaries"],
      "rationale": "A proposta não inclui aplicação server-side.",
      "related_items": []
    },
    {
      "instruction": ".github/instructions/backend.stacks.instructions.md",
      "applicability": "not_applicable",
      "reviewed_sections": ["Python"],
      "rationale": "A proposta não inclui stack server-side.",
      "related_items": []
    },
    {
      "instruction": ".github/instructions/design.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Contexto e identidade existente"],
      "rationale": "A interface precisa respeitar a identidade aplicável.",
      "related_items": ["DEC-02"]
    },
    {
      "instruction": ".github/instructions/design.stacks.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Escolha de Design System"],
      "rationale": "A direção visual exige avaliar um Design System.",
      "related_items": ["DEC-02"]
    },
    {
      "instruction": ".github/instructions/devops.instructions.md",
      "applicability": "not_applicable",
      "reviewed_sections": ["CI/CD"],
      "rationale": "O exemplo não inclui configuração operacional ou CI/CD.",
      "related_items": []
    },
    {
      "instruction": ".github/instructions/devops.stacks.instructions.md",
      "applicability": "not_applicable",
      "reviewed_sections": ["CI/CD"],
      "rationale": "Nenhuma ferramenta de CI/CD está no escopo do exemplo.",
      "related_items": []
    },
    {
      "instruction": ".github/instructions/frontend.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Components"],
      "rationale": "O escopo inclui uma interface de consulta e cadastro.",
      "related_items": ["RF-01", "DEC-02"]
    },
    {
      "instruction": ".github/instructions/frontend.stacks.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["HTML", "CSS e pré-processadores"],
      "rationale": "A stack recomendada usa HTML e CSS.",
      "related_items": ["DEC-02"]
    },
    {
      "instruction": ".github/instructions/project.structure.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Projetos novos"],
      "rationale": "A proposta prevê uma nova aplicação.",
      "related_items": ["DEC-02"]
    },
    {
      "instruction": ".github/instructions/security.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Trust"],
      "rationale": "As entradas da aplicação não são confiáveis.",
      "related_items": ["RF-01"]
    },
    {
      "instruction": ".github/instructions/testing.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Cenários"],
      "rationale": "Os critérios de aceite precisam de validação.",
      "related_items": ["RF-01"]
    }
  ]
}
```

### Exemplo de avaliação na versão 1.3

O trecho abaixo ilustra dois itens de `instruction_reviews`, não um documento
completo. Um documento válido deve incluir todos os arquivos de instruções
existentes, mesmo quando não aplicáveis.

```json
{
  "instruction_reviews": [
    {
      "instruction": ".github/instructions/security.instructions.md",
      "applicability": "applicable",
      "reviewed_sections": ["Trust"],
      "rationale": "As entradas da aplicação precisam ser tratadas como não confiáveis.",
      "related_items": ["RF-01"]
    },
    {
      "instruction": ".github/instructions/backend.instructions.md",
      "applicability": "not_applicable",
      "reviewed_sections": ["Boundaries"],
      "rationale": "A proposta não inclui aplicação server-side.",
      "related_items": []
    }
  ]
}
```

### Verificação local

Na raiz do workspace, execute com Python 3 e o caminho do documento:

```powershell
python scripts\validate_discovery.py DISCOVERY.md
```

Para a versão `1.3`, a verificação confere o bloco JSON, a versão e o estado,
a cobertura dos arquivos de instruções atuais, duplicidades, aplicabilidade,
justificativas, existência dos títulos de seção e referências a IDs. Ela não
valida os demais campos do contrato nem comprova que o agente leu as seções ou
que seu julgamento está correto; essas verificações continuam sendo
responsabilidade do agente e da revisão humana. Novos arquivos ou seções
renomeadas podem exigir atualização da avaliação.

O comando retorna erro em caso de falha; para versões `1.0`, `1.1` e `1.2`,
retorna aviso sem bloquear, pois elas não exigem avaliações estruturadas.
Não altere automaticamente documentos antigos para simular cobertura.

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
  "schema_version": "1.3",
  "source": "DISCOVERY.md",
  "objective": "Avaliar a proposta de cadastro de compromissos",
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
      "status": "confirmed",
      "rationale": "",
      "alternatives": []
    }
  ],
  "open_questions": [],
  "constraints": [],
  "expected_result": "Parecer sobre os requisitos propostos"
}
```

`source`, `objective` e `expected_result` são strings não vazias; `source`
identifica o arquivo efetivamente usado. `schema_version` corresponde à versão
da origem. `constraints` é um array de strings.
O handoff não autoriza operações fora das políticas e permissões existentes.
