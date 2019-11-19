country = int(input("Enter 1 or 2 to choose a country \n 1. USA \n 2. Australia \n "))
tax_id = input("Enter Your Tax ID : \n ")
salary = float(input("Please enter Your salary in numbers: \n"))
tax = 0.0


def USA(salary):
    if salary < 9276:
        tax = salary * 0.1
        return tax
    elif salary > 9275 and salary < 37651:
        tax = salary * 0.15
        return tax
    elif salary > 37650 and salary < 91151:
        tax = salary * 0.25
        return tax
    elif salary > 91150 and salary < 190151:
        tax = salary * 0.28
        return tax
    elif salary > 190150 and salary < 413351:
        tax = salary * 0.33
        return tax
    elif salary > 413350 and salary < 415051:
        tax = salary * 0.35
        return tax
    elif salary >1415050:
        tax = salary * 0.396
        return tax
    else:
        print("Out of Bound.Not currently Supported")


def Australia(salary):
    if salary < 18201:
        tax = 0
        return tax
    elif salary > 18200 and salary < 37001:
        tax = salary * 0.19
        return tax
    elif salary > 37000 and salary < 80001:
        tax = salary * 0.325
        return tax
    elif salary > 80000 and salary < 180001:
        tax = salary * 0.37
        return tax
    elif salary < 180000:
        tax = salary * 0.45
        return tax
    else:
        print("Out of Bound.Not currently Supported")


if country == 1:
    tax = USA(salary)
    print("{} from your ${} salary your tax is {}".format(tax_id, salary, round(tax,2)))
elif country == 2:
    tax = Australia(salary)
    print("{} from your ${} salary your tax is {}".format(tax_id, salary, round(tax,2)))
else:
    print("{} Please enter a valid responce".format(tax_id))
    
