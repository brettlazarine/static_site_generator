import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", text_type_image, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

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


if __name__ == "__main__":
    unittest.main()
