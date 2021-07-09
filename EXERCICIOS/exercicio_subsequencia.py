"""
 Crie um programa para encontrar a sub-sequência contínua
 dentro do array A que possua maior soma:

Exemplo 1:

Input: [-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]

Output: 13

Neste primeiro exemplo, o subarray [5, 2, 1, 4, -7, 8] é a sequência contínua
de maior soma contida dentro do array e a soma deste array é 13

Exemplo 2:

Input: [6, -4, -2, 1, -3, 5, -1, 2, 1, 1, -5, 4]

Output: 8

Neste segundo exemplo, o subarray [5, -1, 2, 1, 1] é a sequência contínua de
maior soma contida dentro do array e a soma destes número é 8.

Seu programa só precisa exibir o VALOR da maior soma, não é necessário exibir o
array em questão.
"""


def cubico(arr):
    max_sum = arr[0]
    current_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j+1):
                current_sum += arr[k]
            max_sum = max(max_sum, current_sum)
            current_sum = 0
    return max_sum


def quadratico(arr):
    max_sum = arr[0]
    current_sum = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum


def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in arr[1:]:
        current_sum = max(current_sum+i, i)
        max_sum = max(max_sum, current_sum)
    return max_sum


def subarray(a, size):

    max_so_far = -size - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))
    print(f'SubList is {arr[start:end+1]}')


arr = [-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]
# print(cubico(arr))
# print(quadratico(arr))
# print(kadane(arr))
subarray(arr, len(arr))
