N_max = 5
n = 0
n_list = []

for n in range(N_max):
#Because the if statement belongs to the for loop, we have to indent it to the right
    if n < 3:
#Because the append command belongs to the if statement we have to indent it 2x times to the right
        n_list.append(n)

print(n_list)