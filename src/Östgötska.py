word_list = input().split()
count = 0
for word in word_list:
    if "ae" in word:
        count += 1

if count/len(word_list) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
