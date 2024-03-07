connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]
rome = [city for city in connections if city[1] == 'Rome']
howmany = len(rome)
avg = sum(city[2] for city in rome) / howmany
print("Total flights from Rome:", howmany,\
      "On average the flight takes: ", avg) 