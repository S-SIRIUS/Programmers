import sys
sys.setrecursionlimit(1000000)

preorder = [int(line) for line in sys.stdin if line.strip()]

def postorder(l, r):
    if l >= r:
        return
    root = preorder[l]

    mid = r
    for i in range(l+1, r):
        if preorder[i] > root:
            mid = i
            break

    postorder(l+1, mid)

    postorder(mid, r)
    print(root)

postorder(0, len(preorder))