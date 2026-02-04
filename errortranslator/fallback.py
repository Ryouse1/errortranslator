ERROR_MAP = {
    "NameError": {
        "ja": "変数が定義されていません",
        "en": "Variable is not defined"
    },
    "SyntaxError": {
        "ja": "文法エラーがあります",
        "en": "Syntax error"
    },
    "TypeError": {
        "ja": "型が正しくありません",
        "en": "Invalid type"
    }
}

def fallback_translate(text, lang):
    for key, langs in ERROR_MAP.items():
        if key in text:
            return langs.get(lang, langs["en"])
    return "エラーが発生しました"
