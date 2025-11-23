# Contexto de Negócio & Definição do Problema

**Empresa:** RoboSense Labs  
**Projeto:** tinyml-imu-odom  
**Data:** Novembro de 2025  
**Versão:** 0.1

---

## 1. Contexto de Negócio

### 1.1. Perfil da Empresa

RoboSense Labs é uma empresa fictícia de P&D especializada em sistemas de propriocepção acessíveis para robótica móvel indoor. A empresa desenvolve soluções que permitem a robôs de baixo custo compreenderem seu próprio movimento utilizando sensores inerciais baratos, modelos TinyML e pipelines reprodutíveis que podem ser integrados em microcontroladores ou SBCs de pequena capacidade.

A tese empresarial é direta: não é necessário LiDAR para saber se um robô se moveu, parou, virou ou derrapou — quando o problema é estado local.

### 1.2. Contexto do Mercado

Robôs indoor na Europa (Espanha/Portugal, setor industrial/comercial) apresentam um cenário claro:

- PMEs não têm orçamento para sensores caros.
- A maioria dos AMRs opera em trajetórias repetitivas e previsíveis.
- A consciência de movimento (Δpose local) é suficiente para detecção de falhas, segurança e controle de execução.

O mercado está maduro para soluções robustas de baixo custo, especialmente para:

- AGVs simples,
- robots de logística,
- robots educacionais,
- AMRs de baixo volume.

---

## 2. Problema de Negócio

### 2.1. Custo desproporcional de percepção

O stack típico de percepção custa entre €2.000–€8.000 (LiDAR + IMU industrial). Para PMEs, isso inviabiliza migração para automação móvel.

### 2.2. Lacuna técnica

- IMUs baratas sofrem com ruído, drift e inconsistências.
- Não existem datasets amplos focados em Δpose curto usando IMUs baratas.
- Métodos clássicos (integração direta) são instáveis.
- TinyML ainda é subexplorado no domínio de odometria.

### 2.3. Lacuna operacional

Empresas querem saber se o robô está fazendo o que deveria fazer, não mapear o mundo.

Precisam de:

- confirmação de movimento,
- detecção de anomalias,
- validação de comandos,
- sinais de segurança.

---

## 3. Proposta de Solução (Valor da RoboSense)

A RoboSense Labs projeta um pipeline completo de odometria aprendida baseada em IMU, com:

- coleta padronizada inspirada no MAGF-ID,
- pipeline ML profissional (Python → inferência em Go),
- modelos TinyML leves,
- latência <10 ms,
- custo total de hardware < €10 na fase inicial.

A solução atende AMRs de baixo custo, robôs educacionais, AGVs simples e protótipos industriais.

---

## 4. Abordagem Técnica (Visão de Produto)

### 4.1. Arquitetura da solução

- IMU barata (MPU6050/9250)
- Amostragem ~100 Hz
- Janela temporal 100–300 ms
- Modelo compacto (MLP/CNN/GRU leve)
- Exportação p/ ONNX/TFLite Micro
- Inferência em Go com latência controlável

### 4.2. Diferencial competitivo

- Preço radicalmente baixo
- Pipeline transparente e reprodutível
- Orientado a indústria educacional e PMEs
- Transferível para Arduino/ESP32
- Pode evoluir para fusão sensorial na Fase 3

---

## 5. Objetivos de Negócio

### Primário

Produzir um sistema de classificação de movimento e estimativa de Δpose local com:

- F1-score > 0.90 nos estados principais,
- inferência < 10ms,
- modelo < 30MB,
- hardware < €10.

### Secundários

- Criar metodologia de coleta inspirada no MAGF-ID.
- Documentar todo o pipeline (acadêmico + empresarial).
- Comparar ambientes Python vs Go.
- Preparar terreno para fusão sensorial (IMU + ToF + ultrassônico).

---

## 6. Métricas de Sucesso

| Métrica | Meta | Essencial |
|---------|------|-----------|
| F1-score de classificação (IMU) | >0.90 | Sim |
| Latência p95 (Go) | <10ms | Sim |
| Tamanho do modelo | <30MB | Sim |
| Custo do hardware | <€10 | Sim |
| Reprodutibilidade do pipeline | Obrigatória | Sim |

---

## 7. Stakeholders

### Primários

- Engenheiros de robótica
- Equipes de automação industrial
- Educadores e laboratórios de navegação
- Pequenas empresas de robótica

### Secundários

- Estudantes
- Equipes de prototipagem rápida
- Comunidades de maker e educação técnica

---

## 8. Impacto de Negócio

### Financeiro

- Reduz drasticamente o custo de percepção.
- Torna AMRs de baixo custo comercialmente viáveis.

### Operacional

- Aumenta segurança (detecção rápida de anomalias).
- Permite auditoria de movimento de robôs simples.

### Estratégico

- Cria pipeline científico-industrial aberto.
- Estabelece base para produtos de fusão sensorial.
- Facilita adoção educacional e formação técnica.

---

## 9. Escopo (Fase 1 – Atual)

### Inclusões

- Classificação de movimento IMU-only
- Δpose local
- Treino Python + deploy Go
- Inspiração metodológica MAGF-ID

### Exclusões

- SLAM
- Navegação global
- LiDAR ou câmeras (somente fases futuras)

---

## 10. Restrições e Premissas

- Hardware de baixa potência (TinyML-friendly)
- Dataset próprio (MAGF-ID apenas para referência metodológica)
- Tempo limitado (projeto educacional/8 semanas)
- Orçamento extremamente reduzido

---

## 11. Roadmap Macro

### Fase 1 — Definição & Estruturação

- Documentação base
- Análise do MAGF-ID
- Protótipo IMU-only
- Treino inicial + comparação Python/Go

### Fase 2 — Coleta de Dados Próprios

- Protótipo físico
- Coleta sistemática
- Re-treino e ajustes

### Fase 3 — Fusão Sensorial

- IMU + ToF + ultrassônico
- Modelo multisensorial
- Validação em ambiente real