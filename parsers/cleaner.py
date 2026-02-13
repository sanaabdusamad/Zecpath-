import re

def clean_text(text: str) -> str:
    """
    Cleans and normalizes extracted resume text
    """

    if not text:
        return ""

    # 1. Remove unwanted symbols (non-ASCII)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # 2. Replace multiple spaces/tabs with single space
    text = re.sub(r"[ \t]+", " ", text)

    # 3. Normalize new lines (avoid too many blank lines)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 4. Normalize bullet points
    text = text.replace("•", "-")
    text = text.replace("▪", "-")
    text = text.replace("●", "-")

    # 5. Remove trailing spaces in each line
    lines = [line.strip() for line in text.split("\n")]

    # 6. Join back cleaned lines
    cleaned_text = "\n".join(lines)

    return cleaned_text.strip()