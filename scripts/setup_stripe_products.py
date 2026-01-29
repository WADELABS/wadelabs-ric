import stripe
import sys

# Configure Key
# This script assumes you have set the STRIPE_API_KEY environment variable.
# Or you can manually paste your test key here during local execution.
stripe.api_key = "sk_test_..." # REPLACE WITH YOUR STRIPE SECRET KEY

def create_product(name, amount_cents, interval=None):
    try:
        print(f"Creating {name}...")
        product = stripe.Product.create(name=f"Wadelabs RIC - {name}")
        
        price_data = {
            "unit_amount": amount_cents,
            "currency": "usd",
            "product": product.id,
        }
        
        if interval:
            price_data["recurring"] = {"interval": interval}
            
        price = stripe.Price.create(**price_data)
        return price.id
    except Exception as e:
        print(f"Error creating {name}: {e}")
        return None

def main():
    print("--- Setting up Wadelabs RIC Products (Sandbox) ---")
    
    # 1. Starter: $499/mo
    starter_id = create_product("Starter Plan", 49900, "month")
    
    # 2. Pro: $1500/mo
    pro_id = create_product("Pro Plan", 150000, "month")
    
    # 3. Audit: $2500 one-time
    audit_id = create_product("Launch Certification (Audit)", 250000, None)
    
    print("\n--- CONFIGURATION JSON ---")
    print("Copy these IDs into website/js/config.js:\n")
    print(f"Starter ID: {starter_id}")
    print(f"Pro ID:     {pro_id}")
    print(f"Audit ID:   {audit_id}")
    
    # Generate the full config content for easy copy-paste handling by the agent
    config_content = f"""
const CONFIG = {{
    // PUBLIC KEY (Test Mode)
    stripePublishableKey: 'pk_test_51SuidpEcU4RfdUABsfMyw7YIDaRqDkKWYL06VHrvRERr2Ie8pMAdMiTpF0w7POjzX6rLSVNJpj4dRIfShZTkgFtM00pyEP4Vro', 
    
    // PRICE IDs (Generated {stripe.api_key[:8]}...)
    stripePriceIds: {{
        'starter': '{starter_id}', // $499/mo
        'pro': '{pro_id}',     // $1500/mo
        'audit': '{audit_id}'    // $2500 one-time
    }}
}};
"""
    print("\n--- RAW CONFIG FILE CONTENT ---")
    print(config_content)
    
    # Save directly to file to save a step
    with open('website/js/config.js', 'w') as f:
        f.write(config_content)
    print("Automatically updated website/js/config.js")

if __name__ == "__main__":
    main()
