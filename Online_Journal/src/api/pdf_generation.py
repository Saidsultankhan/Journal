from rest_framework import views
from src.apps.jounal.models import DairyOfClass
from django.http import HttpResponse
from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Frame
)


class PDFGeneratorView(views.APIView):

    def get(self, request):
        filename = 'marks.pdf'
        buffer = BytesIO()
        
        pdf = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']

        database = [["Name", "Grade", "Subject", 'Quarter', 'mark']]
        pupils_data = DairyOfClass.objects.filter(pupil__user=request.user).prefetch_related('pupil', 'subject', 'grade')
        user = request.user.pupil_user.values().first()['name_uz']

        for i in pupils_data:
            database.append(
                [
                    f"{user}", 
                    f"{str(i.grade)}",
                    f"{str(i.subject)}",
                    f"{i.quarter}",
                    f"{i.mark}",
                ]
            )

        # for dairy_data in obj.dairy_pupil.values():
                    #     print(dairy_data['mark'])
                    # print(obj.dairy_pupil.values())
        header_text = f'Butun yil davomida olingan {user}-ning baholari.'
        header_frame = Frame(pdf.width - 200, pdf.height - 50, 200, 50, showBoundary=0)

        table = Table(database)
        style = TableStyle(
                            [
                                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                            ]
                        )

        table.setStyle(style)

        elements = []

        header_content = Paragraph(header_text, header_style)
        elements.append(header_content)
        elements.append(table)
        header_frame.addFromList([header_content], pdf)
        pdf.build(elements)

        pdf_data = buffer.getvalue()
        buffer.close()

        # return HttpResponse()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        response.write(pdf_data)

        return response