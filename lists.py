my_linear_list = []
my_sliding_window_list = []

i = 0
i_end = 10
while i < i_end:
    i += 1
    my_linear_list.append(i)
    my_sliding_window_list.append(1)

for index, value in enumerate(my_linear_list):
    print(f'index: {index} value: {value}')


#two pointers
print('\n\nTWO POINTER----------------\n')
left = 0
right = len(my_linear_list) - 1

print('begin while')
i = 0
while left < right:
    i += 0
    print(f'{i} first: left {left} right {right}')
    left += 1
    right -= 1
    print(f'{i} then: left {left} right {right}')

# sliding window
print('\n\nSLIDING WINDOW----------------\n')

print('\nwindow setup')

w = 4 # window length

# version 1
# the leetcode standard

left = right = sum_val = 0
i = 0 #iteration count

while right < w:
    i += 1
    print(f'{i} first   {right} sum_val: {sum_val} right: {right}')
    sum_val += my_sliding_window_list[right]
    right += 1
    print(f'{i} then    {right} sum_val: {sum_val} right: {right}')

print('\nwindow runs')

while right < len(my_sliding_window_list):
    i+= 1
    print(f'{i} first   {right} sum_val: {sum_val} right: {right} left: {left}')
    sum_val += my_sliding_window_list[right]
    sum_val -= my_sliding_window_list[left]
    right += 1
    left += 1
    print(f'{i} then    {right} sum_val: {sum_val} right: {right} left: {left}')

# version 2 
# is apparently bad for branch prediction?

left = right = sum_val = 0
while right < len(my_sliding_window_list):
    if right < w:
        sum_val += my_sliding_window_list[right]
        right += 1
    else:
        sum_val += my_sliding_window_list[right]
        sum_val -= my_sliding_window_list[left]
        left += 1
        right += 1

# version 3 slicing to setup sum_val
right = sum_val = 0
sum_val = sum(my_sliding_window_list[:w])

for right in range(w, len(my_sliding_window_list)):
    sum_val += my_sliding_window_list[right] - my_sliding_window_list[right - w]
    
if sum_val == w:
    print('\nSUCCESS: sum_val of sliding window is w')
else: print('\nERROR: sum_val of sliding window is not w')