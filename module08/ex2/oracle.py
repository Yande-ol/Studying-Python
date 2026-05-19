"""oracle.py

Load configuration from environment and from a .env file when available.
Demonstrates simple differences between development and production modes.
"""
from __future__ import annotations
import os
from typing import Dict


def load_env_file() -> None:
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except Exception:
        # dotenv not installed — skip but warn
        print("python-dotenv not installed; skipping .env file loading")


def get_config() -> Dict[str, str]:
    keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    cfg: Dict[str, str] = {}
    for k in keys:
        v = os.environ.get(k)
        if v is not None:
            cfg[k] = v
    return cfg


def print_status(cfg: Dict[str, str]) -> None:
    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix")
    mode = cfg.get("MATRIX_MODE", "development")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    db = cfg.get("DATABASE_URL")
    if db:
        print("Database: Connected to configured instance")
    else:
        print("Database: Not configured")
    if cfg.get("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API_KEY")
    print(f"Log Level: {cfg.get('LOG_LEVEL', 'INFO')}")
    print(f"Zion Network: {cfg.get('ZION_ENDPOINT', 'Unknown')}")


def security_check() -> None:
    print("Environment security check:")
    # naive checks
    # check for .env presence
    if os.path.exists(".env"):
        print("[OK] .env file present (ensure it is in .gitignore)")
    else:
        print("[WARN] .env file missing — using environment variables only")
    # check for obvious hardcoded secrets
    suspicious = False
    for root, _, files in os.walk("."):
        for f in files:
            if f.endswith(".py"):
                try:
                    path = os.path.join(root, f)
                    with open(path, "r", encoding="utf-8") as fh:
                        txt = fh.read()
                    if "API_KEY" in txt and "os.environ" not in txt:
                        suspicious = True
                except Exception:
                    continue
    if suspicious:
        print("[WARN] Potential hardcoded secret patterns found in code")
        print("Review files for accidental commits of secrets.")
    else:
        print("[OK] No hardcoded secrets detected")


def main() -> None:
    load_env_file()
    cfg = get_config()
    print_status(cfg)
    security_check()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - defensive
        print(f"ERROR: unexpected error: {exc}")
        raise
