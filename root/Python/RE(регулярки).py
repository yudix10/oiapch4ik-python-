import re
with open('text.txt', 'r', encoding='utf-8') as text:
	write_text = text.read()

title_words = re.findall(r'\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}', write_text)
print(title_words)

# шпора https://gist.github.com/mewforest/5e307ea347895350731cc3c02813b761#file-regular-expressions-md