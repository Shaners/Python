# Old code, need to revisit and redo

# Different methods for creating Pseudorandom numbers or PRNGs

# multiply the last number with a factor a, add a constant c and then modulate it by m
a = 3
c = 9
m = 16
xi = 0

def seed(x):
    global xi
    xi = x

def rng():
    global xi
    xi = (a*xi + c)%m
    return xi

for i in range(10):
    print rng()
    

# better one hopfully
seed = ( seed << 13 ) ^ x
return ( 1.0 - ( ( seed * ( seed * seed * 15731 + 789221) + 1376312589) & 7fffffff) / 1073741824.0)

# test this, does it work well?
seed = seed * 1103515245 + 12345
seed = seed / 65536 % 32768