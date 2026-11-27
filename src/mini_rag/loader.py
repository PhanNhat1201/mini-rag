from pathlib import Path


def load_documents(folder: str) -> list[dict]:
    """Read all .txt and .md files in `folder` (UTF-8).

    Returns a list like [{"id": <file name>, "text": <content>}, ...],
    sorted by file name.
    """
    root = Path(folder)
    documents = []
    for item in sorted(root.iterdir(), key=lambda item: item.name):
        if item.suffix.lower() not in (".txt", ".md") or not item.is_file():
            continue
        documents.append({"id": item.name, "text": item.read_text(encoding="utf-8")})
    return documents
