import re

def get_card_flag(card_number):
    card_number = re.sub(r'\D', '', card_number)  # Remove non-numeric characters
    
    cards = {
        "visa": r"^4[0-9]{12}(?:[0-9]{3})",
        "mastercard": r"^5[1-5][0-9]{14}",
        "diners": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}",
        "amex": r"^3[47][0-9]{13}",
        "discover": r"^6(?:011|5[0-9]{2})[0-9]{12}",
        "hipercard": r"^(606282\d{10}(\d{3})?)|(3841\d{15})",
        "elo": r"^((((636368)|(438935)|(504175)|(451416)|(636297))\d{0,10})|((5067)|(4576)|(4011))\d{0,12})",
        "jcb": r"^(?:2131|1800|35\d{3})\d{11}",
        "aura": r"^(5078\d{2})(\d{2})(\d{11})$"
    }
    
    for flag, pattern in cards.items():
        if re.match(pattern, card_number):
            return flag
    
    return False

# Exemplo de uso
card_number = "4111111111111111"
print(get_card_flag(card_number))
