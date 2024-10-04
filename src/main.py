from textnode import *


def main():
    code_node = TextNode("This is text with a `code block` word", text_type_text)
    new_code_nodes = split_nodes_delimiter([code_node], "`", text_type_code)
    print(new_code_nodes)
    bold_node = TextNode("This is text with a **bold word**", text_type_text)
    new_bold_nodes = split_nodes_delimiter([bold_node], "**", text_type_bold)
    print(new_bold_nodes)
    italic_node = TextNode("This is text with an *italic word*", text_type_text)
    new_italic_nodes = split_nodes_delimiter([italic_node], "*", text_type_italic)
    print(new_italic_nodes)


main()