import pandas as pd
import tkinter as tk

class Node:

    def __init__(self, value):

        self.value = value
        self.children = []
        self.end = False


    def add_child(self, child):

        self.children.append(child)

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

    def set_end(self):
        self.end = True



class Tries:

    def __init__(self):

        self.root = Node('#')
        self.search_list = []

    def add_word(self, word):
        curr = self.root
        for i in word:
            cur_list = [abc.value for abc in curr.get_children()]
            if i in cur_list:
                curr = curr.get_children()[cur_list.index(i)]
               # print("blablabla")
               # pass
            else:
                temp = Node(i)
                curr.add_child(temp)
                curr = temp
        curr.set_end()

    def print_trie(self, root1):
        self.recurssion("", root1)

    def recurssion(self,str1, node):

        if node.end:
            self.search_list.append(str1)
            #print(str1)
       # print([ae.value for ae in node.children])
        for i in node.get_children():
            self.recurssion(str1+i.value, i)


words = []
words_list = pd.read_csv("dictionary.csv")
for i in words_list['A'][:]:
    #print(i)
    j = str(i)

    words.append(j)




tree = Tries()
for i in words:
   tree.add_word(i)

"""
abc = tree.root.get_children()[1].get_children()[1]
#tree.print_trie(abc)
tree.recurssion("Ab", abc)

print([i.value for i in abc.get_children()])

print([i.value for i in tree.root.get_children()])
print(tree.search_list)
"""



"""
str1 = "abc"
str2 = ""
abc = tree.root
flag = False
for i in str1:
    curr_list = [j.value for j in abc.get_children()]
    #print(curr_list)
    if i in curr_list:
        abc = abc.get_children()[curr_list.index(i)]
        str2+=abc.value
    else:
        flag = True
        break
"""


def search(str1):
    str2 = ""
    abc = tree.root
    flag = False
    tree.search_list = []
    for i in str1:
        curr_list = [j.value for j in abc.get_children()]
        # print(curr_list)
        if i in curr_list:
            abc = abc.get_children()[curr_list.index(i)]
            str2 += abc.value
        else:
            flag = True
            break
    text = ""
    #print(str)
    if flag:
        text = "Did you Mean? " + str2
      #  print("Did you Mean? " + str2)
    else:
        text = "Reselts for: " + str2
     #   print("Reselts for: " + str2)

    tree.recurssion(str2, abc)
    #print(tree.search_list[:11])

    text+="\n"
    for i in tree.search_list[:11]:
        text +=("\n"+i)

    label = tk.Label(root, text=text, bg='#80c1ff', font=40, anchor='nw', justify='left', bd=10)
    label.place(relx=0.0555, rely=0.21, relwidth=0.848, relheight=0.645)



HEIGHT = 550
WIDTH = 660


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#frame = tk.Frame(root, bg='black')
#frame.place(relwidth=1, relheight=1)

bg_image = tk.PhotoImage(file="bg4.png")
bg_label = tk.Label(root, image = bg_image)
bg_label.place(relwidth=1, relheight=1)


frame1 = tk.Frame(root, bg='#29b6f6', bd=10)
frame1.place(relx=0.045, rely=0.0925, relwidth=0.86, relheight=0.065)
#frame1.place(relx=0.05, rely=0.1, relwidth=0.65, relheight=0.05)

entry = tk.Entry(root, bg='#80c1ff', font=35, bd=1)
entry.place(relx=0.05, rely=0.1, relwidth=0.65, relheight=0.05)

button = tk.Button(root, text="Search", bg='gray', fg='blue', command=lambda: search(entry.get()), bd=3)
button.place(relx=0.70, rely=0.1, relwidth=0.20, relheight=0.05)




frame2 = tk.Frame(root, bg='#29b6f6')
frame2.place(relx=0.05, rely=0.2, relwidth=0.86, relheight=0.665)



root.mainloop()



