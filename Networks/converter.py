import markdown
import sys

# Открывает файл Markdown
with open('networks.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Конвертирует Markdown в HTML
html = markdown.markdown(text)

# Сохраняет результат в HTML файл
with open('networks.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Конвертация завершена. Файл сохранён как 'example.html'")