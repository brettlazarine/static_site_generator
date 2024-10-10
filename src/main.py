from markdown import *
from textnode import *
from blockmarkdown import *


def main():
    markdown = """
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

This is a regular paragraph of text.

1. First item in an ordered list
2. Second item in an ordered list
3. Third item in an ordered list

- First item in an unordered list
- Second item in an unordered list
- Third item in an unordered list

This is a [link](https://example.com).

This is an image: ![alt text](https://example.com/image.png)

**Bold text** and *italic text*.

`Inline code` example.
"""
    print(markdown_to_html_node(markdown))


main()