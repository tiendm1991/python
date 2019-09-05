def dfsComponentSize(matrix, vertex):
    s = {-1}
    visited = [False] * len(matrix)
    helped(matrix, s, visited, vertex)
    return len(s)-1

def helped(matrix, s, visited, vertex):
    s.add(vertex)
    visited[vertex] = True
    for i in range(len(matrix)):
        if i != vertex and matrix[vertex][i] and not visited[i]:
            helped(matrix,s,visited,i)
    return
print(dfsComponentSize([[False, True, False],
                      [True, False, False],
                      [False, False, False]],0))
