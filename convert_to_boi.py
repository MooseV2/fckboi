from itertools import islice
commands = '><+-.,[]'
bf_code = input('-- Enter your Brainfuck code: ')
output_code = []
for character in bf_code:
	if character in commands:
		output_code.append(commands.index(character)+1)

# output_code = output_code[::-1]

partitions = []
for code in range(len(output_code)//10+1):
	partitions.append(''.join(str(x) for x in output_code[10*code:10*code+10]))
print('-- Your resulting boilang code (paste this in the bottom of the file):')
print('-- START OF PROGRAM --')
for item in partitions:
	print(f'boi! addcode [int {item[::-1]}] [int {len(item)}] boi')
print('-- END OF PROGRAM --')


