#!/usr/bin/env python3

import subprocess
from pathlib import Path

n = 0

m = [
    """
    目標1
    """,

    """
    目標2
    """,

    """
    目標3
    """
]

print(m[n])  # 目標の確認

if input("push?[y/n]") == "y":

    subprocess.run(["git", "add", "."], check=True)

    subprocess.run(
        ["git", "commit", "-m", m[n]],
        check=True
    )

    subprocess.run(["git", "push"], check=True)

    # 自分自身を書き換える
    path = Path(__file__)
    text = path.read_text()

    new_n = n + 1

    text = text.replace(
        f"n = {n}",
        f"n = {new_n}",
        1
    )