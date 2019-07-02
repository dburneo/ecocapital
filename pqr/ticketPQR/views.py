from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import io
import textwrap
from django.http import HttpResponse, FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image

import json, urllib.request
import requests

from django.conf.urls.static import static

with urllib.request.urlopen("https://xinternet.co/j/entrada.json") as url:
    data = json.loads(url.read().decode())

class TicketPQR(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ticketpqr.pdf"'

        def textSplit(x, y, txt, lenTxt, p):
            txt1 = textwrap.wrap(txt, lenTxt)
            for t in txt1:
                p.drawString(x, y, t)
                y -= 12

        p = canvas.Canvas(response)

        # p.drawImage("https://xinternet.co/axios/ecocapital/pqr_fondo.png", 55, 468, width=505, height=319)
        p.drawImage("pqr/ticketPQR/static/ticketPQR/pqr_fondo.png", 55, 468, width=505, height=319)
        p.setFont('Helvetica', 10)
        p.drawString(115, 708, data['date']['Value'])
        p.setFont('Helvetica-Bold', 14.5)
        p.drawString(492, 705, data['ticket_id']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(162, 690, data['claimant_name']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(122, 677, data['claimant_id']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(265, 677, data['phone']['Value'])
        p.setFont('Helvetica', 8)
        p.drawString(381, 677, data['email']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(108, 658, data['code']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(316, 658, data['subscription_id']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(426, 664, data['category']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(129, 638, data['client_name']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(436, 638, data['client_id']['Value'])
        p.setFont('Helvetica', 10)
        # p.drawString(146, 625, data['address_1']['Value'])

        textSplit(146, 625, data['address_1']['Value'], 15, p)

        p.setFont('Helvetica', 10)
        # p.drawString(296, 625, data['city_division']['Value'])

        textSplit(296, 625, data['city_division']['Value'], 12, p)

        p.setFont('Helvetica', 10)
        # p.drawString(461, 625, data['address_2']['Value'])

        textSplit(461, 625, data['address_2']['Value'], 17, p)

        p.setFont('Helvetica', 10)
        p.drawString(195, 600, data['channel']['Value'])
        p.setFont('Helvetica', 10)
        p.drawString(312, 600, data['concept']['Value'])
        p.setFont('Helvetica', 10)
        # p.drawString(120, 587, data['description']['Value'])

        textSplit(120, 587, data['description']['Value'], 70, p)

        p.setFont('Helvetica', 10)
        # p.drawString(120, 562, data['answer']['Value'])

        textSplit(120, 562, data['answer']['Value'], 93, p)

        p.setFont('Helvetica', 10)
        p.drawString(147, 492, data['signature_1']['Value'])

        p.showPage()
        p.save()
        
        return response

    # def get(self, request):
    #     content = {'Message': 'Hello Developer'}
    #     return Response(content)
