# Code Refactoring

## Objetivo

Melhorar legibilidade, coesão, acoplamento, duplicação, testabilidade, boundaries ou performance comprovada, preservando comportamento observável.

## Workflow

1. Definir problema estrutural, comportamento preservado, contracts e risco.
2. Usar testes existentes; criar characterization tests quando necessário.
3. Refatorar em passos pequenos e verificáveis.
4. Envolver Architect apenas para boundaries, contracts ou dependências estruturais.
5. Validar após cada etapa relevante.

Não misturar feature, alterar comportamento silenciosamente, quebrar contracts, criar abstrações prematuras ou fazer formatting amplo não relacionado.

## Resposta

Problema estrutural; Refactoring; Comportamento preservado; Validação; Impacto arquitetural; Melhorias opcionais.
