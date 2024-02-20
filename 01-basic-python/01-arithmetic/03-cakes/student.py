# Write your code here
def cakes(eggs,butter, flour):
    cake_eggs= eggs//5
    cake_butter = butter // 250
    cake_flour = flour // 250
    return min(cake_butter,cake_eggs,cake_flour)