def html_begin():
    return "<html>\n"

def html_end():
    return "</html>\n"

def link(text, url):
    return f'<a href="{url}">{text}</a>'

def table_begin():
    return '<table border="1">'
def table_end():
    return "</table>"
def row_begin():
    return "<tr>"
def row_end():
    return "</tr>"
def col_begin():
    return "<td>"
def col_end():
    return "</td>"

s = ""
s += html_begin()
s += link("click this","https://www.google.com")



s += table_begin()

for i in range(10):
    s += row_begin()

    s += col_begin()
    s += "apple"
    s+=col_end() 
    s += col_begin()
    s += "orange"
    s+=col_end() 
    s += col_begin()
    s += "banana"
    s+=col_end() 
    s+=row_end()

s+= table_end()

s+= html_end()


print(s)
