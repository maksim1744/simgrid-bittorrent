f = open('result', 'r').readlines()
f.sort()

iters = 0

ttm = 0

crange = list(range(50, 501, 50))

res = [[-1 for i in range(len(crange) + 1)] for j in range(len(crange) + 1)]
for i in range(len(crange)):
    res[i + 1][0] = crange[i]
    res[0][i + 1] = crange[i]

for line in f:
    line = line.strip().replace(' ', '').split('|')[1:]
    if '0' not in line[0]:
        continue
    chunks, peers, messages = map(int, line[:3])
    time = float(line[3])
    iters += 1
    ttm += time

    if iters % 3 == 0:
        res[crange.index(chunks) + 1][crange.index(peers) + 1] = messages
        ttm = 0


for l in res:
    print('\t'.join(map(str, l)).replace('.', ','))
