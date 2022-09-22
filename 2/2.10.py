nums = input()
s = ""

for i in range(len(nums)):
  sim = nums[i]
  if sim.isdigit() == True:
    s += nums[i]

print("+" + s)