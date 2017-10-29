import svgwrite

dwg = svgwrite.Drawing('test.svg', profile='tiny')
dwg.add(dwg.line((0, 0), (1000, 0), stroke=svgwrite.rgb(255, 0, 0, '%')))
dwg.add(dwg.rect(insert=(1000, 0), size=(100, 100), rx=None, ry=None, fill='red'))
dwg.add(dwg.rect(insert=(1005, 5), size=(90, 90), rx=None, ry=None, fill='white'))
dwg.add(dwg.circle(center=(0, 150), r=90, fill='blue'))
dwg.add(dwg.circle(center=(0, 150), r=80, fill='white'))
dwg.save()