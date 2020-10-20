h, w, n, m = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(h)]
kernel = [list(map(int, input().split()))[::-1] for _ in range(n)][::-1]
kernel_flattened = []
for row in kernel:
    kernel_flattened += row
result_image = []

for i in range(h):
    row = []
    for j in range(w):
        flattened = []
        for sub_row in image[i:i+n]:
            for num in sub_row[j:j+m]:
                flattened.append(num)
        if len(flattened) == len(kernel_flattened):
            row.append(sum(a*b for a, b in zip(flattened, kernel_flattened)))
    result_image.append(row)

for row in result_image:
    print(*row)
