#   Project Euler Solutions 
#   Edward Barthelemy
#   A good warmup back into it
#   Finished 09/01/16 

def main():
    answer = 0
    for x in range(1,1000):
        if x % 3 == 0 or x % 5 == 0:
            answer += x
    return str(answer)

print(main())