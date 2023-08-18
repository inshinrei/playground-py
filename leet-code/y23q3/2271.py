from bisect import bisect_right


def max_white_tiles(tiles, carpet_len):
    if any(tile[1] - tile[0] + 1 >= carpet_len for tile in tiles):
        return carpet_len
    result = 0
    prefix = [0] * (len(tiles) + 1)
    tiles.sort()
    starts = [tile[0] for tile in tiles]
    for i, tile in enumerate(tiles):
        length = tile[1] - tile[0] + 1
        prefix[i + 1] = prefix[i] + length
    for i, (s, _) in enumerate(tiles):
        carpet_end = s + carpet_len - 1
        end = bisect_right(starts, carpet_end) - 1
        not_cover = max(0, tiles[end][1] - carpet_end)
        result = max(result, prefix[end + 1] - prefix[i] - not_cover)
    return result
