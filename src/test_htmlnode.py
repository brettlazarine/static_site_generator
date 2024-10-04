import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_one_prop(self):
        node = HTMLNode("div", "Hello, World!", props={"class": "container"})
        props = node.props_to_html()
        expected = ' class="container"'

        self.assertEqual(props, expected)

    def test_two_props(self):
        node = HTMLNode("div", "Hello, World!", props={"class": "container", "id": "main"})
        props = node.props_to_html()
        expected = ' class="container" id="main"'

        self.assertEqual(props, expected)

    def test_three_props(self):
        node = HTMLNode("div", "Hello, World!", props={"class": "container", "id": "main", "style": "color: red;"})
        props = node.props_to_html()
        expected = ' class="container" id="main" style="color: red;"'

        self.assertEqual(props, expected)

    def test_repr(self):
        node = HTMLNode("div", "Hello, World!", props={"class": "container"})
        repr = node.__repr__()
        expected = f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})"

        self.assertEqual(repr, expected)

if __name__ == "__main__":
    unittest.main()