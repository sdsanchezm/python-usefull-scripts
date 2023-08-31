import re

def generate_table_of_content(content):
    toc = "## Table of Contents\n\n"
    headings = re.findall(r'^(#+)\s+(.+)$', content, flags=re.MULTILINE)
    
    for heading in headings:
        level, title = len(heading[0]), heading[1]
        indent = "  " * (level - 1)
        link = re.sub(r'[^\w\- ]', '', title.lower().replace(' ', '-'))
        toc += f"{indent}- [{title}](#{link})\n"
    
    return toc

def main():
    input_file = "README.md"
    output_file = "TableOfContent.md"

    with open(input_file, "r", encoding='utf-8') as file:
        content = file.read()

    toc = generate_table_of_content(content)

    with open(output_file, "w", encoding='utf-8') as file:
        file.write(content + "\n\n" + toc)

if __name__ == "__main__":
    main()
