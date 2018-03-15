def music_sort(numSongs, ratings):
    """
    :param numSongs: int
    :param ratings: List[List[int]]
    :return: List[int]
    """
    incoming = {i: 0 for i in range(numSongs)}
    outgoing = {i: [] for i in range(numSongs)}

    for rating in ratings:
        if len(rating) > 1:
            first = rating[:-1]
            second = rating[1:]
            for f, s in zip(first, second):
                incoming[s] += 1
                outgoing[f].append(s)

    visited = [0] * numSongs
    t_sort = []

    while 0 in visited:
        for node in range(numSongs):
            if visited[node] == 1:
                continue
            elif incoming.get(node) == 0:
                t_sort.append(node)

                for i in outgoing[node]:
                    incoming[i] -= 1

                visited[node] = 1
    return t_sort

a = [1,4,5]
b = [2,5]
c = [5,3]
d = [1]
e = [0]

print(music_sort(6, [a,b,c,d]))