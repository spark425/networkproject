import urllib.request, urllib.parse, json #modules for HTTP requests, URL encoding, and JSON parsing

#starts function with word as parameter
def dictionary(word):
    word = word.strip()
    if not word:
        return #exit function if no word

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{urllib.parse.quote(word)}"
    try:
        with urllib.request.urlopen(url) as resp: #opens URL
            data = json.load(resp)
    except:
        return #exit function if error occurs

#start list that gets definitions
    definitions = [
        d.get("definition")
        for entry in data
        for m in entry.get("meanings", []) #meaning in entry
        for d in m.get("definitions", []) #definition in meaning
    ]

    if not definitions:
        print(f"No definitions found for '{word}'")
        return

#list gets definitions, numbers them, and prints them, max 10
    print(f"Definitions for '{word}':")
    for i, definition in enumerate(definitions[:10], 1):
        print(f"{i}. {definition}")
        
#ask for user input and call function
if __name__ == "__main__":
    user_word = input("Enter an English word: ")
    dictionary(user_word)