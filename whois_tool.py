import whois


def display_whois(domain):
    try:
        # Query WHOIS information for the domain
        information = whois.whois(domain)

        print("\n" + "=" * 60)
        print("              WHOIS INFORMATION TOOL")
        print("=" * 60)

        print(f"\nDomain Name     : {information.domain_name}")
        print(f"Registrar       : {information.registrar}")
        print(f"Creation Date   : {information.creation_date}")
        print(f"Expiration Date : {information.expiration_date}")
        print(f"Updated Date    : {information.updated_date}")

        print("\nName Servers")
        print("-" * 60)

        if information.name_servers:
            for server in information.name_servers:
                print(f"[+] {server}")
        else:
            print("[!] Name server information unavailable.")

        print("\nDomain Status")
        print("-" * 60)

        if information.status:
            if isinstance(information.status, list):
                for status in information.status:
                    print(f"[+] {status}")
            else:
                print(f"[+] {information.status}")
        else:
            print("[!] Status information unavailable.")

        print("=" * 60)

    except Exception as error:
        print("\n[!] Unable to retrieve WHOIS information.")
        print(f"Error: {error}")


def main():
    print("WHOIS Information Tool")
    print("----------------------")

    domain = input("Enter domain name: ").strip()

    if not domain:
        print("[!] Please enter a domain.")
        return

    # Remove protocol if the user enters a complete URL
    domain = domain.replace("https://", "")
    domain = domain.replace("http://", "")
    domain = domain.split("/")[0]

    display_whois(domain)


if __name__ == "__main__":
    main()