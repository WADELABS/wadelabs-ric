/**
 * Wadelabs RIC - Stripe Checkout Stub
 * Simulates redirect to Stripe Payment Links
 */

const STRIPE_LINKS = {
    'starter': 'https://buy.stripe.com/test_starter_plan',
    'pro': 'https://buy.stripe.com/test_pro_plan',
    'audit': 'https://buy.stripe.com/test_audit_one_time'
};

function startCheckout(planIds) {
    console.log(`Initiating checkout for plan: ${planIds}`);

    const btn = event.target;
    const originalText = btn.innerText;

    // Simulate loading state
    btn.innerText = 'REDIRECTING...';
    btn.classList.add('opacity-75', 'cursor-not-allowed');

    setTimeout(() => {
        // In production, this would be Stripe.redirectToCheckout or window.location
        if (STRIPE_LINKS[planIds]) {
            alert(`[STUB] Redirecting to Stripe Checkout for ${planIds.toUpperCase()}\nURL: ${STRIPE_LINKS[planIds]}`);
            // window.location.href = STRIPE_LINKS[planId];
        } else {
            console.error('Unknown plan ID');
        }

        // Reset for demo
        btn.innerText = originalText;
        btn.classList.remove('opacity-75', 'cursor-not-allowed');
    }, 1000);
}
