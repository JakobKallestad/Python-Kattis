n = int(input())
for _ in range(n):
    beats, seconds = map(float, input().split())
    bpm = (beats*60)/seconds
    abpm = 60/seconds
    print(bpm-abpm, bpm, bpm+abpm)