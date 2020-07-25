""" helper for final assignment: Generate PDF"""

# code is based on provided code from the week 3 assignment for the final course

from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(file, title, add_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(add_info, styles['BodyText'])
    empty_line = Spacer(1, 20)

    report.build([report_title, empty_line, report_info, empty_line])
