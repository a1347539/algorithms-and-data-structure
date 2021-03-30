def maxheapify(nodes,node):
    if node*2 <= len(nodes):
        if nodes[node-1] < nodes[node*2-1] or nodes[node*2]:
            if nodes[node*2-1] < nodes[node*2]:
                nodes[node-1], nodes[node*2] = nodes[node*2], nodes[node-1]
            else:
                nodes[node-1], nodes[node*2-1] = nodes[node*2-1], nodes[node-1]






nodes = [1,2,3,4,5,6,7]


print(maxheapify(nodes))
