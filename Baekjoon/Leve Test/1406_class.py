import sys

left_stack = list(sys.stdin.readline()[:-1])
right_stack = list()
testcase = int(sys.stdin.readline())


for _ in range(testcase):
    cmd = sys.stdin.readline()

    if cmd[0] == 'L' and left_stack:
        right_stack.append(left_stack.pop())
    elif cmd[0] == 'D' and right_stack:
        left_stack.append(right_stack.pop())
    elif cmd[0] == 'B' and left_stack:
        left_stack.pop()
    elif cmd[0] == 'P':
        left_stack.append(cmd[2])

sys.stdout.write(''.join(left_stack + right_stack[::-1]))
