import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestMarkDownNode(unittest.TestCase):
    def test_eq1(self):
        old_nodes = [TextNode("This is a text node", TextType.BOLD)]
        res_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        exp_nodes = [TextNode("This is a text node", TextType.BOLD)]
        self.assertEqual(res_nodes, exp_nodes)

    def test_code_text(self):
        old_nodes = [TextNode("This is a text node", TextType.BOLD),
                     TextNode("This is a code node", TextType.CODE),
                     TextNode("This is a `code` node", TextType.TEXT),
                     TextNode("This is a **bold** node", TextType.TEXT),
                     TextNode("This is an _italic_ node", TextType.TEXT)]
        
        res_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        
        exp_nodes = [TextNode("This is a text node", TextType.BOLD),
                     TextNode("This is a code node", TextType.CODE),
                     TextNode("This is a ", TextType.TEXT), 
                     TextNode("code", TextType.CODE),
                     TextNode(" node", TextType.TEXT),
                     TextNode("This is a **bold** node", TextType.TEXT),
                     TextNode("This is an _italic_ node", TextType.TEXT)]
    
        self.assertEqual(res_nodes, exp_nodes)

    def test_bold_text(self):
        old_nodes = [TextNode("This is a text node", TextType.BOLD),
                     TextNode("This is a code node", TextType.CODE),
                     TextNode("This is a `code` node", TextType.TEXT),
                     TextNode("This is a **bold** node", TextType.TEXT),
                     TextNode("This is an _italic_ node", TextType.TEXT)]
        
        res_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        
        exp_nodes = [TextNode("This is a text node", TextType.BOLD),
                     TextNode("This is a code node", TextType.CODE),
                     TextNode("This is a `code` node", TextType.TEXT), 
                     TextNode("This is a ", TextType.TEXT),
                     TextNode("bold", TextType.BOLD),
                     TextNode(" node", TextType.TEXT),
                     TextNode("This is an _italic_ node", TextType.TEXT)]
    
        self.assertEqual(res_nodes, exp_nodes)

    def test_italic_text(self):
        old_nodes = [TextNode("This is a text node", TextType.BOLD),
                     TextNode("This is a code node", TextType.CODE),
                     TextNode("This is a `code` node", TextType.TEXT),
                     TextNode("This is a **bold** node", TextType.TEXT),
                     TextNode("This is an _italic_ node", TextType.TEXT)]
        
        res_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        
        exp_nodes = [TextNode("This is a text node", TextType.BOLD),
                     TextNode("This is a code node", TextType.CODE),
                     TextNode("This is a `code` node", TextType.TEXT), 
                     TextNode("This is a **bold** node", TextType.TEXT),
                     TextNode("This is an ", TextType.TEXT),
                     TextNode("italic", TextType.ITALIC),
                     TextNode(" node", TextType.TEXT),]
    
        self.assertEqual(res_nodes, exp_nodes)

    def test_double_delimiter_P1(self):
        old_nodes = [TextNode("This is a text node", TextType.BOLD),
                     TextNode("This is a code node", TextType.CODE),
                     TextNode("This is a `code` node", TextType.TEXT),
                     TextNode("This is a **bold** node", TextType.TEXT),
                     TextNode("This is an _italic_ node", TextType.TEXT),
                     TextNode("This is a `double` delimited `code` node", TextType.TEXT)]

        res_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        exp_nodes = [TextNode("This is a text node", TextType.BOLD),
                     TextNode("This is a code node", TextType.CODE),
                     TextNode("This is a ", TextType.TEXT), 
                     TextNode("code", TextType.CODE),
                     TextNode(" node", TextType.TEXT),
                     TextNode("This is a **bold** node", TextType.TEXT),
                     TextNode("This is an _italic_ node", TextType.TEXT),
                     TextNode("This is a ", TextType.TEXT),
                     TextNode("double", TextType.CODE),
                     TextNode(" delimited ", TextType.TEXT), 
                     TextNode("code", TextType.CODE),
                     TextNode(" node", TextType.TEXT),]
        self.assertEqual(res_nodes, exp_nodes)
    
    def test_no_delimit(self):
        old_nodes = [TextNode("This is a text node", TextType.TEXT)]
        res_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        exp_nodes = [TextNode("This is a text node", TextType.TEXT)]
        self.assertEqual(res_nodes, exp_nodes)

    def test_empty_element1(self):
        old_nodes = [TextNode("This is a text **node**", TextType.TEXT)]
        res_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        exp_nodes = [TextNode("This is a text ", TextType.TEXT),
                     TextNode("node", TextType.BOLD)]
        self.assertEqual(res_nodes, exp_nodes)

    def test_empty_element2(self):
        old_nodes = [TextNode("**This** is a text node", TextType.TEXT)]
        res_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        exp_nodes = [TextNode("This", TextType.BOLD),
                     TextNode(" is a text node", TextType.TEXT)]
        self.assertEqual(res_nodes, exp_nodes)

    def test_unmatched_delimiter_raises_error_p1(self):
        node = TextNode("This has `unmatched delimiter", TextType.TEXT)
        
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == '__main__':
    unittest.main()