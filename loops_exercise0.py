specified_num = int(input("Enter the number for which you want the multiplication table: "))
specified_limit = int (input("Enter the limit up to which you want the multiplication table generated: "))

print (f"Multiplication Table for {specified_num}: ")
for i in range (1, specified_limit + 1):
    product = specified_num * i
    print (f"{specified_num} x {i} = {product}")