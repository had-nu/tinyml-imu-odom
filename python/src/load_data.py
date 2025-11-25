"""
Data loading and initial exploration utilities for MAGF-ID dataset,
focusing on Project 1 (IMU-based TinyML Odometry).

Initial exploration script for MAGF-ID ROSBOT data (Project 1).

✓ Resolves dataset paths robustly
✓ Restricts to ROSBOT_Exp
✓ Loads CSVs
✓ Prints basic schema info for inspection
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
import numpy as np

# ======================== CONFIGURAÇÃO DE CAMINHOS ========================
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

DATA_ROOT = (SCRIPT_DIR / "../../data/raw/MAGF_ID_code_Data/").resolve()
DATA_DIR = DATA_ROOT / "Data"

PLATFORM_DIR = DATA_DIR / "ROSBOT_Exp"

CONFS_NAMES = ["Conf_1", "Conf_2", "Conf_3"]
CONFS_DIR = [PLATFORM_DIR / name for name in CONFS_NAMES]

MRU_DIR = "MRU"

# ======================== FUNÇÕES ========================
def dir_verify() -> None:
    print("=" * 70)
    print("VERIFICAÇÃO DA ESTRUTURA DO DATASET")
    print("=" * 70)
    
    print(f"Script: {SCRIPT_DIR}")
    print(f"Raiz do projeto: {PROJECT_ROOT}")
    print(f"Raiz dos dados: {DATA_ROOT}")

    print(f"Plataforma: {PLATFORM_DIR}\n")

    if not PLATFORM_DIR.is_dir():
        raise FileNotFoundError(f"[ERRO] Plataforma não encontrada: {PLATFORM_DIR}")
    tudo_ok = True

    for conf_path in CONFS_DIR:
        if conf_path.is_dir():
            print(f"  ✓ {conf_path.name}")
        else:
            print(f"  ✗ {conf_path.name} → PASTA NÃO EXISTE")
            tudo_ok = False
            continue

        # --- MRU ---
        mru_path = conf_path / MRU_DIR
        if mru_path.is_dir():
            arquivos = len(list(mru_path.glob("*.csv")))
            print(f"    ✓ MRU     → {arquivos} arquivo(s)")
        else:
            print(f"    ✗ MRU     → não encontrado")
            tudo_ok = False

    print("\n" + "="*70)
    if tudo_ok:
        print("PERFEITO! Toda a estrutura do dataset está correta e completa.")
        print("Pode prosseguir para carregamento dos dados.")
    else:
        print("ATENÇÃO: Há pastas ou arquivos faltando. Corrija antes de continuar.")
    print("="*70)


def load_all_mru(conf: str) -> pd.DataFrame:
    """
    Carrega todos os CSVs da pasta MRU de uma configuração (Conf_1, Conf_2, Conf_3),
    concatena tudo em um único DataFrame e adiciona metadados úteis.
    """

    conf_path = PLATFORM_DIR / conf
    if not conf_path.is_dir():
        raise FileNotFoundError(f"[ERRO] Configuração não encontrada: {conf_path}")

    mru_path = conf_path / MRU_DIR
    if not mru_path.is_dir():
        raise FileNotFoundError(f"[ERRO] Pasta MRU não encontrada: {mru_path}")

    csv_files = sorted(mru_path.glob("*.csv"))

    if len(csv_files) == 0:
        raise FileNotFoundError(f"[ERRO] Nenhum CSV encontrado em {mru_path}")

    print("=" * 60)
    print(f"Carregando {len(csv_files)} arquivos MRU para {conf}...")
    print("=" * 60)

    dfs = []

    # Carregar um por um
    for seq_id, csv_path in enumerate(csv_files, start=1):
        df = pd.read_csv(csv_path)
        df["config"] = conf
        df["file"] = csv_path.name
        df["seq_id"] = seq_id

        dfs.append(df)

        print(f"✓ {conf} | {csv_path.name} | {df.shape[0]:,} linhas")

    # Concatenar tudo
    df_final = pd.concat(dfs, ignore_index=True)
    df_final.name = f"{conf}_ALL_MRU"

    print("-" * 60)
    print(f"{conf}: Total final → {df_final.shape[0]:,} linhas x {df_final.shape[1]} colunas")
    print("-" * 60)

    return df_final


def main() -> None:
    try:
        dir_verify()
    except Exception as e:
        print(e)

    mru_conf1 = load_all_mru("Conf_1")
    print("-" * 70)
    print(mru_conf1.head())
    print("-" * 70)

    mru_conf2 = load_all_mru("Conf_2")
    print("-" * 70)
    print(mru_conf2.head())
    print("-" * 70)

    mru_conf3 = load_all_mru("Conf_3")
    print("-" * 70)
    print(mru_conf3.head())
    print("-" * 70)


if __name__ == "__main__":
    main()
