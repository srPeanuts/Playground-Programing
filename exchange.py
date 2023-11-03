def exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_fee = (exchange_rate * (spread/100) + exchange_rate)
    y = ((budget / exchange_fee) // denomination) * denomination
    return int(y)

print(exchangeable_value(127.25, 1.20, 10, 20)) # should print 80