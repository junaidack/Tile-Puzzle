import heapq


def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):


    if not to_state:
        to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]

    return sum(abs(k%3 - j%3) + abs(k//3 - j//3)
        for k, j in ((from_state.index(x), to_state.index(x)) for x in range(1, 8)))


def print_succ(state):

    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):

    succ_states = []

    indices = []
    for idx, value in enumerate(state):
        if value == 0:
            indices.append(idx)

    for index in indices:
        copy = list(state)
        copy1 = list(state)
        copy2 = list(state)
        copy3 = list(state)

        if index == 0:
            if state[1] != 0:
                copy[0] = state[1]
                copy[1] = 0
                succ_states.append(copy)
            if state[3] != 0:
                copy1[0] = state[3]
                copy1[3] = 0
                succ_states.append(copy1)

        elif index == 1:
            if state[0] != 0:
                copy[1] = state[0]
                copy[0] = 0
                succ_states.append(copy)
            if state[2] != 0:
                copy1[1] = state[2]
                copy1[2] = 0
                succ_states.append(copy1)
            if state[4] != 0:
                copy2[1] = state[4]
                copy2[4] = 0
                succ_states.append(copy2)

        elif index == 2:
            if state[1] != 0:
                copy[2] = state[1]
                copy[1] = 0
                succ_states.append(copy)
            if state[5] != 0:
                copy1[2] = state[5]
                copy1[5] = 0
                succ_states.append(copy1)

        elif index == 3:
            if state[0] != 0:
                copy[3] = state[0]
                copy[0] = 0
                succ_states.append(copy)
            if state[4] != 0:    
                copy1[3] = state[4]
                copy1[4] = 0
                succ_states.append(copy1)
            if state[6] != 0:
                copy2[3] = state[6]
                copy2[6] = 0
                succ_states.append(copy2)

        elif index == 4:
            if state[1] != 0:
                copy[4] = state[1]
                copy[1] = 0
                succ_states.append(copy)
            if state[3] != 0:
                copy1[4] = state[3]
                copy1[3] = 0
                succ_states.append(copy1)
            if state[5] != 0:
                copy2[4] = state[5]
                copy2[5] = 0
                succ_states.append(copy2)
            if state[7] != 0:
                copy3[4] = state[7]
                copy3[7] = 0
                succ_states.append(copy3)

        elif index == 5:
            if state[2] != 0:
                copy[5] = state[2]
                copy[2] = 0
                succ_states.append(copy)
            if state[4] != 0:
                copy1[5] = state[4]
                copy1[4] = 0
                succ_states.append(copy1)
            if state[8] != 0:
                copy2[5] = state[8]
                copy2[8] = 0
                succ_states.append(copy2)

        elif index == 6:
            if state[3] != 0:
                copy[6] = state[3]
                copy[3] = 0
                succ_states.append(copy)
            if state[7] != 0:
                copy1[6] = state[7]
                copy1[7] = 0
                succ_states.append(copy1)

        elif index == 7:
            if state[4] != 0:
                copy[7] = state[4]
                copy[4] = 0
                succ_states.append(copy)
            if state[6] != 0:
                copy1[7] = state[6]
                copy1[6] = 0
                succ_states.append(copy1)
            if state[8] != 0:
                copy2[7] = state[8]
                copy2[8] = 0
                succ_states.append(copy2)

        elif index == 8:
            if state[5] != 0:
                copy[8] = state[5]
                copy[5] = 0
                succ_states.append(copy)
            if state[7] != 0:
                copy1[8] = state[7]
                copy1[7] = 0
                succ_states.append(copy1)

    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):


    max_len = 1
    g = 0
    h = get_manhattan_distance(state, goal_state)
    cost = g+h
    pq = []
    closed = []
    visited = []
    initial = (h,state,(g,h,-1))
    heapq.heappush(pq,(h,state,(g,h,-1)))
    index = 0
    while pq:
        c,s,other_infor = heapq.heappop(pq)
        closed.append((c,s,other_infor))
        visited.append(s)
        if s == goal_state:
            break
        succ_states = get_succ(s)
        for succ_state in succ_states:
            if succ_state not in visited:
                heapq.heappush(pq,(get_manhattan_distance(succ_state)+other_infor[0],succ_state,(other_infor[0]+1,get_manhattan_distance(succ_state),index)))
        max_len = max(len(pq), max_len)
        index += 1


    lastNode = closed[-1]
    trace = []
    while lastNode[2][2] > 0:
        lastNode = closed[lastNode[2][2]]
        trace.append(lastNode)

    trace.append(initial)
    trace.reverse()
    trace.append((c,s,other_infor))

    for k in range(len(trace)):
        print(str(trace[k][1])+ " h=" +str(trace[k][2][1])+ " moves: " + str(trace[k][2][0]))

    print("Max queue length: "  + str(max_len))

      
if __name__ == "__main__":

    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    print()

    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    solve([4,3,0,5,1,6,7,2,0])
    print()
