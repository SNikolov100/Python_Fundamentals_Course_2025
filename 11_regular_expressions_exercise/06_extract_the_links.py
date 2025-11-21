import re


pattern = r"((www\.)([a-z0-9\-]+)(\.[a-z]+)+\b)"

while True:
    entered_sentences = input()
    if not entered_sentences:
        break
    links = re.finditer(pattern, entered_sentences, re.IGNORECASE)
    for link in links:
        print(link.group(0))
