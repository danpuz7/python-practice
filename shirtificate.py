from fpdf import FPDF

pdf = FPDF()

img_path = "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png"
img_width = 100
pdf_width = pdf.w - 2 * pdf.l_margin
x_position = (pdf_width - img_width) / 2
def add_title(pdf, title_text): 
    pdf.set_font("helvetica", style="B", size=36)
    title_width = pdf.get_string_width(title_text)
    title_x_position = (pdf_width - title_width) / 2
    pdf.set_xy(title_x_position, pdf.get_y())
    pdf.cell(title_width, 10, title_text, align="C")

def add_image(pdf, img_path, x_position, img_width):
    pdf.set_y(pdf.get_y() + 30)
    pdf.image(img_path, x=x_position, y=pdf.get_y(), w= img_width)
    

def add_subtitle(pdf, subtitle_text):
    pdf.set_y(pdf.get_y() + 30)
    pdf.set_font("times", size=15)
    subtitle_width = pdf.get_string_width(subtitle_text)
    subtitle_x_position = (pdf_width - subtitle_width) / 2
    pdf.set_xy(subtitle_x_position, pdf.get_y())
    pdf.set_text_color(255, 255, 255)
    pdf.cell(subtitle_width, 10, subtitle_text, align="C")


pdf.add_page()

add_title(pdf, "CS50 Shirtificate")

add_image(pdf, img_path, x_position, img_width)

add_subtitle(pdf, "Dan took CS50")

pdf.output("tuto1.pdf")
