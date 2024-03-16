
"""
Link:https://runestone.academy/ns/books/published/py4e-int/regex/hp-practice-adv.html

"""
# Create a regex that finds dates in the format MM/DD/YY or MM/DD/YYYY and returns just the year part
import re


def regex1(text):
    x = re.search("\\d{2}/\\d{2}/\\d{2,4}", text)
    if x is not None:
        print(x.group())




# Create a regex that finds phone numbers like 333-232-3403 or (333) 232 3403.
def regex2(text):
    x = re.search("\\d{3}-\\d{3}-\\d{4}|\(\\d{3}\\)\s\\d{3}\s\\d{4}", text)
    if x is not None:
        print(x.group())






if __name__ == "__main__":
    regex1(" today is 12/10/2022")
    regex1(" today is 12/12/22")
    regex2(" please contact us at 333-223-3403")
    regex2(" please contact us at (333) 223 3403")
