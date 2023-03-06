from dataclasses import dataclass


@dataclass
class Packet:
    version: int
    type_id: int
    literal: int
    length: int
    sub: list


def parse_packet(bits, depth=0):
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    pos = 6
    if type_id == 4:
        literal, is_last = 0, False
        while not is_last:
            is_last = bits[pos] == '0'
            literal = (literal << 4) | int(bits[pos + 1:pos + 5], 2)
            pos += 5
        return Packet(version, type_id, literal, pos, [])

    length_type_id = int(bits[pos], 2)
    pos += 1
    if length_type_id == 0:
        total_len = int(bits[pos:pos + 15], 2)
        pos += 15
        length = 0
        sub_packets = []
        while length != total_len:
            packet = parse_packet(bits[pos:pos + total_len - length], depth + 1)
            sub_packets.append(packet)
            length += packet.length
            pos += packet.length
        return Packet(version, type_id, 0, pos, sub_packets)

    number = int(bits[pos:pos + 11], 2)
    pos += 11
    sub_packets = []
    for _ in range(number):
        packet = parse_packet(bits[pos:], depth + 1)
        sub_packets.append(packet)
        pos += packet.length
    return Packet(version, type_id, 0, pos, sub_packets)


def add_versions(packets):
    total = 0
    for p in packets:
        total += p.version
        total += add_versions(p.sub_packets)
    return total


with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read().strip()
    bits = bin(int(data, 16))[2:].zfill(len(data) * 4)
    packets = parse_packet(bits)
    print(add_versions([packets]))
