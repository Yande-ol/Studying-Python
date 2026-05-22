"""construct.py

Detect virtual environment and display environment information.
"""
from __future__ import annotations
import sys
import os
from typing import Optional


def in_virtualenv() -> Optional[str]:
    """Return the name/path of virtualenv if inside one.

    Returns None when no virtual environment is detected.
    """
    # Common indicators
    # sys.prefix differs from sys.base_prefix in venv/virtualenv
    base_prefix = getattr(sys, "base_prefix", None)
    prefix = getattr(sys, "prefix", None)
    if base_prefix and prefix and base_prefix != prefix:
        return prefix
    # VIRTUAL_ENV env var
    v = os.environ.get("VIRTUAL_ENV")
    if v:
        return v
    return None


def site_packages_path(py_prefix: str) -> str:
    """Return the site-packages path for the given python prefix.

    Construct a conventional path for standard venv layouts.
    """
    major = sys.version_info.major
    minor = sys.version_info.minor
    parts = (py_prefix, "lib", f"python{major}.{minor}", "site-packages")
    candidate = os.path.join(*parts)
    return str(candidate)


def print_outside() -> None:
    print("Outside the Matrix")
    print("MATRIX STATUS: You are still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You are in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate")
    print("# On Windows: matrix_env\\Scripts\\activate")
    print("Then run this program again.")


def print_inside(venv_path: str) -> None:
    print("Inside the Construct")
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    env_name = os.path.basename(venv_path.rstrip(os.sep))
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {venv_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("Package installation path:")
    print(site_packages_path(venv_path))


def main() -> None:
    v = in_virtualenv()
    if v is not None:
        print_inside(v)
    else:
        # Try to detect common system python path for display
        print_outside()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - defensive
        print(f"ERROR: unexpected error: {exc}")
        raise
