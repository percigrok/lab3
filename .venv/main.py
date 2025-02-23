# 1) Определение палиндрома без рекурсии
# def is_palindrome_iterative(sequence):
#     return sequence == sequence[::-1]
#
# print(is_palindrome_iterative([1, 2, 3, 2, 1]))
# print(is_palindrome_iterative("spam"))

# 2) Определение палиндрома с рекурсией
# def is_palindrome_recursive(sequence):
#     if len(sequence) <= 1:
#         return True
#     if sequence[0] != sequence[-1]:
#         return False
#     return is_palindrome_recursive(sequence[1:-1])
#
# print(is_palindrome_recursive([1, 2, 3, 2, 1]))
# print(is_palindrome_recursive("spam"))


# 3) Вычисление последовательности определенной по рекуррентной формуле без рекурсии
# def sequence_iterative(n):
#     if n <= 3:
#         return 1
#
#     seq = [1, 1, 1]
#     for i in range(3, n):
#         seq.append(seq[i - 1] + seq[i - 3])
#     return seq[-1]
#
# print(sequence_iterative(5))
# print(sequence_iterative(10))

# # 4) Вычисление последовательности определенной по рекуррентной формуле с помощью рекурсии
# def sequence_recursive(n):
#     if n <= 3:
#         return 1
#     return sequence_recursive(n - 1) + sequence_recursive(n - 3)
#
#
# print(sequence_recursive(5))
# print(sequence_recursive(10))