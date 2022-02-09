"""Count words in file."""
file = open("test.txt")

all_lines_list =[]
for line in file:
    line = line.rstrip().split(" ") #lins is now a list
    # print(type(line))
    # print(line)
    all_lines_list +=line
# print(all_lines_list)

word_count ={}
for word in all_lines_list:
    word_count[word] = word_count.get(word,0)+1
print(word_count)




