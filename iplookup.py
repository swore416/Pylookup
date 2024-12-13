import requests

ipinfo_api = 'https://ipinfo.io'
ipinfo_token = 'ENTER TOKEN HERE'
vpn_api = 'https://api.ipquery.io/'

def get_info(ip):
    ipinfo_url = f"{ipinfo_api}/{ip}?token={ipinfo_token}"
    vpn_url = f"{vpn_api}{ip}"

    ip_response = requests.get(ipinfo_url)
    vpn_response = requests.get(vpn_url)

    ip_data = None
    vpn_data = None

    if ip_response.status_code == 200:
        ip_data = ip_response.json()
    else:
        print(f"Failed to retrieve data from ipinfo.io {ip_response.status_code}")

    if vpn_response.status_code == 200:
        vpn_data = vpn_response.json()
    else:
        print(f"Failed to retrieve data from ipquery.io {vpn_response.status_code}")

    return ip_data, vpn_data

ip = input("Enter IP: ")
ip_info, vpn_info = get_info(ip)

if ip_info:
    print(f"IP: {ip_info['ip']}")
    print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
    print(f"City: {ip_info.get('city', 'N/A')}")
    print(f"State/Region: {ip_info.get('region', 'N/A')}")
    print(f"Country: {ip_info.get('country', 'N/A')}")
    print(f"Coordinates: {ip_info.get('loc', 'N/A')}")
    print(f"ISP: {ip_info.get('org', 'N/A')}")
    print(f"Zip Code: {ip_info.get('postal', 'N/A')}")
    print(f"Timezone: {ip_info.get('timezone', 'N/A')}")

if vpn_info:
    if 'risk' in vpn_info:
        is_mobile = vpn_info['risk'].get('is_mobile', 'N/A')
        is_vpn = vpn_info['risk'].get('is_vpn', 'N/A')
        is_tor = vpn_info['risk'].get('is_tor', 'N/A')
        is_proxy = vpn_info['risk'].get('is_proxy', 'N/A')
        is_datacenter = vpn_info['risk'].get('is_datacenter', 'N/A')

        print(f"Is Mobile: {is_mobile}")
        print(f"Is VPN: {is_vpn}")
        print(f"Is Tor: {is_tor}")
        print(f"Is Proxy: {is_proxy}")
        print(f"Is Datacenter: {is_datacenter}")
    else:
        print("Information is not available.")
