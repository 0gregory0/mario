import polars as pl


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_even_perfect_numbers(limit):
    results = []
    p = 2
    count = 0

    while count < limit:
        mersenne_prime_candidate = 2**p - 1
        if is_prime(mersenne_prime_candidate):
            even_perfect_number = 2 ** (p - 1) * mersenne_prime_candidate
            results.append((count + 1, p, even_perfect_number))
            count += 1
        p += 1

    return results


def main():
    limit = 10
    table = generate_even_perfect_numbers(limit)
    df = pl.DataFrame(table, schema=["Index", "Prime", "Even Perfect Number"])
    excel_file = "even_perfect_numbers.xlsx"
    df.write_excel(excel_file)
    print(f"Data exported to {excel_file}")


if __name__ == "__main__":
    main()
