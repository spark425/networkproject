def dictionary():
    #Step 1: ask for english word
    word = input("Enter an English word: ")

    #Step 2: put in website
    random_url = "https://www.dictionary.com/browse/"
    full_url = random_url + word
    print(f"Look up the definition of '{word}' at: {full_url}")

    #Step 3: print definition link
    print(f"Definition link for '{word}': {full_url}")
    