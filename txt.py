from fpdf import FPDF
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial" , size=12)
pdf.cell(200,180,txt="CallCenter Ticket Create", ln=2, align="C")
pdf.output("/Users/imge.yazici/Desktop/CallCenterTicketCreate.pdf")