def cycleInGraph(edges):
    # Write your code here.
    visited = [0] * len(edges)
    in_stack = [0] * len(edges)

    for i in range(len(edges)):
        if visited[i]: continue
        contains_cycle = is_node_in_cycle(i, edges, visited, in_stack)
        if contains_cycle: return True
    return False

def is_node_in_cycle(node, edges, visited, currently_in_stack):
    visited[node] = 1
    currently_in_stack[node] = 1

    for neighbor in edges[node]:
        if currently_in_stack[neighbor]: return True
        visited[neighbor] = 1
        currently_in_stack[neighbor] = 1
        is_node_in_cycle(neighbor, edges, visited, currently_in_stack)
    # return False

    for neighbor in edges[node]:
        # if visited[neighbor]:
            # move on?
        if not visited[neighbor]:
            visited[neighbor] = 1
            currently_in_stack[neighbor] = 1
            contains_cycle = is_node_in_cycle(neighbor, edges, visited, currently_in_stack)
            if  contains_cycle:
                return True
        
        elif currently_in_stack[neighbor]:
            return True
    

    currently_in_stack[node] = 0
    return False

