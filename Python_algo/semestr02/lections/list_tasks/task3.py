# Необходимо определить номер (не индекс)
# первого элемента целочисленного списка,
# который не больше заданой величины 437


heights = list(map(int, input().split()))
bus_height = 437

for i, h in enumerate(heights):
    if h <= bus_height:
        print(f"Crash {i + 1}")
        break

else: print("No crash")

