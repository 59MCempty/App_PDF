from fpdf import FPDF

# P for Portrait, L B for Landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

# set cell:
"""
h: height of cell
ln: break line 
if ln=0 --> next cell will be added after tail of this cell
border: create square
"""
pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=1)
pdf.set_font(family="Times", style="I", size=10)
pdf.cell(w=0, h=12, txt="Hi There!", align="L", ln=1, border=0)

pdf.output("output.pdf")