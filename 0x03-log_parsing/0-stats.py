#!/usr/bin/python3
"""Log parsing script."""
import sys


def print_msg(status_codes, total_file_size):
    """Print the statistics of file size and status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count > 0:
            print(f"{code}: {count}")


def main():
    """Main function to parse log lines and compute metrics."""
    total_file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    counter = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) == 7:
                try:
                    file_size = int(parts[6])
                    code = parts[5]
                    if code in status_codes:
                        status_codes[code] += 1
                    total_file_size += file_size
                    counter += 1

                    if counter % 10 == 0:
                        print_msg(status_codes, total_file_size)
                except ValueError:
                    continue
    except KeyboardInterrupt:
        print_msg(status_codes, total_file_size)

    print_msg(status_codes, total_file_size)
