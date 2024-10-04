from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("This is a test TextNode", "bold", "https://test")
    print(text_node)
    html_node = HTMLNode("div", "Hello World!", props={"class": "container"})
    print(html_node)


main()