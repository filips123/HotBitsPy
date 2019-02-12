"""Example for random data generator API."""

from hotbits import RandomDataGenerator

def main():
    """Handle example."""

    # Create generator
    generator = RandomDataGenerator()

    # Get pseudorandom result with 512 bytes
    result = generator.generate(length=512)

    # Print result
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
