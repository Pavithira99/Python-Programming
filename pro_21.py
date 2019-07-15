pp = int(input())
qq = list(map(int, input().split()))
r = int(len(qq)/2)
if sum(qq[:r])//len(qq[:r]) == sum(qq[r:])//len(qq[r:]):
    print('yes')
else:
    print('no')
