import unittest
from blockmarkdown import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_multi(self):
        markdown = """
        # This is a header

        This is a paragraph with **bold** and *italic* words and a [link](https://boot.dev) and an ![image](https://i.imgur.com/fJRm4Vk.jpeg)
        
        * This is first
        * This is second
        * This is third
        """
        blocks = markdown_to_blocks(markdown)
        expected = ['# This is a header', 'This is a paragraph with **bold** and *italic* words and a [link](https://boot.dev) and an ![image](https://i.imgur.com/fJRm4Vk.jpeg)', '* This is first', '* This is second', '* This is third']
        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_single(self):
        markdown = "# This is a header"
        blocks = markdown_to_blocks(markdown)
        expected = ['# This is a header']
        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_empty(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        expected = []
        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_excessive_whitespace(self):
        markdown = """
             # This is a header
             * This is a list

             * Also a list

        """
        blocks = markdown_to_blocks(markdown)
        expected = ['# This is a header', '* This is a list', '* Also a list']
        self.assertEqual(blocks, expected)


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        expected = heading
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_not_heading(self):
        block = "#This is a paragraph"
        block_type = block_to_block_type(block)
        expected = paragraph
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_code(self):
        block = "```\nThis is code\n```"
        block_type = block_to_block_type(block)
        expected = code
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_not_code_start(self):
        block = "```This is not code"
        block_type = block_to_block_type(block)
        expected = paragraph
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_not_code_end(self):
        block = "This is not code```"
        block_type = block_to_block_type(block)
        expected = paragraph
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_quote_single(self):
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        expected = quote
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_quote_multi(self):
        block = """
        > This is a quote
        > This is another quote
        """
        block_type = block_to_block_type(block)
        expected = quote
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_not_quote(self):
        block = """
        > Quote line
        This is not a quote
        """
        block_type = block_to_block_type(block)
        expected = paragraph
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_unordered_list_single(self):
        block = "* This is a list"
        block_type = block_to_block_type(block)
        expected = unordered_list
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_unordered_list_multi(self):
        block = """
        * This is a list
        * This is another list
        """
        block_type = block_to_block_type(block)
        expected = unordered_list
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_not_unordered_list(self):
        block = """
        * List item
        This is not a list
        """
        block_type = block_to_block_type(block)
        expected = paragraph
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_ordered_list_single(self):
        block = "1. This is a list"
        block_type = block_to_block_type(block)
        expected = ordered_list
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_ordered_list_multi(self):
        block = """
        1. This is a list
        2. This is another list
        """
        block_type = block_to_block_type(block)
        expected = ordered_list
        self.assertEqual(block_type, expected)
    def test_block_to_block_type_not_ordered_list(self):
        block = """
        1. List item
        This is not a list
        """
        block_type = block_to_block_type(block)
        expected = paragraph
        self.assertEqual(block_type, expected)


if __name__ == '__main__':
    unittest.main()