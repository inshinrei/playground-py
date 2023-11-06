def can_be_stacked(top, bottom):
    return top[0] < bottom[0] and top[1] < bottom[1]


def tallest_stack(boxes):
    boxes.sort(key=lambda x: x[0])
    heights = {box: box[2] for box in boxes}
    for i in range(1, len(boxes)):
        box = boxes[i]
        S = [boxes[j] for j in range(i) if can_be_stacked(boxes[j], box)]
        heights[box] = box[2] + max([heights[box] for box in S], default=0)
    return max(heights.values(), default=0)
