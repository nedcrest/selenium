import webbrowser

new = 2

tabURL = "http://google.com/?#q="
term = raw_input("Enter search query: ")

webbrowser.open(tabURL+term, new=new)
