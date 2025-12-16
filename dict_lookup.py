import urllib.request
import urllib.error
import urllib.parse
import json


def lookup(word: str):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{urllib.parse.quote(word)}"
    try:
        with urllib.request.urlopen(url) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise

    definitions = []
    for entry in data:
        for meaning in entry.get("meanings", []):
            part = meaning.get("partOfSpeech", "")
            for d in meaning.get("definitions", []):
                definitions.append({
                    "part": part,
                    "definition": d.get("definition"),
                    "example": d.get("example"),
                })
    return definitions


def main():
    word = input("Enter an English word: ").strip()
    if not word:
        print("No word entered.")
        return

    defs = lookup(word)
    if not defs:
        print(f"No definitions found for '{word}'.")
        return

    print(f"Definitions for '{word}':")
    for i, d in enumerate(defs[:10], start=1):
        part = f"({d['part']}) " if d['part'] else ""
        print(f"{i}. {part}{d['definition']}")
        if d.get('example'):
            print(f"   Example: {d['example']}")


if __name__ == '__main__':
    main()
