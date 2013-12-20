#!/usr/bin/env python

import re
from writeup.filters import markdown


with open('index.html', 'r') as f:
    template = f.read()

with open('README.md', 'r') as f:
    text = f.read()

text = '<body>\n<div class="yue">\n%s\n</div>\n</body>' % markdown(text)
html = re.sub(r'<body>.*</body>', text, template, flags=re.S)

with open('index.html', 'w') as f:
    f.write(html)
