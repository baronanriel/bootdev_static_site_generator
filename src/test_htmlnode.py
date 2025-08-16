import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init1(self):
        node = HTMLNode()
        print(node)


    def test_init2(self):
        node = HTMLNode("test", "Test", ['this', 'that', 'cheese'], {'this':"that"})
        print(node)
    
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

    def test_props_to_html2(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        res = node.props_to_html()
        self.assertEqual(res, ' href="https://www.google.com"')
