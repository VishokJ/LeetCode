class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = [str(i+1) for i in range(n)]
        for i in range(2, n, 3): a[i] = "Fizz"
        for i in range(4, n, 5): a[i] = "Buzz"
        for i in range(14, n, 15): a[i] = "FizzBuzz"
        return a