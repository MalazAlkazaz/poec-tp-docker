def apply_vat(price: float, percent: float):
    if isinstance(price , int):
        price = float(price)
    if isinstance(percent , int):
        percent = float(percent)
    if not isinstance(price , float):
       raise ValueError(f'Price (${price}) is not a number')
    if price <= 0:
        raise ValueError(f'Price (${price}) is negative ou null')
    if percent < 0 or percent >100:
        raise ValueError(f'la TVA {percent}) est hors la loi ! out of range')
    return price * (1+percent/100)