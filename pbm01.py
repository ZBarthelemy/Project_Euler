#   Project Euler Solutions 
#   Edward Barthelemy

def main():
    answer = 0
    for x in range(1,1000):
        if x % 3 == 0 or x % 5 == 0:
            answer += x
    return str(answer)

print(main())