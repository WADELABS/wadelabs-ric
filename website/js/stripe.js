/**
 * Wadelabs RIC - Stripe Integration (v1.2)
 * Handles checkout redirection using Stripe.js
 */

// Initialize Stripe Promise
let stripePromise = null;

function getStripe() {
    if (!stripePromise) {
        if (!CONFIG.stripePublishableKey.includes('pk_test')) {
            console.error('Stripe Publishable Key not configured in js/config.js');
            return null;
        }
        stripePromise = Stripe(CONFIG.stripePublishableKey);
    }
    return stripePromise;
}

async function startCheckout(planKey) {
    const btn = event.target;
    const originalText = btn.innerText;

    // Loading State
    btn.innerText = 'REDIRECTING...';
    btn.classList.add('opacity-75', 'cursor-not-allowed');
    btn.disabled = true;

    try {
        const stripe = await getStripe();
        if (!stripe) {
            alert("Payment configuration missing. Please contact sales.");
            throw new Error("Stripe not initialized");
        }

        const priceId = CONFIG.stripePriceIds[planKey];
        if (!priceId) {
            throw new Error(`Unknown plan key: ${planKey}`);
        }

        // Redirect to Checkout
        const { error } = await stripe.redirectToCheckout({
            lineItems: [{ price: priceId, quantity: 1 }],
            mode: planKey === 'audit' ? 'payment' : 'subscription',
            successUrl: window.location.origin + '/success.html',
            cancelUrl: window.location.origin + '/pricing.html',
        });

        if (error) {
            throw error;
        }

    } catch (err) {
        console.error('Checkout Error:', err);
        alert('Could not initiate checkout. Redirecting to contact page...');
        // Fallback or specific error handling
        btn.innerText = originalText;
        btn.classList.remove('opacity-75', 'cursor-not-allowed');
        btn.disabled = false;
    }
}
