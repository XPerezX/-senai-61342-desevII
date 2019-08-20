nums = []

for i in range(100):
    nums.append(i)



for k in nums:

    if (nums[k]%3 == 0  ):
        nums[k]="multiplo"
    r="3" in str(k)
    if r :
        nums[k]="tem 3"

    print (nums[k])


