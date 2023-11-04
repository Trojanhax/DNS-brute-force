import subprocess
import argparse

def host_lookup(ip, domain):
  """Performs a DNS lookup for the given IP address and domain."""
  result = subprocess.run(["host", f"{ip}.{domain}"], capture_output=True, text=True)
  return result.stdout

def main():
    parser = argparse.ArgumentParser(description='Resolve IP addresses to domain names using the host command.')
    parser.add_argument('-f', '--file', required=True, help='Path to the file containing IP addresses')
    parser.add_argument('-d', '--domain', required=True, help='Domain name to append to each IP address')
    parser.add_argument('-o', '--output', required=True, help='Path to the output file for saving the results')

    args = parser.parse_args()

    # Read the IP addresses from the file
    ips = []
    with open(args.file, 'r') as f:
        for line in f:
            ips.append(line.strip())

    # Perform DNS lookups for all IP addresses
    results = []
    for ip in ips:
        result = host_lookup(ip, args.domain)
        results.append(result)

    # Save the results to the output file
    with open(args.output, 'w') as output_file:
        for result in results:
            output_file.write(result)

if __name__ == '__main__':
    main()
