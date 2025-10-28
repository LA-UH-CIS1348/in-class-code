
def calculate_total_1(bill):
    tax = bill * 0.0825
    tip = bill * 0.2
    total = bill+tip+tax
    return total

def calculate_total_2(bill, tip_rate):
    tax = bill * 0.0825
    tip = bill * tip_rate
    total = bill+tip+tax
    return total

def calculate_total_3(bill, tip_rate=0.2):
    tax = bill * 0.0825
    tip = bill * tip_rate
    total = bill+tip+tax
    return total


bill = 158.29

total = calculate_total_1(bill)
print(f"total is {total:.2f}")

total = calculate_total_2(bill, 0.3)
print(f"total is {total:.2f}")

total = calculate_total_3(bill, 0.3)
print(f"total is {total:.2f}")

total = calculate_total_3(bill)
print(f"total is {total:.2f}")

total = calculate_total_3(tip_rate=0.1, bill=300.0)
print(f"total is {total:.2f}")