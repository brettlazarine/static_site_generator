import unittest
from markdown import *

class TestMarkdown(unittest.TestCase):
    def test_extract_markdown_images_one_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

    def test_extract_markdown_images_two_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_links_one_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("to boot dev", "https://www.boot.dev")])

    def test_extract_markdown_links_two_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])


    def test_split_nodes_image_one_image(self):
        text_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", text_type_text)
        new_nodes = split_nodes_image(text_node)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif")])

    def test_split_nodes_image_two_images(self):
        text_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)
        new_nodes = split_nodes_image(text_node)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_split_nodes_link_one_link(self):
        text_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", text_type_text)
        new_nodes = split_nodes_link(text_node)
        self.assertEqual(new_nodes, [TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev")])

    def test_split_nodes_link_two_links(self):
        text_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        new_nodes = split_nodes_link(text_node)
        self.assertEqual(new_nodes, [TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and ", text_type_text), TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")])
        


if __name__ == "__main__":
    unittest.main()