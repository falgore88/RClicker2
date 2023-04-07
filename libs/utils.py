from ctypes import windll

hdc = windll.user32.GetDC(0)


def get_pixel_color(x, y):
    rgb = windll.gdi32.GetPixel(hdc, x, y)
    r = rgb & 0xff
    g = (rgb >> 8) & 0xff
    b = (rgb >> 16) & 0xff
    return "#%02x%02x%02x" % (r, g, b)
