import pdfkit
import jinja2
from datetime import datetime
dato = {}
dato["titulo"]="Meeee"
dato["nombre"]= "Kendryd Rodriguez"
dato["tiempo"]= datetime.now().date().strftime("%d, %b, %y")
print(dato)

contex = {'dato': dato}

ken_loader = jinja2.FileSystemLoader('../Prueba_json')
ken_ambiente = jinja2.Environment(loader=ken_loader)
plantilla_html = 'practica.html'
ambiente = ken_ambiente.get_template(plantilla_html)
poner = ambiente.render(contex)

path_pdf = b'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
confi = pdfkit.configuration(wkhtmltopdf = path_pdf)
output_pdf = 'me.pdf'
pdfkit.from_string(poner, output_pdf, configuration=confi)
