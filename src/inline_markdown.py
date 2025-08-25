from textnode import TextType, TextNode

'''
split_nodes_delimiter takes a list of raw markdown and converts them to textNodes. Currently, this will only be working for 
regular text, bold, italic, and code markdown tags. 
Input: 
old_nodes -> list of text nodes .
delimiter -> This is the delimiter identifier of the md string (i.e. ** for bold, _ for italic, and ` for code)
text_type
'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for md_node in old_nodes:
        if md_node.text_type != TextType.TEXT:
            new_nodes.append(md_node)
            continue
        
        
        dlmt_text = md_node.text.split(delimiter)
        if len(dlmt_text) % 2 == 0:
            raise ValueError("Text was improperly delimited.")
        
        split_nodes = []
        for i, content in enumerate(dlmt_text):
            if not content:
                continue
            if i % 2:
                split_nodes.append(TextNode(content, text_type))
            else:
                split_nodes.append(TextNode(content, TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes

def main():
    return None




if __name__ == "__main__":
    main()