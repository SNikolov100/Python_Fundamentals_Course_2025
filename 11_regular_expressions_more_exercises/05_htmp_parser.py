import re

manipulate_html = []
entered_html = input()
extracted_content = ""
pattern_title = r"<title>(.*?)<\/title>"
pattern_body = r"<body>(.*?)<\/body>"
pattern_content = r"([^>]+)<"
title = re.search(pattern_title, entered_html)

if title:
    delete_text = title.group(0)
    entered_html = entered_html.replace(delete_text, "")
    manipulate_html.append(title.group(1))

temp_body = re.search(pattern_body, entered_html)

if temp_body:
    body = temp_body.group()
    temp_content = re.findall(pattern_content, body)
    for data in temp_content:
        data = data.replace("\\n", "")
        manipulate_html.append(data)
print(f"Title: {manipulate_html[0]}")
for index in range(1, len(manipulate_html)):
    extracted_content += manipulate_html[index]

print(f"Content: {extracted_content}")


