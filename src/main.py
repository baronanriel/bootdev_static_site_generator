from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    props = None
    value = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            tag = None
        case TextType.BOLD:
            tag = 'b'
        case TextType.ITALIC:
            tag = 'i'
        case TextType.CODE:
            tag = 'code'
        case TextType.LINK:
            tag = 'a'
            props = {'href':f'{text_node.url}'}
        case TextType.IMAGE:
            tag = 'img'
            props = {'src':f'{text_node.url}', 'alt':f'{text_node.text}'}
            value = ''
        case _:
            raise Exception("Inappropriate tag type")
    return LeafNode(tag, value, props)


def main():
    test = TextNode("This is some anchor text", TextType.LINK, 'https://www.boot.dev')
    print(test)


if __name__ == "__main__":
    main()