def distinct_year(year):
    year += 1
    while len(set(str(year))) < 4:
        year += 1
    return year


y = int(input())
result = distinct_year(y)
print(result)