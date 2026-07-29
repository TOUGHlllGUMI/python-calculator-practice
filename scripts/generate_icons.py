from PIL import Image, ImageDraw, ImageFont


def make_icon(size, path):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    top = (58, 42, 110)
    bottom = (110, 42, 94)
    for y in range(size):
        t = y / size
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    radius = int(size * 0.22)
    mask_draw.rounded_rectangle([(0, 0), (size - 1, size - 1)], radius=radius, fill=255)
    rounded = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    rounded.paste(img, (0, 0), mask)
    draw = ImageDraw.Draw(rounded)

    bar_w = int(size * 0.5)
    bar_h = int(size * 0.09)
    bar_gap = int(size * 0.08)
    cx = size // 2
    cy = size // 2
    bar_radius = bar_h // 2

    for offset in (-bar_gap, bar_gap):
        y = cy + offset
        draw.rounded_rectangle(
            [(cx - bar_w // 2, y - bar_h // 2), (cx + bar_w // 2, y + bar_h // 2)],
            radius=bar_radius,
            fill=(240, 238, 252, 255),
        )

    rounded.save(path)


make_icon(192, "icons/icon-192.png")
make_icon(512, "icons/icon-512.png")
print("done")
