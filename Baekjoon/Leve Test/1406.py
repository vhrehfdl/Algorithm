import sys

word = sys.stdin.readline().strip()
word_list = list(word)
cursor = len(word_list)

N = int(sys.stdin.readline())
for i in range(0, N):
    command = sys.stdin.readline().strip()

    if command[0] == "L" and cursor > 0:
        cursor -= 1
    elif command[0] == "D":
        cursor += 1
    elif command[0] == "B" and cursor > 0:
        del word_list[cursor-1]
        cursor -= 1
    elif command[0] == "P":
        temp = command.split(" ")[1]
        word_list.insert(cursor, temp)
        cursor += 1

print("".join(word_list))