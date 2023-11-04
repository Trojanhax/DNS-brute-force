# DNS brute force

The DNS Lookup Tool is a Python script that performs DNS lookups for a list of IP addresses and appends a domain name to each IP address. This tool can be helpful for discovering domain names associated with specific IP addresses.

## Features

- Resolve IP addresses to domain names using the `host` command.
- Input a list of IP addresses from a file.
- Customize the domain name to append to each IP address.
- Save the results to an output file.

## Usage

1. Clone the repository or download the script to your local machine.

2. Ensure you have Python 3.x installed.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script with the following command:

```bash
python script.py -f <input_file> -d <domain_name> -o <output_file>
```
Replace <input_file>, <domain_name>, and <output_file> with your desired values:

- <input_file>: Path to the file containing the list of IP addresses.
- <domain_name>: The domain name you want to append to each IP address.
- <output_file>: Path to the file where you want to save the results.

For example:

```bash
python script.py -f Subdomain.txt -d example.com -o results.txt
```
1. The script will read the list of IP addresses from the input file, perform DNS lookups, and save the results to the output file.
# Donate Me
<a href="https://www.buymeacoffee.com/trojanhax" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

# License
This project is licensed under the MIT License - see the LICENSE file for details.
