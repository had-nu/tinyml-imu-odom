# TinyML Inertial Odometry for Indoor Robotics

> Aprendizagem de odometria baseada em IMU com foco em modelos TinyML e pipeline completo de engenharia.

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Go](https://img.shields.io/badge/go-1.21-cyan)](https://golang.org/)
[![Jupyter](https://img.shields.io/badge/jupyter-notebooks-orange)](https://jupyter.org/)
[![TensorFlow Lite Micro](https://img.shields.io/badge/TFLite-Micro-yellow)](https://www.tensorflow.org/lite/microcontrollers)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## About This Project

**tinyml-imu-odom** é um projeto educacional, técnico e incremental que estuda o ciclo completo de desenvolvimento de um modelo de *odometria aprendida (IMU → Δpose)* utilizando princípios de TinyML e metodologias inspiradas no pipeline profissional aplicado na engenharia de robôs móveis.

A iniciativa nasce dentro do contexto académico e avança para um nível pré-industrial, com documentação formal, fases estruturadas, experimentação rigorosa e comparação entre ambientes de treino (Python) e deploy (Go).

Aqui o objetivo não é “construir um modelo”, mas *aprender como um engenheiro constrói, valida e documenta um pipeline completo*, aplicável a cenários reais de navegação indoor sem GPS.

---

## Context & Motivation

Robôs que operam em ambientes *indoor* — fábricas, armazéns, corredores, zonas subterrâneas — não têm acesso a GPS. Neste contexto, a navegação depende de:

- sensores inerciais (IMUs),
- modelos capazes de estimar movimento incremental,
- pipelines eficientes e interpretáveis,
- capacidade de execução embarcada em hardware limitado.

O projeto utiliza como referência conceitual o *MAGF-ID – Multiple and Gyro-Free Inertial Dataset (2024)*, um dos datasets mais avançados em experimentos com IMU para robótica.  
Embora o MAGF-ID utilize múltiplas IMUs de alta precisão, GNSS-RTK e hardware robusto, neste repositório adotamos o mesmo rigor metodológico, porém em *escala TinyML*, com modelos leves, janelas pequenas e potencial de execução em microcontroladores.

---

## Three Complementary Perspectives

### 1. Pipeline completo de Engenharia de ML
O projeto segue um ciclo dividido em fases claras — Problem Definition → Data Acquisition → Exploratory Analysis → Modeling → Evaluation → Deploy — permitindo documentar cada decisão, hipótese e limitação do processo.

### 2. Uso do MAGF-ID como laboratório metodológico
O MAGF-ID fornece referência para:
- arquiteturas sensoriais,
- sincronização temporal,
- organização de dados inerciais,
- definição de ground truth,
- construção de Δpose supervisionado.

> *Este repositório não copia o MAGF-ID, mas usa seu rigor como padrão de qualidade.*

### 3. TinyML como forma técnica de síntese
Modelos pequenos exigem clareza física:
- interpretação correta das acelerações,
- integração de giroscópio,
- janelas temporais coerentes,
- features fisicamente significativas.

TinyML não pode ser pensado como um *“modelo pequeno para rodar em microcontroladores"*, mas como um mecanismo de destilação conceptual que reduz problemas complexos de navegação ao núcleo mínimo que pode ser resolvido de forma estável, explicável e eficiente. TinyML é uma restrição de engenharia: memória mínima, latência mínima, interpretabilidade máxima e estabilidade física. É aprender o que realmente importa para estimar movimento.

### 4. Python para pesquisa, Go para deploy
O ciclo se divide em:
- **Python** → exploração, treino e validação;
- **Go** → inferência embarcada, latência previsível e aplicações reais.

---

## Project Scope

O foco técnico imediato é:

- Construir um pipeline supervisionado para *Δpose local* (Δx, Δy, Δθ) a partir de janelas IMU.
- Treinar modelos *TinyML-compatíveis* (MLP/CNN/GRU pequenos).
- Preparar a infraestrutura para exportação do modelo (TFLite → Go).
- Realizar análise exploratória detalhada dos sinais do ROSbot no MAGF-ID.
- Construir documentação clara e incremental em `docs/` seguindo as fases da UC.

O projeto *não inclui*, nesta primeira versão:
- SLAM,
- mapeamento global,
- navegação completa,
- fusão com câmera ou LiDAR,
- firmware final para hardware real.

Esses tópicos são possíveis extensões futuras.

---

## Repository Structure

```
tinyml-imu-odom/
├── data/ # dados brutos e processados (não versionar raw)
├── docs/ # documentação por fases
├── ref/ # referências bibliográficas
├── python/ # notebooks, treino e experimentação
├── go/ # deploy e inferência em Go
├── models/ # artefatos de modelos (weights, tflite, etc.)
├── scripts/ # scripts auxiliares
└── README.md
```

---

## Status

Early-stage.  
Atualmente na *Fase 1 – Problem Definition* e organização da estrutura documental e experimental.

Próximos passos:

1. Registrar a definição do problema em `docs/01_problem_definition.md`.  
2. Documentar aquisição e organização dos dados em `docs/02_data_acquisition.md`.  
3. Iniciar a análise exploratória no notebook `01_explore_magfid_rosbot.ipynb`.

---

## License

MIT License — veja o arquivo LICENSE.
