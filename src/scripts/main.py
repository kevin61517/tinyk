"""新電腦跑一次就裝完 Homebrew 環境。

用法:
    python install.py              # 用同目錄下的 Brewfile
    python install.py my_brewfile  # 指定檔案
"""
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    # 1. 確認 Homebrew 有裝
    if shutil.which("brew") is None:
        print("找不到 brew,請先安裝 Homebrew:https://brew.sh")
        return 1

    # 2. 找 Brewfile(參數指定,否則用同目錄的 Brewfile)
    brewfile = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "brewfile"
    print('brewfile===>', brewfile)
    if not brewfile.is_file():
        print(f"找不到檔案:{brewfile}")
        return 1

    # 3. 一次裝完(已裝好的會自動跳過,可重複執行)
    print(f"開始安裝 {brewfile} 裡的套件...\n")
    result = subprocess.run(["brew", "bundle", "install", f"--file={brewfile}"])

    print("\n完成!" if result.returncode == 0 else "\n有項目安裝失敗,詳見上方訊息。")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())