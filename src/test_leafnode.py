import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = LeafNode("Hello, World!")
        html = node.to_html()
        expected = "Hello, World!"

        self.assertEqual(html, expected)

    def test_to_html_with_tag(self):
        node = LeafNode("Hello, World!", "div")
        html = node.to_html()
        expected = "<div>Hello, World!</div>"

        self.assertEqual(html, expected)

    def test_to_html_with_props(self):
        node = LeafNode("Hello, World!", "div", {"class": "container"})
        html = node.to_html()
        expected = '<div class="container">Hello, World!</div>'

        self.assertEqual(html, expected)

    def test_to_html_with_multiple_props(self):
        node = LeafNode("Hello, World!", "div", {"class": "container", "id": "main"})
        html = node.to_html()
        expected = '<div class="container" id="main">Hello, World!</div>'

        self.assertEqual(html, expected)

    def test_to_html_with_props_no_tag(self):
        node = LeafNode("Hello, World!", props={"class": "container"})
        html = node.to_html()
        expected = "Hello, World!"

        self.assertEqual(html, expected)

    def test_to_html_no_value(self):
        node = LeafNode("", "div")
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()