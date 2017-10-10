# MathCore class
class MathCore:
    def sum(self, v1, v2):
        """Sum `v1` and `v2`
        and return the sum value.
        """
        return v1 + v2

    def subtract(self, v1, v2):
        """Subtract `v1` and `v2`
        and return the subtracted value.
        """
        return v1 - v2

    def multiply(self, v1, v2):
        """Multiply `v1` and `v2`
        and return the multiplied value.
        """
        value = v1
        for i in range(1, v2):
            value = self.sum(value, v1)
        return value

    def division(self, v1, v2):
        """Division `v1` and `v2`
        and return the divisioned value.
        """
        value = v1
        count = 0
        while (value >= v2):
            value = self.subtract(value, v2)
            count = self.sum(count, 1)
        return count

    def pow(self, v1, v2):
        """`v1` to the power of `v2`
        and return the new value.
        """
        value = v1
        for i in range(1, v2):
            value = self.multiply(value, v1)
        return value

    def mod(self, v1, v2):
        """Division `v1` and `v2`
        and return the rest of the value.
        """
        division = self.division(v1, v2)
        multiplication = self.multiply(division, v2)
        return self.subtract(v1, multiplication)
