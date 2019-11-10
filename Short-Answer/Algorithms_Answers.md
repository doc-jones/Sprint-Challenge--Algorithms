#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
# comment to commit
a)
a = 0  is a single operation = O(1)
while (a < n * n * n) is n^3 = O(n^3)
a = a + n * n     is n^2     = O(n^2)

In other cases we've looked at the bigger of values for Big O dominate, but in this case if you check n = [1, 2, 3, 10] because a is increasing by n^2 at the same time that while is n^3 the rate of growth is just n.


b)
sum = 0 is a single operation  = O(1)
for i in range(n)  loop thru n = O(n)
j = 1 is a single operation    = O(1)
while j < n  loop n times      = O̶(̶n̶)̶
j *= 2  j doubles on each loop = O(logn)
sum += 1  single operation     = O(1)

Nested loops = O(n * logn) = O(nlogn)


c)
def bunnyEars(bunnies):
if bunnies == 0: equals 0 once      = O(1) base case
return 0         one operation      = O(1)

return 2 + bunnyEars(bunnies-1)
loops one bunny at a time until 0   = 0(n)
Increases in bunnies will cause the call to bunnyEars to run bunnies-1 times until it hits zero, so the total runtime is O(n)

## Exercise II


