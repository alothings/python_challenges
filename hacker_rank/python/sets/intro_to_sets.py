"""
Set: collection of unordered elements without duplicates
Task: Average of plants with distinct heights
Input: first line N: total plants
second line contains n space separated heights

Sample input:
10
161 182 161 154 176 170 167 171 170 174

Output:
169.375
"""

def average(array):
    return sum(set(array))/len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))   # map applies function to list
    result = average(arr)
    print(result)
