while True:
    try:
        n = int(input('No: '))
    except ValueError:
        continue
    if n <= 0 or n > 8:
        continue
    for i in range(1, n+1):
            left = ('#'*i).rjust(n)
            right = '#'*i
            print(left + ' ', right)
    break
