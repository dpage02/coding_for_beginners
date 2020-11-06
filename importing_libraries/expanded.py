# init 2 vars with floating-point values
item = .70
rate = 1.05

# attempt floating-point arithmetic with vars
tax = item * rate
total = item + tax

# display values
print('Item:\t', '%.20f' %item)
print('Tax:\t', '%.20f' %tax)
print('Total:\t', '%.20f' % total)