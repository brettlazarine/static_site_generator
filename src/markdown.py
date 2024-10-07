import re
from textnode import *

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    if old_nodes.text_type != text_type_text:
        new_nodes.append(old_nodes)


    images = extract_markdown_images(old_nodes.text)

    if not images:
        new_nodes.append(old_nodes)

    text = old_nodes.text
    for alt, url in images:
        sections = text.split(f"![{alt}]({url})", 1)
        if sections[0]:
            new_nodes.append(TextNode(sections[0], text_type_text))
        
        new_nodes.append(TextNode(alt, text_type_image, url))

        text = sections[1]

    if text:  
        new_nodes.append(TextNode(text, text_type_text))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    if old_nodes.text_type != text_type_text:
        new_nodes.append(old_nodes)
        
    links = extract_markdown_links(old_nodes.text)

    if not links:
        new_nodes.append(old_nodes)
        

    text = old_nodes.text
    for anchor, url in links:
        sections = text.split(f"[{anchor}]({url})", 1)
        
        if sections[0]:
            new_nodes.append(TextNode(sections[0], text_type_text))
        
        
        new_nodes.append(TextNode(anchor, text_type_link, url))

        
        text = sections[1]

    if text:
        new_nodes.append(TextNode(text, text_type_text))

    return new_nodes