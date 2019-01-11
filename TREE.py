rosalind = open("rosalind_tree.txt", "r")
file_input = rosalind.readlines()

edges = []

for i in range(1, len(file_input)):
    edges.append(file_input[i].split())

print(int(file_input[0].strip()) - 1 - len(edges))
