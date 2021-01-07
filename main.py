import requests
import os

def banner():
    print("""
██╗    ██╗██╗  ██╗██╗ ██████╗██╗  ██╗
██║    ██║██║  ██║██║██╔════╝██║  ██║
██║ █╗ ██║███████║██║██║     ███████║
██║███╗██║██╔══██║██║██║     ██╔══██║
╚███╔███╔╝██║  ██║██║╚██████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝
                                     
                        ██╗██████╗   
                        ██║██╔══██╗  
                        ██║██████╔╝  
                        ██║██╔═══╝   
                        ██║██║       
                        ╚═╝╚═╝  
    """)

def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    banner()

    ip_input = input('Enter the IP for a query: ')

    request = requests.get(
        'http://ip-api.com/json/{}'.format(ip_input))

    ip_data = request.json()

    if 'message' not in ip_data:
        clear()
        banner()
        print("==> IP FOUND <==")

        print("IP: {}".format(ip_data['query']))
        print("Country: {}".format(ip_data['country']))
        print("Country Code: {}".format(ip_data['countryCode']))
        print("Region: {}".format(ip_data['region']))
        print("Region Name: {}".format(ip_data['regionName']))
        print("City: {}".format(ip_data['city']))
        print("Postal Code: {}".format(ip_data['zip']))
        print("Lat: {}".format(ip_data['lat']))
        print("Lon: {}".format(ip_data['lon']))
        print("Time Zone: {}".format(ip_data['timezone']))
        print("ISP: {}".format(ip_data['isp']))
        print("Org: {}".format(ip_data['org']))
        print("ASN: {}".format(ip_data['as']))
    else:
        clear()
        print('{}: Invalid IP.'.format(ip_input))

    print('---------------------------------')
    option = int(
        input("""
Do you want to make a new consultation?

1. Yes
2. Get out

>>> """))
    if option == 1:
        clear()
        main()

    elif option == 2:
        clear()
        banner()
        exit()

    else:
        clear()
        banner()
        print("Invalid option.")


if __name__ == '__main__':
    main()
