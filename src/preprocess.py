import re

def normalize(text: str) -> str:
    # Preprocess text for inconsistent formatting
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip() # Replace whitespaces with single space and strip front/back whitespaces
    return text