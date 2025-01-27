import argparse
from googlesearch import search
import tldextract

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Extract main domains from Google search results.")
    parser.add_argument("--query", required=True, help="Search query for Google")
    parser.add_argument("--limit", type=int, default=10, help="Number of search results to fetch")
    args = parser.parse_args()

    # Perform the search
    results = search(args.query, num_results=args.limit)

    # Save or display only main domains
    unique_domains = set()  # To avoid duplicates
    with open("bug_bounty_domains.txt", "w") as f:
        for url in results:
            extracted = tldextract.extract(url)
            main_domain = f"{extracted.domain}.{extracted.suffix}"  # Extract only main domain
            if main_domain not in unique_domains:
                unique_domains.add(main_domain)
                print(main_domain)
                f.write(main_domain + "\n")

if __name__ == "__main__":
    main()
