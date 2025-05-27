# Word Frequency Counter in a Text File
#
# Reads a file and returns frequency of each word using dictionary and functional logic.

def textf(filename):
    with open(filename,'r') as f:
        data=f.read()
        x=data.split()
        print(x)
        dict1={}
        for i in x:
            if i in dict1.keys():
                dict1[i]+=1
            else:
                dict1[i]=i.count(i)
        return dict1



print(textf('text.txt'))