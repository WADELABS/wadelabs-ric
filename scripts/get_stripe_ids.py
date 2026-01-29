import stripe

# This script assumes you have set the STRIPE_API_KEY environment variable.
stripe.api_key = "sk_test_..." # REPLACE WITH YOUR STRIPE SECRET KEY

def list_prices():
    print("Fetching Price IDs...")
    prices = stripe.Price.list(limit=10, expand=['data.product'])
    
    config_map = {}
    
    for p in prices.data:
        prod_name = p.product.name
        if "Starter" in prod_name:
            config_map['starter'] = p.id
        elif "Pro" in prod_name:
            config_map['pro'] = p.id
        elif "Audit" in prod_name or "Certification" in prod_name:
            config_map['audit'] = p.id
            
    print("\nFOUND IDs:")
    print(f"Starter: {config_map.get('starter', 'NOT FOUND')}")
    print(f"Pro:     {config_map.get('pro', 'NOT FOUND')}")
    print(f"Audit:   {config_map.get('audit', 'NOT FOUND')}")

if __name__ == "__main__":
    list_prices()
