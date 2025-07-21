# filepath: pdf_comparator/create_sample_pdf.py
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, """Proposal of Insurance
Date Quoted: [07/01/2023]
Prepared For: Presented By:
[Rajendra Babu]
[Rajendra]
Dear [Rajendra]
I am pleased to present you with a proposal of coverage designed to meet the individual needs of your 
business. This proposal letter summarizes the coverages, limits and premiums associated with the policy 
that you are considering.""")
pdf.output("pdf_comparator/sample.pdf")