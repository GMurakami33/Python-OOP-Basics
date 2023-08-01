"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self, start=0):
        """Initialize the SerialGenerator with a starting value"""
        self.start = start
        self.next_serial = start

    def __repr__ (self):
        return f"SerialGenerator(start={self.start}, next_serial={self.next_serial})"

    def generate (self):
        """Generates next serial number in increments of 1"""
        self.next_serial +=1 
        return self.next_serial - 1
    
    def reset (self):
        """Resets the generator to initial value"""
        self.next_serial = self.start
