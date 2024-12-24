import re
import urllib.request

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
response = urllib.request.urlopen(url)
html_content = response.read().decode()

pattern = r"(?:-link\">)(?P<name>[^<]+)(?:[^o]*[^l]*.*\n *)(?P<address>[^\n]+)(?:\s*.*>\s*.*>\s*.*>\s*<d[^>]*>\s*.*\s*.*>(?P<phone>[^<]+).*>\s*</dl>)?(?:\s*<.*>\s*<.*\s*<.*>(?P<workhours>[^<]+)</dd>)?"

match = re.findall(pattern, html_content)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Адрес', 'Номер', 'Время работы'])

    for i in match:
        writer.writerow(i)

matches = re.finditer(pattern, html_content)

for match in matches:
    print("Название:", match.group('name'))
    print("Адрес:", match.group('address'))
    print("Номер:", match.group('phone'))
    print("Время работы:", match.group('workhours'))
    print("\n")

if not re.search(pattern, html_content):
    print("No match found.")
