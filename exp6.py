maximum, minimum = 1000, -1000

def fun_alphabeta(d, node, maxP, v, A, B):
    if d == 3:
        print(str(v[node]))
        return v[node]
    if maxP:
        best = minimum
        for i in range(0, 2):
            value = fun_alphabeta(d + 1, node * 2 + i, False, v, A, B)
            print("max  " + str(d) + "   " + str(node) + "    " + str(value) + "   " + str(A) + "    " + str(B))
            best = max(best, value)
            A = max(A, best)
            if B <= A:
                break
        else:
            return best
    else:
        best = maximum
        for i in range(0, 2):
            value = fun_alphabeta(d + 1, node * 2 + i, True, v, A, B)
            print("min  " + str(d) + "   " + str(node) + "    " + str(value) + "   " + str(A) + "    " + str(B))
            best = min(best, value)
            B = min(B, best)
            if B <= A:
                break
        else:
            return best

scr = []
x = int(input("Enter total number of leaf node: "))
for i in range(x):
    y = int(input("Enter node value: "))
    scr.append(y)

d = int(input("Enter depth value: "))
node = int(input("Enter node value: "))

print("The optimal value is: ", fun_alphabeta(d, node, True, scr, minimum, maximum))
