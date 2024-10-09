from markdown import *
from textnode import *
from blockmarkdown import *


def main():
    markdown = """
> This is a quote
> This is another quote
    """
    print(block_to_block_type(markdown))


main()