import re


paragraph = "paragraph"
heading = "heading"
code = "code"
quote = "quote"
unordered_list = "unordered_list"
ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    for line in lines:
        line = line.strip()
        if line:
            blocks.append(line)
    return blocks


def block_to_block_type(block):
    split = []
    if "\n" in block:
        split = markdown_to_blocks(block)
        
        is_quote = False
        for line in split:
            if line[0] == ">":
                is_quote = True
            else:
                is_quote = False
                break
        if is_quote:
            return quote
        
        is_unordered = False
        for line in split:
            if line[0] == "*" or line[0] == "-":
                is_unordered = True
            else:
                is_unordered = False
                break
        if is_unordered:
            return unordered_list
        
        num = 1
        is_ordered = False
        for line in split:
            if line[:3] == f"{num}. ":
                is_ordered = True
                num += 1
            else:
                is_ordered = False
                break
        if is_ordered:
            return ordered_list

    if re.match(r"^#{1,6} ", block):
        return heading
    elif block[:3] == "```" and block[-3:] == "```":
        return code
    elif block[0] == ">":
        return quote
    elif block[0] == "*" or block[0] == "-":
        return unordered_list
    elif block[:3] == "1. ":
        return ordered_list
    
    return paragraph

