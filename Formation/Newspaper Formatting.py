"""
📰 Problem: Format Text into a Newspaper Page
You are given a list of paragraphs and a maximum line width. Your task is to format the text into a newspaper-style page that follows specific formatting rules.

Input
paragraphs: A list of paragraphs, where each paragraph is a list of strings (words).

width: An integer representing the maximum number of characters allowed on each line (excluding border asterisks).

Output
Return a list of strings, where each string is a line of the newspaper page, properly formatted and surrounded by a border.

Formatting Rules
Line Filling:

Start a new line when adding another word would exceed the width.

Words in a paragraph must appear in order.

Separate words with a single space.

Do not split a word between lines.

Text Justification:

Center each line horizontally:

If there is extra space on the line, add an equal number of spaces before and after the line content.

If the extra space is odd, the extra space goes after the text.

Borders:

Add a border of * characters:

Top and bottom borders: A full line of width + 2 asterisks.

Each text line: one asterisk on each side.

Paragraph Continuation:

Continue lines from the same paragraph without starting a new line unless needed due to the width constraint.

Only start a new line when you can't add the next word to the current line.
"""
paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["Please", "look", "and", "align", "to", "center"]]
width = 16



# first element => * * length 
# last element => * * length 

# in between:
# iterate through words in each paragraph 
# keep track of current length, starting with the first word (guaranteed that the paragrpah will be non-empty?)
# add space  + current word -> if this exceeds the max width, format the current string 
# add the asterick at the edges 
# should be (width - 2 - cur_length) // 2 (also keep remainder to add at the end)
# append this

def process_paragraph(string: str, width: int):
    spaces = (width - len(string)) // 2
    remainder = (width - len(string)) % 2
    res = f"*{' ' * spaces}{string}{' ' * (spaces + remainder)}*"
    return res

def solution(paragraphs: list, width: int):
    res = []

    res.append("*" * (width + 2))

    for paragraph in paragraphs:
        cur_string = paragraph[0]

        for i in range(1, len(paragraph)):
            if len(cur_string) + len(paragraph[i]) + 1 > width:
                processed = process_paragraph(cur_string, width)
                res.append(processed)
                cur_string = paragraph[i]
        
            else:
                cur_string += f" {paragraph[i]}"
        
        processed = process_paragraph(cur_string, width)
        res.append(processed)
    
    res.append("*" * (width + 2))
    return res

actual = solution(paragraphs, width)

for paragraph in actual:
    print(f"{paragraph}, {len(paragraph)}")
