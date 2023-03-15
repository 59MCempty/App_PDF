from fpdf import FPDF
import pandas


# P for Portrait, L B for Landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pandas.read_csv("topics.csv")

"""
h: height of cell
ln: break line 
if ln=0 --> next cell will be added after tail of this cell
border: create square

# set cell:
pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=1)
pdf.set_font(family="Times", style="I", size=10)
pdf.cell(w=0, h=12, txt="Hi There!", align="L", ln=1, border=0)
"""

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)  # gray color
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    # pdf.line(x1, x2, y1, y2)
    # x1, y1: coordinates of starting point of line
    # value of x1: from left border to starting point
    # x2, y2: coordinates of the end point of line
    # value of x2: distance from starting point to the end point
    pdf.line(12, 21, 200, 21)

    # add more pages follow topic.csv
    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")