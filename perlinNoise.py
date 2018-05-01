# This is old old code that is broken that I don't understand well enough

"""
# Import random function, can I make my own? May not be any point of doing it, actaully we shouldn't use random with perlin...
import random, time

def gen_pseudorandom_one(seed):
    seed = ( seed << 13 ) ^ x
    return ( 1.0 - ( ( seed * ( seed * seed * 15731 + 789221) + 1376312589) & 7fffffff) / 1073741824.0)

def gen_pseudorandom_two(seed):
    seed = ( seed << 13 ) ^ x
    return ( 1.0 - ( ( seed * ( seed * seed * 15731 + 789221) + 1376312589) & 7fffffff) / 1073741824.0)

# Define the perlin noise function, perlin noise outdated maybe change this to simplex
def gen_perlin_noise(seed, points):
    noise = []
    i = 0   
"""

# Lets try this again
# This is too much, I'll have to revisit after I've learned more

# Import the Math module
import math

# Create the permutation tuples
p = (
151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,
30,69,142,8,99,37,240,21,10,23,190,6,148,247,120,234,75,0,26,197,
62,94,252,219,203,117,35,11,32,57,177,33,88,237,149,56,87,174,20,
125,136,171,168,68,175,74,165,71,134,139,48,27,166,77,146,158,231,
83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,102,
143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,18,169,200,
196,135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,
250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,
58,17,182,189,28,42,223,183,170,213,119,248,152,2,44,154,163,70,
221,153,101,155,167,43,172,9,129,22,39,253,19,98,108,110,79,113,
224,232,178,185,112,104,218,246,97,228,251,34,242,193,238,210,144,
12,191,179,162,241,81,51,145,235,249,14,239,107,49,192,214,31,181,
199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,138,236,
205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180, # Starts again, why?
151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,
30,69,142,8,99,37,240,21,10,23,190,6,148,247,120,234,75,0,26,197,
62,94,252,219,203,117,35,11,32,57,177,33,88,237,149,56,87,174,20,
125,136,171,168,68,175,74,165,71,134,139,48,27,166,77,146,158,231,
83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,102,
143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,18,169,200,
196,135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,
250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,
58,17,182,189,28,42,223,183,170,213,119,248,152,2,44,154,163,70,
221,153,101,155,167,43,172,9,129,22,39,253,19,98,108,110,79,113,
224,232,178,185,112,104,218,246,97,228,251,34,242,193,238,210,144,
12,191,179,162,241,81,51,145,235,249,14,239,107,49,192,214,31,181,
199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,138,236,
205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180)

# Linear interpolation between two points
def lerp(t, a, b):
    return a + t * (b - a)
    
# why?
def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)
  
# what's this?
def grad(hash, x, y, z):
    h = hash & 15
    if h < 8:
        u = x
    else:
        u = y
    if h < 4:
        v = y
    elif h == 12 or h == 14:
        v = x
    else:
        v = z
    if h & 1 != 0:
        u = -u
    if h & 2 != 0:
        v = -v
    return u + v
  
# meat and potatoes here
# Needs to be supplied 3 values, how do I get these? where do they come from?
# is this simplix noise? yes should be
def pnoise(x, y, z):
    # defines p as global variable, p contains set of tuples
    global p
    # sets upercase x to an integer that is the floor of x 
    X = int(math.floor(x)) & 255 # why bitwise operator here??
    Y = int(math.floor(y)) & 255 # does this ensure that we have a value between 1 and 255??
    Z = int(math.floor(z)) & 255
    x -= math.floor(x) # take x and - the floor of x
    y -= math.floor(y)
    z -= math.floor(z)
    
    u = fade(x) # does some weird conversion here, why? how is this fading?
    v = fade(y)
    w = fade(z)
    
    A =  p[X] + Y # take X tuple and add Y to it
    AA = p[A] + Z # take A tuple and add Z to it
    AB = p[A + 1] + Z # weird
    B =  p[X + 1] + Y # this is like A but permutation plus 1
    BA = p[B] + Z # this is like AA
    BB = p[B + 1] + Z # this is like AB
    
    pAA = p[AA] # what?
    pAB = p[AB] # we're getting permution values
    pBA = p[BA]
    pBB = p[BB]
    pAA1 = p[AA + 1] # Getting the same permution values but one index higher
    pBA1 = p[BA + 1]
    pAB1 = p[AB + 1]
    pBB1 = p[BB + 1]
    
    gradAA =  grad(pAA, x,   y,   z) # gradients computation I believe
    gradBA =  grad(pBA, x-1, y,   z)
    gradAB =  grad(pAB, x,   y-1, z)
    gradBB =  grad(pBB, x-1, y-1, z)
    gradAA1 = grad(pAA1,x,   y,   z-1)
    gradBA1 = grad(pBA1,x-1, y,   z-1)
    gradAB1 = grad(pAB1,x,   y-1, z-1)
    gradBB1 = grad(pBB1,x-1, y-1, z-1)
    return lerp(w, # w is fade z?
    lerp(v, lerp(u, gradAA, gradBA), lerp(u, gradAB, gradBB)),
    lerp(v, lerp(u, gradAA1,gradBA1),lerp(u, gradAB1,gradBB1)))
    
    