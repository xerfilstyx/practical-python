# report.py
#
# Exercise 1.2

bill_thickness = 0.11 * 0.001   # 지폐의 두께(0.11mm)를 미터로 환산
sears_height = 442  # 시어스 타워의 높이(미터)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills *= 2

print('Number of days:', day)
print('Number of bills:', num_bills)
print('Final height:', num_bills * bill_thickness)