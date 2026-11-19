# Bug Resolution

## Workflow

1. Identificar comportamento observado, esperado, ambiente, impacto e evidências.
2. Reproduzir com segurança usando testes, logs ou ambiente descartável.
3. Distinguir causa raiz, sintoma, ambiente, configuração, dependência e teste incorreto.
4. Corrigir a causa com a menor mudança sustentável.
5. Criar regression test quando viável; confirmar falha antes e sucesso depois quando possível.
6. Avaliar impacto de segurança e envolver revisão quando material.
7. Executar validação direcionada e ampliar conforme risco.

Não mascarar sintomas, aumentar timeout sem causa, ocultar exceptions, desabilitar controles ou enfraquecer testes.

## Resposta

Causa raiz; Correção; Componentes alterados; Regression test; Validação; Limitações.
