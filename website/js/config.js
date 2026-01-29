/**
 * Wadelabs RIC - Configuration
 */

const CONFIG = {
    // PUBLIC KEY - Safe to get from environment or build
    stripePublishableKey: 'pk_test_REPLACE_WITH_REAL_KEY',

    // PRICE IDs - Map plans to Stripe Price IDs
    stripePriceIds: {
        'starter': 'price_1234567890', // $499/mo
        'pro': 'price_0987654321',     // $1500/mo
        'audit': 'price_1122334455'    // $2500 one-time
    }
};
