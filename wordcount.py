"""Count words in file."""
file = open("twain.txt")

all_lines_list =[]
for line in file:
    line = line.rstrip().split(" ") #lins is now a list
    #line.lower()
    # print(type(line))
    # print(line)
    all_lines_list +=line
# print(all_lines_list)

#Method 1: for loop to count word counts
word_count ={}
for word in all_lines_list:
    word_count[word.lower().strip("""!()-[]{};:'"\,<>./?@#$%^&*_~""")] = word_count.get(word.lower().strip("""!()-[]{};:'"\,<>./?@#$%^&*_~"""),0)+1
# print(word_count)
# print(sorted(word_count).items())

#sort based on key alphabetical order
#for key in sorted(word_count):
    #print(f"{key} {word_count[key]}")
#print(set(f"{key} {word_count[key]}"))
# sort based on value
#print(word_count)




for key, value in word_count.items():
    print(f"{key} {value}")
# Method2: collection.counter approach
# from collections import Counter
# cnt = Counter()
# for word in all_lines_list:
#     cnt[word.lower().strip("""!()-[]{};:'"\,<>./?@#$%^&*_~""")] +=1
# for key, value in cnt.items():
#     print(f"{key} {value}")

# for key, value in word_count.items():
#     print(f"{key} {value}")
#     #count(key, value)
# rstrip("!")
#strip("(){}<>")