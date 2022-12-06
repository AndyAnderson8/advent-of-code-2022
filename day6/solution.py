input = open('input.txt').read().splitlines()

def packetBeginningIndex(markerLength):
  for line in input:
    for i in range(len(line) - markerLength):
      marker = line[i:i + markerLength]
      allUnique = True
      for j, firstLetter in enumerate(marker):
        for k, secondLetter in enumerate(marker):
          if j > k and firstLetter == secondLetter:
              allUnique = False
      if allUnique:
        return i + markerLength

print("Part 1:", packetBeginningIndex(4))
print("Part 2:", packetBeginningIndex(14))