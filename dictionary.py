import urllib.request
import urllib.error
import urllib.parse
import json

def dictionary():
    word = input("Enter an English word: ").strip()
    if not word:
        print("No word entered.")
        return

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{urllib.parse.quote(word)}"
    try:
        with urllib.request.urlopen(url) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"No definition found for '{word}'.")
            return
        print(f"HTTP error {e.code}: {e.reason}")
        return
    except Exception as e:
        print(f"Error fetching definition: {e}")
        return

    definitions = []
    for entry in data:
        for meaning in entry.get("meanings", []):
            part = meaning.get("partOfSpeech", "")
            for d in meaning.get("definitions", []):
                definitions.append((part, d.get("definition"), d.get("example")))

    if not definitions:
        print(f"No definitions found for '{word}'.")
        return

    print(f"Definitions for '{word}':")
    for i, (part, definition, example) in enumerate(definitions[:10], start=1):
        part_str = f"({part}) " if part else ""
        print(f"{i}. {part_str}{definition}")
        if example:
            print(f"   Example: {example}")


if __name__ == "__main__":
    dictionary()