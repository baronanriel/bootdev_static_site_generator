class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag                  # String HTML Tag
        self.value = value              # String Value of Tag (Text in paragraph)
        self.children = children        # List of HTMLNode objects representing children of this node
        self.props = props              # Dictionary of Key-value pairs representing attributes of HTML Tag

    def to_html(self):
        raise NotImplementedError
    
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