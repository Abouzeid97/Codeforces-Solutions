s1, s2, s3, s4 = map(int, input().split())

unique_colors = len(set([s1, s2, s3, s4]))
minimum_horseshoes_to_buy = 4 - unique_colors

print(minimum_horseshoes_to_buy)