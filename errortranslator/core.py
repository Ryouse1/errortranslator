import sys
import traceback
from .translator import translate_error

_original_hook = sys.excepthook

def et(lang="auto", minimal=True):
    def hook(exc_type, exc, tb):
        raw = "".join(traceback.format_exception_only(exc_type, exc)).strip()
        msg = translate_error(raw, lang=lang)

        if minimal:
            last = traceback.extract_tb(tb)[-1]
            print(f'File "{last.filename}", line {last.lineno}')
            print(f"{exc_type.__name__}: {msg}")
        else:
            print(msg)

    sys.excepthook = hook
