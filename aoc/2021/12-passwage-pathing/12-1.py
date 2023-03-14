with open('./input.txt', 'r', encoding='utf-8') as input_data:
    data = input_data.read()
    l = [r.split('-') for r in data.splitlines()]
    edges = [[a, b] for a, b in l if a != 'end' and b != 'start']
    edges += [[b, a] for a, b in l if a != 'end' and b != 'start']


    def find_path(current_path, found_paths, repeat):
        node = current_path[-1]
        if node == 'end':
            found_paths.append(current_path)
            return
        for edge in edges:
            if edge[0] == node:
                if edge[1].isupper() or edge[1] not in current_path:
                    find_path(current_path + [edge[1]], found_paths, repeat)
                elif edge[1].islower() and edge[1] in current_path and repeat:
                    find_path(current_path + [edge[1]], found_paths, False)


    def find_paths(repeat):
        found_paths = []
        find_path(['start'], found_paths, repeat)
        return found_paths


    assert len(find_paths(False)) == 119
