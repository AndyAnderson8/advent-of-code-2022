input = open('input.txt').read().splitlines()

def packetBeginningIndex(markerLength):
  for line in input:
    for i in range(len(line) - markerLength):
      if len(set(line[i:i + markerLength])) == markerLength:
        return i + markerLength

print("Part 1:", packetBeginningIndex(4))
print("Part 2:", packetBeginningIndex(14))