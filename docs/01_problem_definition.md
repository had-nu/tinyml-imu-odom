# Fase 1 – Definição do Problema

## 1. Contexto

- Navegação de robôs móveis em ambientes *indoor e *GPS-denied*.
- Uso de IMUs de baixo custo como principal sensor de movimento.
- Interesse específico no mercado europeu (Espanha/Portugal) para AMRs/AGVs e robôs de serviço.

## 2. Problema central

Como estimar de forma eficiente e robusta o movimento local de um robô (Δx, Δy, Δθ) utilizando apenas dados de IMU em janelas curtas de tempo, com modelos pequenos o suficiente para execução em plataformas de **TinyML**.

## 3. Objetivo do projeto

Desenvolver e avaliar um pipeline de **odometria aprendida baseada em IMU**,
treinado no ROSbot do dataset MAGF-ID, com:

- modelos TinyML (baixo número de parâmetros),
- latência compatível com uso embarcado,
- saídas adequadas à fusão com filtros clássicos (EKF/complementar).

## 4. Escopo

Incluído:

- Uso do **ROSbot** do MAGF-ID como fonte principal de dados.
- Treino em **Python** e preparação para exportar modelos para TinyML.
- Estruturação de um caminho de **deploy em Go**, para uso futuro em robôs físicos.
- Foco em Δpose local (incrementos de curta duração), não em SLAM completo.

Excluído (neste projeto):

- Navegação global, SLAM e planejamento de caminho.
- Fusão com câmera ou LiDAR.
- Implementação de firmware produtivo em robôs comerciais.

## 5. Restrições e requisitos

- Modelo deve ser compatível com execução em hardware limitado (TinyML).
- Pipeline deve ser reprodutível e documentado (scripts, notebooks e configs).
- Dataset externo: MAGF-ID não será redistribuído neste repositório.

## 6. Métricas de sucesso (iniciais)

- **Erro médio de posição** ao reconstruir trajetórias (m/m ou % distância percorrida).
- **Erro angular médio** em Δθ.
- **Tamanho do modelo** (número de parâmetros, tamanho do arquivo exportado).
- **Tempo de inferência** em CPU comum (proxy para implementação embarcada).

## 7. Stakeholders e alinhamento com mercado

- Empresas de robótica e automação (Espanha/Portugal) que operam AMRs/AGVs.
- Laboratórios e cursos em robótica/navegação interessados em exemplos concretos de TinyML.
- Uso potencial futuro em protótipos com Arduino/ESP32/RPi.

