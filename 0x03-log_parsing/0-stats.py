#!/usr/bin/python3
import sys


def print_stats(file_size, status_codes):
    """Print statistics about file size and status codes."""
    print(f"File size: {file_size}")
    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")


def main():
    """Main function to process log lines and print statistics."""
    file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) == 7:
                try:
                    size = int(parts[6])
                    code = int(parts[5])
                    if code in status_codes:
                        status_codes[code] += 1
                    file_size += size
                    count += 1

                    if count % 10 == 0:
                        print_stats(file_size, status_codes)
                except ValueError:
                    continue
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)


if __name__ == "__main__":
    main()
