import sys

class HTMLParser:
    def __init__(self):
        self.stack = []

    def is_valid_html(self, html):
        self.stack = [] 
        i = 0
        while i < len(html):
            if html[i] == '<':
                j = i + 1
                while j < len(html) and html[j] != '>':
                    j += 1
                if j == len(html):
                    return False  # Invalid tag

                tag = html[i + 1:j]
                if tag[0] != '/':
                    self.stack.append(tag)
                else:
                    if not self.stack or self.stack[-1] != tag[1:]:
                        return False
                    self.stack.pop()
                i = j
            i += 1
        return len(self.stack) == 0

    def is_valid_html_structure(self, html):
        if not self.is_valid_html(html):
            return False
        if '<html>' not in html or '</html>' not in html:
            return False
        head_start = html.find('<head>')
        head_end = html.find('</head>')
        body_start = html.find('<body>')
        body_end = html.find('</body>')

        if head_start != -1 and (head_end == -1 or head_end < head_start):
            return False
        if body_start != -1 and (body_end == -1 or body_end < body_start):
            return False
        if head_end != -1 and body_start != -1 and head_end > body_start:
            return False

        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python program.py input.html")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        html = file.read()

    parser = HTMLParser()
    result = parser.is_valid_html_structure(html)
    print(f"Input file {input_file}: {'Accepted' if result else 'Rejected'}")
