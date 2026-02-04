# errortranslator

Python の **英語エラーメッセージを自動的に翻訳して置き換える**ライブラリです。  
"try / except" や既存コードの修正は不要。  
**import 1行で、以降のエラー表示がすべて翻訳されます。**

---

## 📦 Install（インストール）

## bash
pip install errortranslator
## 🚀 使い方（最重要）
**✅ 基本の使い方**
Pythonファイルの一番上に、必ずこの2行を書く
from errortranslator import et
et(lang="ja")
その下は、いつも通りのPythonコードを書く
from errortranslator import et
et(lang="ja")

a = 10
print(b)
**✅ 実行結果**
File "test.py", line 6
NameError: 変数が定義されていません
英語のエラーメッセージは 一切表示されません
Python標準エラーを 完全に置き換え
try / except は不要
既存コードはそのまま使えます
**🌍 言語指定**
et(lang="ja")    # 日本語
et(lang="en")    # 英語
et(lang="ko")    # 韓国語
et(lang="zh")    # 中国語
et(lang="auto")  # 自動判定（Gemini）
**🔑 Gemini API の設定（翻訳品質アップ）**
ローカル / Colab（macOS / Linux）
export GEMINI_API_KEY="your_api_key"
Windows（PowerShell）
setx GEMINI_API_KEY "your_api_key"
GitHub Actions
Repository → Settings → Secrets → Actions
GEMINI_API_KEY を追加
env:
  GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
※ APIキーが無くても fallback（内蔵辞書）で動作します
**🛟 fallback について**
Gemini API が使えない場合でも、
以下のエラーは 内蔵辞書で翻訳されます。
NameError
SyntaxError
TypeError
IndexError
→ API未設定でもクラッシュしません
**⚙️ 仕組み**
sys.excepthook を置き換え
Pythonの全例外を自動キャッチ
エラーメッセージを整形（utils）
Gemini API で翻訳
翻訳後メッセージで 完全置換表示
🔥 上級者向け（毎回importしたくない人）
すべての Python 実行で自動的に有効にする場合：
export PYTHONSTARTUP="import errortranslator; errortranslator.et('ja')"
## 🧪 対応環境
Python 3.8 以上
ローカル実行
Google Colab
GitHub Actions
## 📄 License
MIT License
**💡 コンセプト**
「英語エラーが分からなくて止まる」をゼロにする。
初心者・学習用・独自言語（pypl）でも使える
Python エラー翻訳ランタイム。


---
