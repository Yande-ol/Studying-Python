"""loading.py

Load and analyze simulated Matrix data using numpy, pandas and matplotlib
when available. Handles missing dependencies gracefully and shows simple
installation instructions for pip and Poetry.
"""
from __future__ import annotations
from typing import Dict, List, Tuple, Union, TYPE_CHECKING

if TYPE_CHECKING:
    # pandas is optional at runtime; import only for type checking
    import pandas as _pd


DataLike = Union["_pd.DataFrame", List[Tuple[float, float]]]


REQUIRED = ["pandas", "numpy", "matplotlib"]


def check_dependencies() -> Dict[str, bool]:
    results: Dict[str, bool] = {}
    for pkg in REQUIRED + ["requests"]:
        try:
            __import__(pkg)
            results[pkg] = True
        except Exception:
            results[pkg] = False
    return results


def show_versions(installed: Dict[str, bool]) -> None:
    print("Checking dependencies:")
    for pkg in REQUIRED + ["requests"]:
        ok = installed.get(pkg, False)
        if ok:
            try:
                version = getattr(__import__(pkg), "__version__", "?")
            except Exception:
                version = "?"
            print(f"[OK] {pkg} ({version})")
        else:
            print(f"[MISSING] {pkg}")


def install_instructions() -> None:
    print("\nInstall with pip:")
    print("pip install -r requirements.txt")
    print("\nOr with Poetry:")
    print("poetry install")


def simulate_data(num: int = 1000) -> DataLike:
    import numpy as _np

    # simulate two features and a label
    x = _np.random.normal(loc=0.0, scale=1.0, size=num)
    y = _np.sin(x) + _np.random.normal(scale=0.1, size=num)
    df: DataLike
    try:
        import pandas as _pd

        df = _pd.DataFrame({"x": x, "y": y})
    except Exception:
        # fallback simple lists
        df = list(zip(x.tolist(), y.tolist()))
    return df


def analyze_and_plot(df) -> str:
    try:
        import pandas as _pd
        import matplotlib.pyplot as _plt

        if isinstance(df, list):
            df = _pd.DataFrame(df, columns=["x", "y"])

        # simple analysis
        summary = df.describe().to_string()
        print("Analyzing Matrix data...")
        print(summary)
        print("Generating visualization...")
        _plt.figure(figsize=(6, 4))
        _plt.scatter(df["x"], df["y"], s=4)
        _plt.title("Matrix simulation")
        _plt.xlabel("x")
        _plt.ylabel("y")
        out = "matrix_analysis.png"
        _plt.savefig(out)
        _plt.close()
        return out
    except Exception as exc:
        print(f"Cannot analyze/plot because: {exc}")
        return ""


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    deps = check_dependencies()
    show_versions(deps)

    missing = [p for p, ok in deps.items() if not ok and p in REQUIRED]
    if missing:
        print("\nMissing required dependencies:", ", ".join(missing))
        install_instructions()
        return

    df = simulate_data(1000)
    print("Processing 1000 data points...")
    out = analyze_and_plot(df)
    if out:
        print("Analysis complete!")
        print(f"Results saved to: {out}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - defensive
        print(f"ERROR: unexpected error: {exc}")
        raise
