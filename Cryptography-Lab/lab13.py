def poly_ops(p1, p2):
    # Addition: Align by padding zeros at the start
    diff = abs(len(p1) - len(p2))
    if len(p1) < len(p2):
        p1 = [0]*diff + p1
    else:
        p2 = [0]*diff + p2
    
    addition = [p1[i] + p2[i] for i in range(len(p1))]
    print(f"\nPoly Add: {addition}")

    # Multiplication: Distributive property
    res_mult = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            res_mult[i + j] += p1[i] * p2[j]
            print(f"  Step: p1[{i}]*p2[{j}] -> adds {p1[i]*p2[j]} to index {i+j}")
    
    print(f"Poly Multiply: {res_mult}")


# ---- Main Program ----
print("Polynomial Operations")
p1 = list(map(int, input("Enter coefficients of first poly (space-separated): ").split()))
p2 = list(map(int, input("Enter coefficients of second poly (space-separated): ").split()))

poly_ops(p1, p2)
