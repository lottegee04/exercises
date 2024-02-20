# Write your code here
def format_time(hours, minutes, seconds):
    return f"{hours:0>2d}:{minutes:0>2d}:{seconds:0>2d}"

print(format_time(4,5,6))