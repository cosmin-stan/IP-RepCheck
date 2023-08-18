# Recorded Future API Python Script: IP Reputation and Risk Assessment

This Python script allows you to retrieve and consolidate IP address information from the Recorded Future API.
The script reads a list of IP addresses from a text file (ip_addresses.txt), queries the Recorded Future API for risk and AI insights data and presents the results in the terminal (*RF-IPcheck.py*) OR in xls format (*RF-IPcheck_xls.py*).


## Prerequisites

Before using this script, make sure you have:

- Recorded Future API (Threat module API key)
- Python 3.x installed
- Python packages (requests, xlwt)
```
pip install requests
pip install xlwt
```

## Usage

1. Clone or download this repository to your local machine.
2. Create a text file named *ip_addresses.txt* in the same directory as the script. Populate the file with the list of IP addresses you want to query, one IP address per line.
3. Open a terminal or command prompt and navigate to the script directory.
4. Run the script using the following command:

```
python3 RF-IPcheck.py
```
This script will query the RF API for each IP address listed in the txt file and display the info in the terminal.

OR
```
python3 RF_IPcheck_xls.py
```
This script will query the RF API for each IP address listed in the txt file and create an Excel file named ip_address.xls containing the information.
