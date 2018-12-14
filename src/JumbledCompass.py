start = int(input())
end = int(input())
counter_clockwise = (start+360-end)%360
clockwise = (360-start+end)%360
print(clockwise) if clockwise <= counter_clockwise else print(-counter_clockwise)
