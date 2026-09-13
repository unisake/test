#!/usr/bin/env python3

import subprocess
from pathlib import Path

m = [
    ]

print(m[0])

if input("push?[y/n]") == "y":

    # 自分自身を書き換える
    path = Path(__file__)
    text = path.read_text()

    text = text.replace(
        f"\"{m[0]}\",\n",
        "",
        1
    )

    path.write_text(text)

    # 書き換えた状態をGitに登録
    subprocess.run(["git", "add", "."], check=True)

    subprocess.run(
        ["git", "commit", "-m", m[0]],
        check=True
    )

    subprocess.run(["git", "push"], check=True)