import os
with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as f:
  lines = [str(line) for line in f.read().splitlines()]

elvesCalories = []
currentElfCalories = 0

for line in lines:
  if line == "":
    elvesCalories.append(currentElfCalories)
    currentElfCalories = 0
  else:
    currentElfCalories += int(line)
elvesCalories.sort()

print("Part 1:", (elvesCalories[-1]))
print("Part 2:", sum(elvesCalories[-3:]))