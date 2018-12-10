sum = 0
hashmap = dict()
hashmap[sum] = 1
while True:
    with open("input.txt", 'r') as file:
        for line in file:
            sum = sum + int(line)
            if sum in hashmap:
                print sum
                exit()
                hashmap[sum] = hashmap[sum] + 1
            else:
                hashmap[sum] = 1

print hashmap
print sum
