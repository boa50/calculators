def annual_to_monthly(value):
    return (1 + value) ** (1 / 12) - 1


initial = 1.3 * 10e5
withdrawal_per_month = 8000
# interest_rate_per_month = 0.5 / 100
interest_rate_per_month = annual_to_monthly(8 / 100)

remaining = initial

n_months = 0

while remaining > 0:
    remaining -= withdrawal_per_month

    if remaining > 0:
        remaining *= 1 + interest_rate_per_month
        n_months += 1

        # print(n_months, remaining)

        if n_months >= 60 * 12:
            remaining = 1

    else:
        total_years = int(n_months / 12)
        total_months = n_months % 12

        print(f"Able to survive for {total_years} years and {total_months} months")
