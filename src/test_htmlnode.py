import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):    
    def test_props_to_html1(self):
        node = HTMLNode()
        res = node.props_to_html()
        self.assertEqual(res, '')

    def test_props_to_html2(self):
        node = HTMLNode(props={
    "href": "https://www.google.com",
    "target": "_blank",
})
        res = node.props_to_html()
        self.assertEqual(res, ' href="https://www.google.com" target="_blank"')

    def test_props_to_html3(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        res = node.props_to_html()
        self.assertEqual(res, ' href="https://www.google.com"')


    def test_leaf_to_html_p1(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p2(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_p3(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
