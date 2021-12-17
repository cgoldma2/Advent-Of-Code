#!/usr/bin/env python3

import sys


def decode_packet(packet):
    V = int(packet[0:3], 2)
    T = int(packet[3:6], 2)

    if T == 4:
        packet = packet[6:]
        n = ""
        while packet:
            if packet[0] == "1":
                n += packet[1:5]
                packet = packet[5:]
            else:
                n += packet[1:5]
                packet = packet[5:]
                break
        print("immediate", int(n,2))
        return int(n,2), packet

    else:
        vals = []
        I = int(packet[6], 2)
        L = 0
        if not I:
            print("I=0")
            L = int(packet[7:22], 2)
            packet = packet[22:]
            l_packet = len(packet)

            while len(packet) > l_packet-L:
                val, packet = decode_packet(packet)
                vals.append(val)

        else:
            L = int(packet[7:18], 2)
            packet = packet[18:]

            for _ in range(L):
                val, packet = decode_packet(packet)
                vals.append(val)

    if T == 0:
        return sum(vals), packet
    elif T == 1:
        prod = 1
        for n in vals:
            prod *= n
        return prod, packet
    elif T == 2:
        return min(vals), packet
    elif T == 3:
        return max(vals), packet
    elif T == 5:
        return vals[0] > vals[1], packet
    elif T == 6:
        return vals[0] < vals[1], packet
    elif T == 7:
        return vals[0] == vals[1], packet

def main():
    packet = format(int('1'+sys.stdin.readline().rstrip(), 16), 'b')
    packet = packet[1:]
    print(decode_packet(packet))


if __name__ == "__main__":
    main()

