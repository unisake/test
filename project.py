#!/usr/bin/env python3

import subprocess
from pathlib import Path

n = 2

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

print(m[n])

if input("push?[y/n]") == "y":

    # 自分自身を書き換える
    path = Path(__file__)
    text = path.read_text()

    new_n = n + 1

    text = text.replace(
        f"n = {n}",
        f"n = {new_n}",
        1
    )

    path.write_text(text)

    # 書き換えた状態をGitに登録
    subprocess.run(["git", "add", "."], check=True)

    subprocess.run(
        ["git", "commit", "-m", m[n]],
        check=True
    )

    subprocess.run(["git", "push"], check=True)