# Real-Debrid-Link-Converter

A simple Python script that converts a list of links from various file hosters into direct download links using the Real Debrid API.

## Use Case

Imagine you have a list of links from various file hosters (e.g., 1fichier) that you want to convert into multiple direct download links. This script automates the process using the Real Debrid API, saving you time and effort.

## Features

- Converts links from Real Debrid supported file hoster services to direct downloads.
- Provides real-time progress tracking during link processing.
- Outputs results to a specified text file.

## Requirements

- Python 3
- `requests` library

## Setup and Usage

### Step 1: Download the Script

1. Clone the repository or download the script directly:
   
   ```bash
   git clone https://github.com/magacalia/Real-Debrid-Link-Converter.git
   cd Real-Debrid-Link-Converter
   ```

### Step 2: Install Requests Library

2. Ensure you have the requests library installed. If not, install it using pip:
   
   ```bash
   pip install requests
   ```

### Step 3: Get Your API Token

3. Generate your Real Debrid API key:
   Go to [Real Debrid API Token](https://real-debrid.com/apitoken) and generate your API key.
   
   **Disclaimer**: A Premium Real Debrid Subscription is required for the API key to function.

### Step 4: Configure the Script

4. Open `real-debrid-converter.py` in a text editor and replace `'YOUR_API_KEY_HERE'` with your Real Debrid API key:

   ```python
   api_credentials = {'auth_token': 'YOUR_API_KEY_HERE'}

   ```

### Step 5: Prepare Your Input File

5. You must provide your input .txt file, containing the hoster's links, in the same directory as the script.
   By default, the script reads from `hoster-links.txt`. You can modify this file to include your list of links, with each link on a new line.

### Step 6: Run the Script

6. Run the script:

   ```bash
   python real-debrid-converter.py
   ```

   When prompted, enter the name for the output file (must end with .txt).

   After processing all links, the script generates the new file (with the previously specified name) in the same directory. This file maintains the original order of links but presents them as Real Debrid direct download links.
