def wordCount(file) :
    num_words = len(file.split())
    print(f"Found {num_words} total words")

def characterCount(file) :
    chars = {}
    for i in file:
        lowered = i.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]


def list(num_chars):
    sorted = []
    for ch in num_chars:
        sorted.append({"char": ch, "num": num_chars[ch]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted