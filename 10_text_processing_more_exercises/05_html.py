title_of_article = input()
content_of_article = input()

print("<h1>")
print("\t" + title_of_article)
print("</h1>")
print("<article>")
print("\t" + content_of_article)
print("</article>")

while True:
    command = input()
    if command == "end of comments":
        break
    print("<div>")
    print("\t" + command)
    print("</div>")

