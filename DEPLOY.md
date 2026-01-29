# Wadelabs RIC - Deployment Guide

## 1. Source Code
The code is hosted on GitHub:
> **Repo**: https://github.com/wade-technologies/wadelabs-ric (Check your terminal output for the exact URL)

## 2. Infrastructure (Hosting)
Since this is a static website (HTML/Tailwind), the fastest way to deploy is via **Vercel** or **Netlify**.

### Option A: Vercel (Fastest)
Run this in your terminal:
```bash
cd website
npx vercel deploy --prod --token xiOhdPqfaXfLZHah9XwQkBqR
```

## 3. Stripe Integration (Payments)
To enable real payments:
1.  Open `website/js/config.js`.
2.  Replace the placeholders with your **Stripe Live Keys**:
    ```javascript
    const CONFIG = {
        stripePublishableKey: 'pk_live_...', 
        stripePriceIds: {
             'starter': 'price_...', 
             'pro': 'price_...', 
             'audit': 'price_...'
        }
    };
    ```
3.  Commit and push the changes:
    ```bash
    git add website/js/config.js
    git commit -m "Update Stripe configuration"
    git push
    ```

## 4. Automation (Optional)
The GitHub Actions workflow files (if added) will automatically check code integrity on push.
