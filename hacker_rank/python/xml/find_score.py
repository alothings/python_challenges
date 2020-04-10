"""
#####################################################################
Intro: Score is calculated by the sum of the score of each element.
For any element, score = number of attributes it has

Task: Given a valid XML doc, print its score.


Input: by line:
n number of lines in xml
xml document

Output: single integer score

"""
import sys
import string
import xml.etree.ElementTree as etree


def get_attr_number(node):
    if len(node) == 0:
        return len(node.attrib)
    else:
        # return len(node.attrib) + sum([len(el.attrib) for el in node])
        return len(node.attrib) + sum([get_attr_number(el) for el in node])


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


""" Test input:

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
"""