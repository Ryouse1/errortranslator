import re
import traceback

def normalize_error(text: str) -> str:
    text = text.strip().replace("\n", " ")
    text = re.sub(r'File ".*?", line \d+, ', "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def extract_last_frame(tb) -> str:
    frame = traceback.extract_tb(tb)[-1]
    return f'File "{frame.filename}", line {frame.lineno}'

def detect_error_type(text: str) -> str:
    m = re.search(r"(\w+Error)", text)
    return m.group(1) if m else "Error"
