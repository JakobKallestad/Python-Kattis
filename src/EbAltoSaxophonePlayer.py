notes_to_fingers = {
    'a': {2, 3},
    'b': {2},
    'c': {2,3,4,7,8,9,10},
    'd': {2,3,4,7,8,9},
    'e': {2,3,4,7,8},
    'f': {2,3,4,7},
    'g': {2,3,4},
    'A': {1,2,3},
    'B': {1,2},
    'C': {3},
    'D': {1,2,3,4,7,8,9},
    'E': {1,2,3,4,7,8},
    'F': {1,2,3,4,7},
    'G': {1,2,3,4}
}

n_test_cases = int(input())
for _ in range(n_test_cases):
    finger_count = {i:0 for i in range(1, 11)}
    notes = list(input())
    prev_fingers = [False] * 11
    for n in notes:
        for finger in range(1, 11):
            if finger in notes_to_fingers[n]:
                if not prev_fingers[finger]:
                    finger_count[finger] += 1
                prev_fingers[finger] = True
            else:
                prev_fingers[finger] = False
    print(*finger_count.values())
