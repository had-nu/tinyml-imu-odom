# Fase 2 – Aquisição e Organização dos Dados  
**Projeto:** tinyml-imu-odom  
**Dataset Base:** MAGF-ID (Subset ROSBOT)  
**Versão:** 0.1 – Novembro/2025  

---

## 1. Objetivo da Fase

Esta fase documenta como os dados inerciais do MAGF-ID (Multiple and Gyro-Free Inertial Dataset, 2024) são:

- localizados dentro da estrutura do repositório,
- verificados para consistência e completude,
- carregados para o pipeline de exploração e pré-processamento,
- organizados de forma padronizada para uso nos experimentos de odometria TinyML.

O foco é o subcomponente MRU do ROSBOT, contendo séries temporais de leituras IMU.

---

## 2. Fonte e Estrutura do Dataset

O MAGF-ID possui diversas plataformas e modalidades experimentais.  
Para o Projeto 1 utilizamos exclusivamente:

```
MAGF_ID_code_Data/
└── Data/
└── ROSBOT_Exp/
├── Conf_1/
│ └── MRU/
├── Conf_2/
│ └── MRU/
└── Conf_3/
└── MRU/
```

### Justificativa do Subset
- O ROSBOT é a plataforma com arquitetura mais próxima do protótipo do Projeto 1 (IMU → Δpose).
- As três configurações (Conf_1, Conf_2, Conf_3) permitem avaliar consistência entre trajetórias.
- O componente MRU contém os sinais crus e contínuos de IMU necessários para janelamento.

---

## 3. Caminhos e Ancoragem no Repositório

A organização interna do código foi feita para ser robusta a mudanças na raiz do projeto.  
A ancoragem é:

- `SCRIPT_DIR` → diretório do script ativo  
- `PROJECT_ROOT` → raiz do repositório  
- `DATA_ROOT` → raiz do dataset MAGF-ID dentro de `data/raw/`  

O arquivo Python monta automaticamente os caminhos para:

- `ROSBOT_Exp`
- `Conf_1`, `Conf_2`, `Conf_3`
- subdiretório `MRU` em cada configuração

---

## 4. Verificação Estrutural (Função `dir_verify()`)

Antes de carregar qualquer dado, a estrutura completa é validada:

- existência de `ROSBOT_Exp/`
- existência de todas as configurações definidas (`Conf_1–3`)
- existência da subpasta `MRU/` em cada configuração
- existência de pelo menos um arquivo `.csv` dentro de cada MRU

Saída esperada:
```
✓ Conf_1
  ✓ MRU → 27 arquivo(s)
✓ Conf_2
  ✓ MRU → 22 arquivo(s)
✓ Conf_3
  ✓ MRU → 19 arquivo(s)
```

Caso algo esteja faltando, o processo é interrompido com uma mensagem clara.

---

## 5. Carregamento dos Dados (Função `load_mru(conf)`)

Cada configuração é carregada individualmente através da função:

```python
df = load_mru("Conf_1")
```
A função:

1. monta o caminho completo da configuração,
2. valida a existência da pasta e da subpasta MRU,
3. localiza os arquivos `.csv`,
4. carrega o primeiro CSV encontrado como DataFrame,
5. atribui um nome ao DataFrame (`Conf_1_MRU`),
6. imprime estatísticas básicas de linhas e colunas.

Este padrão garante:

- previsibilidade,
- simplicidade no diagnóstico,
- compatibilidade com futuras funções de janelamento.

---

## 6. Organização dos Dados para EDA

Após o carregamento individual, os DataFrames podem ser:

- analisados separadamente,
- concatenados com uma coluna `config` indicando a origem,
- sincronizados ou recortados para janelas uniformes.

A próxima etapa será implementada na *Fase 3 - Exploratory Data Analysis – EDA)*.

---

## 7. Premissas Técnicas

- Cada configuração (`Conf_1`, `Conf_2`, `Conf_3`) contém diversos arquivos CSV dentro da pasta `MRU/`.  
- Esses arquivos representam múltiplas capturas independentes ou segmentos gravados separadamente da trajetória do robô.
- A contagem atual é:
  - **Conf_1 → 27 CSVs**
  - **Conf_2 → 22 CSVs**
  - **Conf_3 → 19 CSVs**
- Cada CSV corresponde a uma sequência temporal própria, contendo leituras IMU completas (acelerações + giroscópio).
- A lógica do pipeline deverá:
  - tratar cada CSV como uma “instância de movimento”, *ou*
  - concatená-los em ordem, caso seja necessário formar trajetórias maiores.
- A decisão final dependerá da análise exploratória (Fase 3), onde verificaremos:
  - consistência das colunas,
  - timestamps disponíveis,
  - continuidade temporal,
  - presença ou ausência de sincronização entre arquivos,
  - possíveis quebras ou reinícios de gravação.

---

## 8. Próximos Passos

A Fase 3 será dedicada à análise dos sinais:

- inspeção de colunas disponíveis,
- limpeza e normalização,
- plotagem dos eixos de aceleração e giroscópio,
- cálculo de frequência efetiva,
- detecção de inconsistências ou saturações,
- preparação do janelamento para modelos TinyML.

---

**Status:**
Fase 2 concluída após criação deste documento.
Projeto avança para *Fase 3 – Análise Exploratória*.

---