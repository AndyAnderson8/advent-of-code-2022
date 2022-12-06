input = open('input.txt').read()

def packetBeginningIndex(markerLength):
  for i in range(len(input) - markerLength):
    if len(set(input[i:i + markerLength])) == markerLength:
      return i + markerLength

print("Part 1:", packetBeginningIndex(4))
print("Part 2:", packetBeginningIndex(14))