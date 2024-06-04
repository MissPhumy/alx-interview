def canUnlockAll(boxes):
    n = len(boxes)
    keys = {0}
    opened_boxes = [0]

    while opened_boxes:
        current_box = opened_boxes.pop()
        for key in boxes[current_box]:
            if key not in keys and key < n:
                keys.add(key)
                opened_boxes.append(key)

    return len(keys) == n
