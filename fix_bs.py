import os

FILE_PATH = r"s:\turboblocks-web\src\pages\checkout.astro"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("document.querySelector('.lg\\\\\\\\:col-span-7 section:first-of-type');", "document.querySelector('.lg\\\\:col-span-7 section:first-of-type');")
content = content.replace("document.querySelector('.lg\\\\\\\\:col-span-5');", "document.querySelector('.lg\\\\:col-span-5');")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Backslashes fixed.")
