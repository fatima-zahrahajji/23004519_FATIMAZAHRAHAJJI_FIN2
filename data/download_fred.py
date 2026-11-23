"""Télécharge GDPC1 et UNRATE depuis l'export CSV public de FRED.

Usage : python data/raw/download_fred.py
Écrit GDPC1.csv, UNRATE.csv et extraction_log.txt dans le dossier de ce script.
"""
import datetime as dt
import urllib.request
from pathlib import Path

SERIES = ["GDPC1", "UNRATE"]
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
OUT = Path(__file__).resolve().parent


def main() -> None:
    lines = []
    for code in SERIES:
        url = URL.format(code)
        with urllib.request.urlopen(url, timeout=60) as resp:
            content = resp.read()
        (OUT / f"{code}.csv").write_bytes(content)
        n_rows = max(content.count(b"\n") - 1, 0)
        lines.append(f"{code} : {url} ; {n_rows} lignes")
        print(lines[-1])
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    (OUT / "extraction_log.txt").write_text(
        f"Date d'extraction : {stamp}\n" + "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
