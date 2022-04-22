import os
import time

os.system("echo -n \"\" >tmp")


def compile_with_chunks(chunks):
    lines = open("template-bittorrent.hpp", "r").readlines()
    f = open("s4u-bittorrent.hpp", "w")
    for line in lines:
        if line.startswith("constexpr unsigned long FILE_PIECES"):
            f.write(f"constexpr unsigned long FILE_PIECES   = {chunks}UL;\n")
        else:
            f.write(line)
    f.close()
    os.system("cmake . >>tmp && make 1>>tmp 2>>tmp")

def gen_peers(peers):
    os.system(f"python3 gen_peers.py {peers} >>tmp")

res = open("result", "w", buffering=1)
def mprint(s):
    print(s)
    res.write(s + '\n')

fstr = "|{: >11} |{: >11} |{: >11} |{: >11} |"
def run_test(chunks, peers):
    start_time = time.perf_counter()
    os.system("./bittorrent cluster_platform.xml large.xml 2>>tmp 1>out")
    messages = 0
    for line in open('out', 'r').readlines():
        line = line.strip()
        line = line.split(": ");
        if line[0] == 'messages':
            messages += int(line[1])
        elif line[0] == 'status':
            a, b = map(int, line[1].split('/'))
            if a != b:
                mprint('error')
    mprint(fstr.format(chunks, peers, messages, '{:.2f}'.format(time.perf_counter() - start_time)))

mprint("|   chunks   |   peers    |  messages  |  time (s)  |")

for i in range(10):
    mprint("|------------|------------|------------|------------|")
    opts = range(50, 501, 50)
    for chunks in opts:
        compile_with_chunks(chunks)
        for peers in opts:
            gen_peers(peers)
            run_test(chunks, peers)
