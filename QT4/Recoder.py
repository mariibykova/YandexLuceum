f = open('cyrillic.txt', 'r', encoding='utf-8')
result = open('transliteration.txt', 'w', encoding='utf-8')
 
lines = f.read()
 
mp = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
    "б": "b", "ю": "ju", "ё": "jo"
}
 
for char in lines:
    if char.lower() in mp:
        translit_char = mp[char.lower()]
 
        if char.isupper():
            translit_char = translit_char.capitalize()
 
        result.write(translit_char)
    else:
        result.write(char)