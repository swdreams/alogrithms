from collections import deque

N = 100005

gr = [[] for i in range(N)]


# Function to add edge
def add_edge(u, v):
    gr[u].append(v)
    gr[v].append(u)


# Function to return the minimum path
# from 0th node to the (n - 1)th node
def dijkstra(n):
    # To check whether an edge is visited
    # or not and to keep distance of vertex
    # from 0th index
    vis = [0 for i in range(n)]
    dist = [10 ** 9 for i in range(n)]

    # Make 0th index visited and
    # distance is zero
    vis[0] = 1
    dist[0] = 0

    # Take a queue and
    # append first element
    q = deque()
    q.append(0)

    # Continue this until
    # all vertices are visited
    while (len(q) > 0):
        x = q.popleft()

        # Remove the first element
        for i in gr[x]:

            # Check if a vertex is
            # already visited or not
            if (vis[i] == 1):
                continue

            # Make vertex visited
            vis[i] = 1

            # Store the number of moves
            # to reach element
            dist[i] = dist[x] + 1

            # Push the current vertex
            # into the queue
            q.append(i)

            # Return the minimum number of
    # moves to reach (n - 1)th index
    return dist[n - 1]


# Function to return the minimum number of moves
# required to reach the end of the array
def Min_Moves(a, n):
    # To store the positions of each element
    fre = [[] for i in range(10)]
    for i in range(n):
        if (i != n - 1):
            add_edge(i, i + 1)

        fre[a[i]].append(i)

        # Add edge between same elements
    for i in range(10):
        for j in range(len(fre[i])):
            for k in range(j + 1, len(fre[i])):
                if (fre[i][j] + 1 != fre[i][k] and
                        fre[i][j] - 1 != fre[i][k]):
                    add_edge(fre[i][j], fre[i][k])

                    # Return the required
    # minimum number of moves
    return dijkstra(n)


# Driver code
a = [1, 2, 3, 4, 1, 5]
n = len(a)

print(Min_Moves(a, n))
