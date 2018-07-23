#!usr/bin/python3
def mini_max_sum(arr):
    """function to find the minimum and maximum values by summing exactly four of five integers""" 
    tot = sum(arr)
    result = []
    for i in arr:
        result.append(tot - i)
    print("{} {}".format(min(result), max(result)))

if __name__ == "__main__":
    arr = list(map(int, input("Please input 5 space separated integers\n").strip().split(' ')))
    #error handling for when the user inputs less than 5 integers
    if(len(arr) == 5):
        mini_max_sum(arr)
    else:
        print("\nPlease input 5 space separated integers")
