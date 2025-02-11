from systemcommands import *
import markdown

def mth_icon():
    print("================================================")
    print("||              MARKDOWN TO HTML              ||")
    owner()
    print("================================================")

def markdown_to_html():
    mth_icon()
    markdown_text = input("Enter the markdown text (when finished enter 0) : \n")
    str = ''
    while markdown_text != "0":
        str += markdown.markdown(markdown_text)
        str += "\n"
        markdown_text = input("")
        

    print(str)

markdown_to_html()