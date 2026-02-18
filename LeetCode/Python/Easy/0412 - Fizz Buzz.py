class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = []
        for i in range(n):
            if ((i + 1) % 3 == 0) and ((i + 1) % 5 == 0):
                array.append("FizzBuzz")
            else:
                if (i + 1) % 3 == 0:
                    array.append("Fizz")
                elif (i + 1) % 5 == 0:
                    array.append("Buzz")
                else: array.append(str(i + 1))
        return array
