# Feature Delivery

## Prontidão

Confirmar que objetivo, comportamento e critérios de aceite estão claros.
Preservar decisões confirmadas no discovery, incluindo direção visual, Design
System, foundations, idiomas e temas quando aplicáveis. Antes da implementação
visual, identificar o sistema adotado ou alinhar uma escolha e suas foundations
conforme `.github/instructions/design.stacks.instructions.md`. Retornar ao
discovery somente para ambiguidade ou conflito material, mudança de requisitos
ou solicitação do usuário.

## Workflow

1. Inspecionar stack, arquitetura, módulos, contracts, testes e validações existentes. Para necessidades ainda sem tecnologia definida, avaliar prioritariamente as opções documentadas conforme as regras globais e alinhar decisões materiais. Preservar escolhas já adotadas ou explicitamente solicitadas.
2. Definir domínios afetados e coordenar Architect, Frontend, Backend, Security e Testing Agent somente quando necessários.
3. Alinhar contracts antes de implementações frontend/backend incompatíveis.
4. Implementar mudanças focadas, seguras e compatíveis, aplicando as práticas das seções pertinentes à stack e à versão identificadas.
5. Adicionar testes proporcionais ao risco.
6. Executar formatter, lint, static analysis, type checking, testes, security checks, build e E2E quando aplicáveis.
7. Corrigir falhas atribuíveis à mudança e revalidar.

## Conclusão

Informar: Resultado; Principais alterações; Decisões técnicas; Segurança; Testes e validações; Limitações ou riscos.
