

def validate_title(title):
    title = title.strip()

    if not title.strip():
        return False

    if title.isdigit():
        return False

    return True


def validate_amount(amount):
    amount = amount.strip()

    if not amount:
        return False

    try:
        amount = float(amount)
        if amount <= 0:
            return False
        return True

    except ValueError:
        return False
