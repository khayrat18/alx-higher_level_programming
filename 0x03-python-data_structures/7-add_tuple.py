# #!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0

    if tuple_a:
        sum1 += tuple_a[0]
    if len(tuple_b) > 1:
        sum2 += tuple_a[1]
    if tuple_b:
        sum1 += tuple_b[0]
    if len(tuple_b) > 1:
        sum2 += tuple_b[1]
    return (sum1, sum2)