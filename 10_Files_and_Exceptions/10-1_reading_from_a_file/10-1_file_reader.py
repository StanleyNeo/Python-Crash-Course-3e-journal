# 10-1_reading_from_a_file 20250619 Stanley Neo

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()  # remove blank line strips, any whitespace characters
for line in lines:
    print(line)


