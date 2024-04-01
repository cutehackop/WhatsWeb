import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import time

# Typing animation function
def type_with_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  # Adjust speed as needed
    print()

# Banner
banner = r'''
.-.
       .'   `.          --------------------------------
       :g g   :         | WhatsWeB - Scanner - Scan Any web |
       : o    `.        |       @CODE BY CUTEHACK99YT    |
      :         ``.     --------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
'''

# Function to scan a website
def scan_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract information from the website
            # Example: Find all links
            links = soup.find_all('a')
            
            # Print the results with typing animation
            type_with_animation(Fore.GREEN + f"Scanning {url}...")
            type_with_animation(Fore.WHITE + f"Links found: {len(links)}")
            for link in links:
                type_with_animation(link.get('href'))

            # Check for cookies
            cookies = response.cookies
            type_with_animation(Fore.CYAN + f"Cookies found: {cookies}")

            # Get website IP and country
            ip_address = requests.get('https://api64.ipify.org').text
            type_with_animation(Fore.YELLOW + f"IP Address: {ip_address}")
            ip_info = requests.get(f'https://ipinfo.io/{ip_address}/json').json()
            type_with_animation(Fore.YELLOW + f"Country: {ip_info.get('country')}")

            # Find email addresses
            email_addresses = soup.find_all('a', href=lambda href: href and 'mailto:' in href)
            type_with_animation(Fore.MAGENTA + f"Email addresses found: {len(email_addresses)}")
            for email in email_addresses:
                type_with_animation(email.get('href').replace('mailto:', ''))

            # Check for Apache server
            server_header = response.headers.get('Server')
            if server_header and 'Apache' in server_header:
                type_with_animation(Fore.GREEN + "Apache server detected")

            # Check for response codes 404 or 202
            if response.status_code == 404:
                type_with_animation(Fore.RED + "404 Not Found")
            elif response.status_code == 202:
                type_with_animation(Fore.YELLOW + "202 Accepted")

            # Check for PHP type
            if 'PHP' in response.text:
                type_with_animation(Fore.CYAN + "PHP detected")

            # Check for Google Analytics
            if 'Google Analytics' in response.text:
                type_with_animation(Fore.BLUE + "Google Analytics detected")

            # Check for frames
            frames = soup.find_all('frame')
            if frames:
                type_with_animation(Fore.MAGENTA + f"Frames found: {len(frames)}")

            # Check for uncommon headers
            uncommon_headers = [header for header in response.headers if 'X-' in header]
            if uncommon_headers:
                type_with_animation(Fore.YELLOW + "Uncommon headers found:")
                for header in uncommon_headers:
                    type_with_animation(header)

        else:
            type_with_animation(Fore.RED + f"Failed to scan {url}. Status code: {response.status_code}")
    except Exception as e:
        type_with_animation(Fore.RED + f"An error occurred: {e}")

# Input from the user
if __name__ == "__main__":
    # Show banner
    print(banner)

    # Get the website URL from the user
    target_url = input("Enter the website URL to scan: ")
    
    # Show information message
    print("\n============SHOW INFORMATION HERE =============")

    # Scan the website
    scan_website(target_url)
