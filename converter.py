def convert_currency(amount, from_currency, to_currency):
    """Core logic for currency conversion using a base-USD dictionary."""
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 151.0
    }
    
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates or to_currency not in rates:
        raise ValueError(f"Currency {from_currency} or {to_currency} not supported.")
        
    usd_amount = amount / rates[from_currency]
    return round(usd_amount * rates[to_currency], 2)