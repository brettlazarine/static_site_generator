from markdown import *
from textnode import *


def main():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    node1 = TextNode(text, text_type_text)
    print(split_nodes_image(node1))
    #print(extract_markdown_images(text))
    text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    node2 = TextNode(text2, text_type_text)
    print(split_nodes_link(node2))
    #print(extract_markdown_links(text2))

main()