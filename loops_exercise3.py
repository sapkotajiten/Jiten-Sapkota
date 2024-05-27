for i in range (1, 9+1):
    if i == 3:
        print (f"Skipping {i} in the inner loop")
    elif i == 7:
        print (f"Reached {i}, breaking the outer loop")
        break
    print(i)