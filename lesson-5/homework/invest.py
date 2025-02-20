def invest(amount: float, rate: float, years: int) -> float:
    for i in range(1, years+1):
        amount = round(amount + (amount / 100 * rate), 2)
        print(f"year {i}: {amount}")

def main():
    amount = float(input("Enter the initial amount: "))
    rate = float(input("Enter the rate: "))
    years = int(input("Enter the years: "))
    invest(amount, rate, years)

main()