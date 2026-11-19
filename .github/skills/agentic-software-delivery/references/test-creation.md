# Test Creation

## Workflow

1. Identificar comportamento, critérios de aceite, risco, contracts, implementação e ferramentas existentes.
2. Escolher o menor nível confiável: unit, integration, component, contract ou E2E.
3. Cobrir happy path, boundaries, invalid input, failures, authn/authz, ownership, regressions e accessibility conforme risco.
4. Usar stack, fixtures, conventions e test database existentes.
5. Garantir testes determinísticos, independentes, legíveis e behavior-oriented.
6. Evitar sleeps, order dependency, production services, secrets, dados reais e mocking excessivo.
7. Executar testes direcionados e ampliar conforme impacto.
8. Classificar falhas em product defect, test defect, environment, configuration, dependency ou flakiness.

Não alterar production code unilateralmente para facilitar testes. Coordenar mudanças de testability com o domain owner.

## Resposta

Estratégia; Testes criados; Riscos cobertos; Execução e resultados; Defeitos; Limitações e gaps.
