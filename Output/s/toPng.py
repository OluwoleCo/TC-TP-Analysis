from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

drawing = svg2rlg('drawss.svg')
renderPM.drawToFile(drawing, 'hahas.png')
