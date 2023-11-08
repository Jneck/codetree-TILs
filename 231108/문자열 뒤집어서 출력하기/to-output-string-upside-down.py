import sys
print = sys.stdout.write
temp_list = []
for i in range(4):
    temp_list.append(input())

for i in range(3, -1, -1):
    for j in range(len(temp_list[i])-1, -1, -1):
        print(temp_list[i][j])
    print('\n')