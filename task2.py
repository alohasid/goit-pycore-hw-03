from random import randint

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min > max:
        raise ValueError("Min value cannot be greater than max value")
    if quantity < 1:
        raise ValueError("Quantity cannot be less than 1")
    if quantity > (max - min + 1):
        raise ValueError("Quantity cannot be greater than the number of unique values in the range")
    
    result = set()
    while len(result) < quantity:
        result.add(randint(min, max))
    
    return sorted(result)

print(get_numbers_ticket(1, 49, 6))
# with_exception1 = get_numbers_ticket(49, 1, 6) # ValueError Min value cannot be greater than max value 
# with_exception2 = get_numbers_ticket(1, 49, 0) # ValueError Quantity cannot be less than 1 
# with_exception3 = get_numbers_ticket(1, 49, 50) # ValueError Quantity cannot be greater than the number of unique values in the range 



