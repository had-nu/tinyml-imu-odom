"""
Data loading and initial exploration utilities for MAGF-ID dataset,
focusing on Project 1 (IMU-based TinyML Odometry).

Initial exploration script for MAGF-ID ROSBOT data (Project 1).

✓ Resolves dataset paths robustly
✓ Restricts to ROSBOT_Exp
- Loads CSVs
- Prints basic schema info for inspection
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
import numpy as np

# ======================== CONFIGURAÇÃO DE CAMINHOS ========================
BASE_DIR = Path(__file__).resolve().parent
DATA_ROOT = (BASE_DIR / "../../data/raw/MAGF_ID_code_Data").resolve()
DATA_DIR = DATA_ROOT / "Data"

PLATFORM_DIR = DATA_DIR / "ROSBOT_Exp"

CONFS_NAMES = ["Conf_1", "Conf_2", "Conf_3"]
CONFS_DIR = [PLATFORM_DIR / name for name in CONFS_NAMES]

MRU_DIR = "MRU"
DOTS_DIR = 'DOTs'

DOTS_SUBDIRS_EXPECTED = ["Ceiling", "Top", "Bottom"]

# ======================== FUNÇÕES ========================
def dir_verify() -> None:
    print("=" * 70)
    print("VERIFICAÇÃO DA ESTRUTURA DO DATASET")
    print("=" * 70)
    
    print(f"Script: {BASE_DIR}")
    print(f"Dataset raiz: {DATA_ROOT}")
    print(f"Plataforma: {PLATFORM_DIR}\n")

    if not PLATFORM_DIR.is_dir():
        raise FileNotFoundError(f"[ERRO] Plataforma não encontrada: {PLATFORM_DIR}")

    tudo_ok = True

    for conf_path in CONFS_DIR:
        if not conf_path.is_dir():
            print(f"  ✗ {conf_path.name} → PASTA NÃO EXISTE")
            tudo_ok = False
            continue

        print(f"  ✓ {conf_path.name}")

        # --- MRU ---
        mru_path = conf_path / MRU_DIR
        if mru_path.is_dir():
            arquivos = len(list(mru_path.glob("*.csv")))
            print(f"    ✓ MRU     → {arquivos} arquivo(s)")
        else:
            print(f"    ✗ MRU     → não encontrado")
            tudo_ok = False

        # --- DOTs ---
        dots_path = conf_path / DOTS_DIR
        if not dots_path.is_dir():
            print(f"    ✗ DOTs    → não encontrado")
            tudo_ok = False
            continue

        print(f"    ✓ DOTs")
        for sub in DOTS_SUBDIRS_EXPECTED:
            sub_path = dots_path / sub
            if sub_path.is_dir():
                arquivos = len(list(sub_path.glob("*.*")))
                print(f"      ✓ {sub:<8} → {arquivos} arquivo(s)")
            else:
                print(f"      ✗ {sub} → FALTANDO")
                tudo_ok = False

    print("\n" + "="*70)
    if tudo_ok:
        print("PERFEITO! Toda a estrutura do dataset está correta e completa.")
        print("Pode prosseguir para carregamento dos dados.")
    else:
        print("ATENÇÃO: Há pastas ou arquivos faltando. Corrija antes de continuar.")
    print("="*70)


def load_mru(conf: str) -> pd.DataFrame:
    conf_path = PLATFORM_DIR / conf
    if not conf_path.is_dir():
        raise FileNotFoundError(f"[ERRO] Configuração não encontrada: {conf_path}")

    mru_path = conf_path / MRU_DIR
    if not mru_path.is_dir():
        raise FileNotFoundError(f"[ERRO] Pasta MRU não encontrada: {mru_path}")

    csv_files = list(mru_path.glob("*.csv"))

    if len(csv_files) == 0:
        raise FileNotFoundError(f"Nenhum CSV encontrado em {mru_path}")
    if len(csv_files) > 1:
        print(f"[AVISO] Múltiplos CSVs em {mru_path}. Usando o primeiro: {csv_files[0].name}")

    df = pd.read_csv(csv_files[0])
    df.name = f"{conf}_MRU"
    print(f"✓ {df.name}: {df.shape[0]:,} linhas x {df.shape[1]} colunas")
    
    return df


def main() -> None:
    try:
        dir_verify()
    except Exception as e:
        print(e)

    mru_conf1 = load_mru("Conf_1")
    print(mru_conf1.head())

    mru_conf2 = load_mru("Conf_2")
    print(mru_conf2.head())

    mru_conf3 = load_mru("Conf_3")
    print(mru_conf3.head())


if __name__ == "__main__":
    main()
