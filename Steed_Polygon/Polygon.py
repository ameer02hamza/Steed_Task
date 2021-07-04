import matplotlib.pyplot as plt
coord = []
for i in range(10):
    x = int(input("Enter x cord"))
    y = int(input("Enter y cord"))
    coord.append([x, y])
    break_loop = input("If you want to break loop press b")
    if break_loop == 'b':
        break

print(coord)
coord.append(coord[0])

xs, ys = zip(*coord)

plt.figure()
plt.fill(xs, ys, c='C0')
plt.plot(xs, ys)
plt.show()
