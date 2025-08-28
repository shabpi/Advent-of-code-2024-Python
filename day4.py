import re

def search_word(data,word):
    total = 0
    
    for line in data:
        j = 0
        pos_counter = 0
        length_line = len(line)
        length_word = len(word)
        
        while (j < length_line-length_word+1 + pos_counter):
            if(pos_counter == length_word - 1 and line[j] == word[length_word - 1]): ##in our specific situatuion this will work, cuz we don have repeated letters in the word
                total += 1
                pos_counter = 0
                j += 1
                continue
            if (line[j] == word[pos_counter]):
                pos_counter += 1
            elif (line[j] == word[0]):
                pos_counter = 1
            else:
                pos_counter = 0
            j += 1



    return total


def search_vertical(data, word):
    total = 0
    rows = len(data)
    length_line = len(data[0])
    for j in range(0,length_line ):
        i = 0
        pos_counter = 0
        
        length_word = len(word)
        
        while (i < rows-length_word+1 + pos_counter):
            if(pos_counter == length_word - 1 and data[i][j] == word[length_word - 1]): ##in our specific situatuion this will work, cuz we don have repeated letters in the word
                total += 1
                pos_counter = 0
                i += 1
                continue
            if (data[i][j] == word[pos_counter]):
                pos_counter += 1
            elif (data[i][j] == word[0]):
                pos_counter = 1
            else:
                pos_counter = 0
            i += 1
    return total

def diagonalize(text):
    rows = len(text)
    columns = len(text[0])
    output = [[] for k in range(rows + columns - 1)]
    for j in range(0,columns):
        for i in range(0,rows):
            output[i+j].append(text[i][j])
    return output

def diagonalize_2(text):
    rows = len(text)
    columns = len(text[0])
    output = [[] for k in range(rows + columns - 1)]
    for i in range(0,rows):
        for j in range(0,columns):
            output[i+j].append(text[i][columns - j - 1])
    return output


def search(text,word):
    total = 0
    drow = word[::-1]
    print(drow)
    total += search_word(text,word) + search_word(text,drow)
    total += search_word(diagonalize(text),word) + search_word(diagonalize(text),drow)
    total += search_word(diagonalize_2(text),word) + search_word(diagonalize_2(text),drow)
    total += search_vertical(text,word) + search_vertical(text, drow)
    return total

text = []
with open("input.txt") as f:
    
    for line in f: 
        text.append(line.strip()) 

with open("input.txt") as f:
    text2= f.read()

length_line = len(text[0])




length_line -= 2

print(length_line)
text2 = "".join(text)  # flatten grid into single string

occurences = len(re.findall(f"(?=(M.S.{{{length_line}}}A.{{{length_line}}}M.S))",text2) )
occurences += len(re.findall(f"(?=(S.M.{{{length_line}}}A.{{{length_line}}}S.M))",text2) )
occurences += len(re.findall(f"(?=(M.M.{{{length_line}}}A.{{{length_line}}}S.S))",text2) )
occurences += len(re.findall(f"(?=(S.S.{{{length_line}}}A.{{{length_line}}}M.M))",text2) )


print(occurences)

