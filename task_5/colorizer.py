def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i: i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return "#%02x%02x%02x" % rgb_color


def lighten(start_hex, end_hex, count, num):
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)

    r = int(start_rgb[0] + ((end_rgb[0] - start_rgb[0]) / count * num))
    g = int(start_rgb[1] + ((end_rgb[1] - start_rgb[1]) / count * num))
    b = int(start_rgb[2] + ((end_rgb[2] - start_rgb[2]) / count * num))

    rgb = rgb_to_hex((r, g, b))
    return rgb
