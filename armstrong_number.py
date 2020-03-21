"""
@Author: Subarata Talukder
A number P, determine whether the number is Armstrong number or not.
A positive integer of n digits is called an Armstrong number of order R (order is number of digits) if.
abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
"""


# Define a class
class Armstrong():
    # Take range called limit for finding Armstrong
    def __init__(self, limit: int):
        self.limit = limit

    # Private method to check If Armstrong
    def _is_armstron(self, val: int) -> bool:
        parts = [int(x) for x in str(val)]
        count = 0
        for v in parts:
            count += v ** len(parts)
        return (count == val)

    # Show result as a list
    def show_armstrong(self):
        print([x for x in range(self.limit) if self._is_armstron(x)])


# get instance of Armstrong
arm = Armstrong(1000)

# Call the method
arm.show_armstrong()
