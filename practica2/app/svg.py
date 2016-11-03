import random

def rectangulo():
    x = random.randint(0, 500)
    y = random.randint(0, 500)

    h = random.randint(0, 200)
    w = random.randint(0, 200)
    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())
    
    return '<rect x="%s" y="%s" width="%s" height="%s" style="fill:%s" />' % (x, y, h,w, color)

def elipse():
    x = random.randint(0, 500)
    y = random.randint(0, 500)

    a = random.randint(0, 200)
    b = random.randint(0, 200)

    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())

    color_line = '#%02X%02X%02X' % (r(),r(),r())

    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" style="fill:%s;stroke:%s;stroke-width:2" />' % (x,y,a,b, color, color_line)


    return '<rect x="%s" y="%s" width="%s" height="%s" style="fill:%s" />' % (x, y, h,w, color)
def random_svg():
    svg = """<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">"""
    figuras=[rectangulo,elipse]
    svg += figuras[random.randint(0,1)]()
    svg += "</svg>"
    with open("./static/random_svg.svg", "w") as f:
        f.write(svg)


if __name__ == "__main__":
    with open("/static/random_svg.svg", "w") as f:
        f.write(random_svg())
