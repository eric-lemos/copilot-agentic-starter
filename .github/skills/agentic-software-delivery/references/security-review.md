# Security Review

Realizar revisão independente. O Security Agent atua somente por leitura e
encaminha correções e execução de ferramentas ao owner ou coordenador.

## Workflow

1. Delimitar componentes, assets, actors, entry points, trust boundaries, inputs, privileged operations e dados sensíveis.
2. Avaliar authentication, authorization, IDOR, privilege escalation, tenant isolation, injection, XSS, CSRF, SSRF, traversal, command injection, deserialization, files, CORS, sessions, tokens, secrets, logging, dependencies, business abuse e resource exhaustion quando aplicáveis.
3. Quando houver capacidade de execução apropriada, usar scanners locais somente quando disponíveis, autorizados e não destrutivos; caso contrário, solicitar a execução ao owner ou coordenador.
4. Classificar findings em Blocker, High, Medium, Low ou Informational.
5. Incluir evidence, risk, abuse scenario, recommendation e validation.
6. Não reproduzir secrets nem payloads perigosos além do necessário.

Se não houver findings materiais, informar escopo, controles observados, ferramentas, limitações e residual risk. Nunca declarar segurança absoluta.
