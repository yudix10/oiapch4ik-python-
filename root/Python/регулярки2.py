import re

file = open('text.txt', 'r', encoding='utf-8')

read_file = file.read()

search_dates = r'\d{2}[-|\.|\/]?\d{2}[-|\.|\/]?\d{4}'
search_emails = r'[a-zA-Z0-9-!#]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+'
search_numbers = r'\+?[7|8][(|\s|\-]{,2}\d{3}[)|\-|\s]{,2}\d{3}-\d{2}-\d{2}'
search_URL = r'https?:\/\/[a-z0-9-]+\.[ru|org|com]+\/[a-z0-9_-]+'
search_IP = r'[\d]{,3}\.[\d]{,3}\.[\d]{,3}\.[\d]{,3}'
search_value = r'\$[\d]+\.\d+'

print(re.findall(search_dates, read_file))
print(re.findall(search_emails, read_file))
print(re.findall(search_numbers, read_file))
print(re.findall(search_URL, read_file))
print(re.findall(search_IP, read_file))
print(re.findall(search_value, read_file))