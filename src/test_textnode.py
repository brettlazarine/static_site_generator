import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)

    def test_eq_alternate_values(self):
        node = TextNode("Text", "italic")
        node2 = TextNode("Text", "italic")

        self.assertEqual(node, node2)

    def test_eq_different_text(self):
        node = TextNode("First node", "bold")
        node2 = TextNode("Second node", "bold")

        self.assertNotEqual(node, node2)

    def test_eq_different_type(self):
        node = TextNode("Text", "italic")
        node2 = TextNode("Text", "bold")

        self.assertNotEqual(node, node2)

    def test_eq_one_url(self):
        node = TextNode("Text", "italic")
        node2 = TextNode("Text", "italic", "urlgoeshere")

        self.assertNotEqual(node, node2)

    def test_eq_two_url(self):
        node = TextNode("Text", "italic", "urlgoeshere")
        node2 = TextNode("Text", "italic", "urlgoeshere")

        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Text", "bold", "url")
        repr = node.__repr__()
        expected = f"TextNode({node.text}, {node.text_type}, {node.url})"

        self.assertEqual(repr, expected)
    

if __name__ == "__main__":
    unittest.main()