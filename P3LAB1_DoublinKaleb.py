red = int(input())
green = int(input())
blue = int(input())
gray = 0

if (red <= green) and (red <= blue):
    gray = red
    
if (green <= red) and (green <= blue):
    gray = green
    
if (blue <= green) and (blue<= red):
    gray = blue
    
red = red - gray
green = green - gray
blue = blue - gray

print(red, green, blue)
