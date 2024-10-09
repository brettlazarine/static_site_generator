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
        new_nodes = split_nodes_image([text_node]) 
        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif")])

    def test_split_nodes_image_two_images(self):
        text_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)
        new_nodes = split_nodes_image([text_node])  
        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_split_nodes_link_one_link(self):
        text_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", text_type_text)
        new_nodes = split_nodes_link([text_node])  
        self.assertEqual(new_nodes, [TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev")])

    def test_split_nodes_link_two_links(self):
        text_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        new_nodes = split_nodes_link([text_node])  
        self.assertEqual(new_nodes, [TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and ", text_type_text), TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")])

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_not_text(self):
        old_node = TextNode("**Not a text node**", text_type_bold)
        new_nodes = split_nodes_delimiter([old_node], "**", text_type_bold)
        expected = [old_node]
        self.assertEqual(new_nodes, expected)

    def test_code(self):
        old_node = TextNode("This contains a `code` block", text_type_text)
        new_nodes = split_nodes_delimiter([old_node], "`", text_type_code)
        expected = [
            TextNode("This contains a ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" block", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    def test_bold(self):
        old_node = TextNode("This contains a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([old_node], "**", text_type_bold)
        expected = [
            TextNode("This contains a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic(self):
        old_node = TextNode("This contains an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([old_node], "*", text_type_italic)
        expected = [
            TextNode("This contains an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_trailing_words(self):
        old_node = TextNode("This contains a `code`", text_type_text)
        new_nodes = split_nodes_delimiter([old_node], "`", text_type_code)
        expected = [
            TextNode("This contains a ", text_type_text),
            TextNode("code", text_type_code),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_leading_words(self):
        old_node = TextNode("`code` block", text_type_text)
        new_nodes = split_nodes_delimiter([old_node], "`", text_type_code)
        expected = [
            TextNode("code", text_type_code),
            TextNode(" block", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_closing_delimiter(self):
        old_node = TextNode("This contains a `code block", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([old_node], "`", text_type_code)

    def test_no_opening_delimiter(self):
        old_node = TextNode("This contains a code` block", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([old_node], "`", text_type_code)

class TestTextToSplitNodes(unittest.TestCase):
    def test_text_to_split_nodes_one(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_split_nodes_two(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) and **bold**"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("bold", text_type_bold),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_split_nodes_three(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) and **bold** and *italic*"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic),
        ]
        self.assertEqual(nodes, expected)


if __name__ == "__main__":
    unittest.main()