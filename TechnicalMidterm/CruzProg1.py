def palindrome(num):
    return str(num) == str(num)[::-1]

def fileNumberstxt_open(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")

    except Exception as e:
        print(f"Error: {e}")

fileNumberstxt_open("TechnicalMidterm/numbers.txt")




