# Token Decoder Script

This script decodes tokens from a specified range using the `tiktoken` library and saves the decoded strings into two CSV files:
1. `tokens.csv` - Contains all decoded tokens.
2. `zh-cn.csv` - Contains only decoded tokens that include Chinese characters.

## Prerequisites

- Python 3.x
- `tiktoken` library

## Installation

Install the required libraries using pip:
```bash
pip install tiktoken
```

## Usage

Run the script to generate the CSV files:
```bash
python decode_tokens.py
```

## Script Details

### `decode_tokens.py`

```python
import csv
import tiktoken
import re

# Get the encoding object
encoding = tiktoken.get_encoding("o200k_base")

# Define the range of token IDs to iterate over
# Assuming the encoding supports up to 200,000 tokens, adjust as needed
token_range = range(200000)

# Open two CSV files, one for all tokens and one for tokens containing Chinese characters
with open('tokens.csv', 'w', newline='', encoding='utf-8') as csvfile_all, \
     open('zh-cn.csv', 'w', newline='', encoding='utf-8') as csvfile_cn:
    
    csvwriter_all = csv.writer(csvfile_all, escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    csvwriter_cn = csv.writer(csvfile_cn, escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    
    # Write headers
    csvwriter_all.writerow(['Token ID', 'Decoded String'])
    csvwriter_cn.writerow(['Token ID', 'Decoded String'])
    
    # Iterate over token IDs and write to CSV
    for token_id in token_range:
        try:
            # Decode single token bytes and convert to string
            decoded_bytes = encoding.decode_single_token_bytes(token_id)
            decoded_string = decoded_bytes.decode('utf-8')
            
            # Write all tokens to tokens.csv
            csvwriter_all.writerow([token_id, decoded_string])
            
            # Check if the string contains Chinese characters and write to zh-cn.csv
            if re.search(r'[\u4e00-\u9fff]', decoded_string):
                csvwriter_cn.writerow([token_id, decoded_string])
        
        except Exception as e:
            print(f"Skipping token_id {token_id} due to error: {e}")
            continue
```

### Key Points

- **Token Decoding:** Uses the `tiktoken` library to decode tokens.
- **CSV Output:** Outputs all decoded tokens to `tokens.csv` and tokens containing Chinese characters to `zh-cn.csv`.
- **Chinese Character Filter:** Uses a regular expression to check for Chinese characters.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.