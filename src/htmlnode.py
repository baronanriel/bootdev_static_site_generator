class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag                  # String HTML Tag
        self.value = value              # String Value of Tag (Text in paragraph)
        self.children = children        # List of HTMLNode objects representing children of this node
        self.props = props              # Dictionary of Key-value pairs representing attributes of HTML Tag

    def to_html(self):
        raise NotImplementedError("HTMLNode does not have a to_html function yet")
    
    def props_to_html(self):
        res_str = ''
        if not self.props:
            return res_str
        for tag, value in self.props.items():
            res_str += f' {tag}="{value}"'
        return res_str
    
    def __repr__(self):
        res = f'HTMLNode: \n\t'
        res += f'Tag: {self.tag}\n\tValue: {self.value}\n\t'
        res += f'Children: {self.children}\n\tProps: {self.props}'
        return res

    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode does not have any value")
        
        if not self.tag:
            return f'{self.value}'
        
        return f'<{self.tag}>{self.value}</{self.tag}>'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode does not have any tags")
        
        if not self.children:
            raise ValueError("ParentNode does not have any children")
        
        res = f'<{self.tag}>'
        for child in self.children:
            res += child.to_html()
        res += f'</{self.tag}>'
        return res