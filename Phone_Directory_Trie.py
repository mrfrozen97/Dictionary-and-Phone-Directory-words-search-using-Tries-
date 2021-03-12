import pandas as pd
import tkinter as tk
import random
import tkinter.font as FT




class Node:

    def __init__(self, value):

        self.value = value
        self.children = []
        self.end = False
        self.number = ""


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
        self.number_list = []

    def add_word(self, word, number):
        curr = self.root
        for i in word:
            cur_list = [abc.value for abc in curr.get_children()]
            if i in cur_list:
                curr = curr.get_children()[cur_list.index(i)]
            else:
                temp = Node(i)
                curr.add_child(temp)
                curr = temp
        curr.set_end()
        curr.number = number

    def print_trie(self, root1):
        self.recurssion("", root1)

    def recurssion(self,str1, node):

        if node.end:
            self.number_list.append(node.number)
            self.search_list.append(str1)
            #print(str1)
       # print([ae.value for ae in node.children])
        for i in node.get_children():
            self.recurssion(str1+i.value, i)









"""
names = pd.read_csv("names.csv")
numbers = []

for i in names['Name']:
    temp=""
    temp += str(random.randint(7,9))
    for j in range(9):
        temp+=str(random.randint(1,9))
    numbers.append(temp)

names['Number'] = numbers

names.to_csv("phone_directory.csv")
"""


phone_directory_data = pd.read_csv("phone_directory.csv")
names = phone_directory_data['Name']
numbers = phone_directory_data['Number']




phone_directory_trie = Tries()

for i,t in enumerate(names):
    #print(numbers[i])
    phone_directory_trie.add_word(t, numbers[i])




def search(str1):
    if len(str1)>0:
        if str(str1[0]).islower():
            str1 = str(str1[0]).upper() + str1[1:]
    str2 = ""
    abc = phone_directory_trie.root
    flag = False
    phone_directory_trie.search_list = []
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

    phone_directory_trie.recurssion(str2, abc)
    #print(tree.search_list[:11])

    text+="\n"
    #for i in tree.search_list[:21]:
    #    text +=("\n"+i)

    label = tk.Label(root, text=text, bg='#80c1ff', font=40, anchor='nw', justify='left', bd=10)
    label.place(relx=0.0555, rely=0.21, relwidth=0.848, relheight=0.645)



    scroll1 = tk.Scrollbar(root)
    scroll1.place(relx=0.0555, rely=0.21, relwidth=0.848, relheight=0.645)

    font = FT.Font(family="Consolas", size=16)
    font.metrics(fixed=1)
    mylist = tk.Listbox(root, yscrollcommand=scroll1.set,  bg='#80c1ff')
    mylist.configure(font=font)

    mylist.insert(tk.END, text)
    mylist.insert(tk.END, " ")
    for t,i in enumerate(phone_directory_trie.search_list):

        stre = " "*(20-len(i))

        item = i + stre + str(phone_directory_trie.number_list[t])

        mylist.insert(tk.END, item )
    mylist.place(relx=0.0555, rely=0.21, relwidth=0.848, relheight=0.645)

    scroll1.config(command=mylist.yview())




HEIGHT = 550
WIDTH = 660


root = tk.Tk()
root.title("Dictionary Using Tries")

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

button = tk.Button(root, relief=tk.RIDGE, text="Search", bg='#ffc400', fg='blue', command=lambda: search(entry.get()), bd=3)
button.place(relx=0.70, rely=0.1, relwidth=0.20, relheight=0.05)




frame2 = tk.Frame(root, bg='#29b6f6')
frame2.place(relx=0.05, rely=0.2, relwidth=0.86, relheight=0.665)



root.mainloop()




"""
phone_directory_trie.print_trie(phone_directory_trie.root)
for i in range(len(phone_directory_trie.search_list)):
    print(phone_directory_trie.search_list[i], end=" ")
    print(phone_directory_trie.number_list[i])
#print(names)
"""
