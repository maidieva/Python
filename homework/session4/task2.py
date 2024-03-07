list = [i for i in range(1, 51)]
sum_of_even_num_in_list = sum(i for i in list if i % 2 == 0)
print("Sum of all even numbers:", sum_of_even_num_in_list)
mult = 1
for i in list:
    if i % 2 != 0:
        mult*= i
print("Product of all odd numbers:", mult)
larg_num = max(list)
print("Largest number:", larg_num)
