"""Command line program for random data generator API."""

# pylint: disable=C0103
# pylint: disable=R0201

import argparse
import sys

from . import RandomDataGenerator

def main():
    """Handle command line program."""

    parser = argparse.ArgumentParser(
        prog=__package__,
        description='Python API for HotBits random data generator'
    )

    parser.add_argument('--length', action='store', default='128')
    parser.add_argument('--apikey', action='store', default='Pseudorandom')
    parser.add_argument('--custom-url', action='store', default=None)

    args = parser.parse_args()

    try:
        generator = RandomDataGenerator(args.custom_url)
        result = generator.generate(args.length, args.apikey)

    except BaseException as err:
        print(str(err), file=sys.stderr)
        sys.exit(1)

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
