import argparse
import subprocess
from tabulate import tabulate
from traceroute_parser import TracerouteParser


def main():
    parser = argparse.ArgumentParser(
        description='Super fancy tracerouter launcher.'
                    'Enter the IP address or domain name and enjoy!')

    parser.add_argument('target', type=str,
                        help='target IP or domain name')
    parser.add_argument('-w', type=int,
                        help='Option used to specify the amount of time (in seconds) that traceroute will'
                             ' wait for an ICMP response message. '
                             'The allowed range for wait_time is 1 to 300 seconds; the default is 5 seconds.',
                        required=False, default=5)
    parser.add_argument('-m', type=int,
                        help='Option used to specify the maximum TTL value for outgoing ICMP datagrams. '
                             'The allowed range for max_ttl is 1 to 255; the default value is 30.',
                        required=False, default=30)
    args = parser.parse_args()
    output = subprocess.check_output(["traceroute", "-w", str(args.w), "-m", str(args.m), args.target])
    print("Traceroute completed. Processing...\n")
    parser = TracerouteParser()
    traceroute_result = parser.parse_data(output.decode("utf-8"))
    table_rows, table_header = traceroute_result.get_table()
    print(tabulate(table_rows, headers=table_header, tablefmt='orgtbl'))


if __name__ == "__main__":
    main()
