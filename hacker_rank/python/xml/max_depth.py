"""
#####################################################################
Intro: 

Task: Given a valid XML doc, print the maximum level of nesting
root depth = 0

Input: n which is the number of lines
next n liens are the xml doc

Output: single integer value

"""
import xml.etree.ElementTree as etree

maxdepth = 0


# def depth(elem, level):
#     global maxdepth
#     if len(elem) == 0: return 1
#     else:
#         return max(depth(el, level+1) for el in elem)

def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1

    for el in elem:
        depth(el, level+1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

""" Test input:

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

12
<entry>
    <author>                                                                 ①
        <name>Mark</name>
        <uri>http://diveintomark.org/</uri>
    </author>
    <title>Dive into history, 2009 edition</title>                                     ⑤
        <published>2009-03-27T17:20:42Z</published>        
            <category scheme='http://diveintomark.org' term='diveintopython'/>       ⑥
    <category scheme='http://diveintomark.org' term='docbook'/>
        <category scheme='http://diveintomark.org' term='html'/>
            <summary type='html'>Putti</summary>
</entry>          

"""