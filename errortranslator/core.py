import sys
import traceback
from .translator import translate_error
from .utils import normalize_error, extract_last_frame

_original_hook = sys.excepthook

def et(lang="auto", minimal=True):
    def hook(exc_type, exc, tb):
        raw = "".join(traceback.format_exception_only(exc_type, exc))
        clean = normalize_error(raw)
        translated = translate_error(clean, lang)

        if minimal:
            print(extract_last_frame(tb))
            print(f"{exc_type.__name__}: {translated}")
        else:
            print(translated)

    sys.excepthook = hook
