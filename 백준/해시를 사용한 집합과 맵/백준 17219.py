n, m = map(int, input().split())

site_pw = {}

for _ in range(n):
    site, pw = input().split()
    site_pw[site] = pw

for _ in range(m):
    print(site_pw[input()])