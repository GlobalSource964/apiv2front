from datetime import datetime
import os
import requests
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
import logging
from django.views.decorators.cache import cache_page

logger = logging.getLogger(__name__)


def format_domain(domain):
    domain = domain.replace('www.', '').replace('.online', '')
    if 'escorts' in domain:
        domain = domain.replace('escorts', ' Escort')
    elif 'escrots' in domain:
        domain = domain.replace('escrots', ' Escort')
    elif 'escros' in domain:
        domain = domain.replace('escros', ' Escort')
    else:
        domain = domain.replace('escort', ' Escort')
    domain = domain.replace('.', ' ')
    return domain.title()


def get_api_url(request):
    original_domain = request.META['HTTP_HOST']
    if original_domain == '172.29.153.241':
        return 'http://172.29.153.240/api/v2/ilanlar'
    else:
        return 'https://apiv2.ayasescorts.online/api/v2/ilanlar'

@cache_page(60 * 30)
def amp(request):
    original_domain = request.META['HTTP_HOST']
    domain = request.META['HTTP_HOST']
    domain = domain.replace('www.', '')
    whatsapp_number = '+447537129402'
    print(original_domain)
    url = get_api_url(request)

    # Format the domain to a readable title.
    formatted_domain = format_domain(original_domain)
    response = requests.get(url, params={'domain': domain})
    if response.status_code == 200:
        try:
            data = response.json()
            desired_domain = request.META['HTTP_HOST']
            blogs = []  # initialize blogs as an empty list

            for item in data:
                domain_data_list = item.get('domain', [])  # Get domain data list, return empty list if not exist
                for domain_data in domain_data_list:
                    if desired_domain in domain_data.values():  # Check if the desired domain is in the domain_data dictionary
                        blogs = domain_data.get('blogs', [])  # If the domain is the desired domain, get blog data
        except ValueError:  # includes simplejson.decoder.JSONDecodeError eror verir
            print('Decoding JSON has failed')
            data = []
            blogs = []
    else:
        print(f"API Request failed with status code {response.status_code}")
        data = []
        blogs = []

    response = requests.get('https://apiv2.ayasescorts.online/api/v2/domainbacklink')
    backlinks = response.json()

    ust = []
    orta = []
    alt = []
    for item in data:
        resim = item.get('resimler', [{}])[0].get('resim_url', '') if item.get('resimler', []) else ''
        original_telefon = item.get('telefon', '')
        telefon = format_phone_number(original_telefon)
        meta_title = item.get('meta_title', '')
        meta_description = item.get('meta_description', '')
        paket = item.get('paket', [])
        if paket:
            paket_pozisyon = paket[0].get('pozisyon', '')
            if paket_pozisyon == 'ust':
                ust.append(
                    {'resim': resim, 'telefon': telefon, 'original_telefon': original_telefon, 'meta_title': meta_title,
                     'meta_description': meta_description})
            elif paket_pozisyon == 'orta':
                orta.append(
                    {'resim': resim, 'telefon': telefon, 'original_telefon': original_telefon, 'meta_title': meta_title,
                     'meta_description': meta_description})
            elif paket_pozisyon == 'alt':
                alt.append(
                    {'resim': resim, 'telefon': telefon, 'original_telefon': original_telefon, 'meta_title': meta_title,
                     'meta_description': meta_description})

    return render(request, 'phonem.html',
                  {'ust': ust, 'orta': orta, 'alt': alt, 'title': formatted_domain, 'whatsapp': whatsapp_number,
                   'blogs': blogs, 'original_domain': original_domain, 'backlinks': backlinks})

@cache_page(60 * 30)
def index(request):
    original_domain = request.META['HTTP_HOST']
    domain = request.META['HTTP_HOST']
    domain = domain.replace('www.', '')
    whatsapp_number = '+447537129402'
    print(original_domain)
    url = get_api_url(request)

    # Format the domain to a readable title.
    formatted_domain = format_domain(original_domain)
    response = requests.get(url, params={'domain': domain})
    if response.status_code == 200:
        try:
            data = response.json()
            desired_domain = request.META['HTTP_HOST']
            blogs = []  # initialize blogs as an empty list

            for item in data:
                domain_data_list = item.get('domain', [])  # Get domain data list, return empty list if not exist
                for domain_data in domain_data_list:
                    if desired_domain in domain_data.values():  # Check if the desired domain is in the domain_data dictionary
                        blogs = domain_data.get('blogs', [])  # If the domain is the desired domain, get blog data
        except ValueError:  # includes simplejson.decoder.JSONDecodeError eror verir
            print('Decoding JSON has failed')
            data = []
            blogs = []
    else:
        print(f"API Request failed with status code {response.status_code}")
        data = []
        blogs = []

    response = requests.get('https://apiv2.ayasescorts.online/api/v2/domainbacklink')
    backlinks = response.json()

    ust = []
    orta = []
    alt = []
    for item in data:
        resim = item.get('resimler', [{}])[0].get('resim_url', '') if item.get('resimler', []) else ''
        original_telefon = item.get('telefon', '')
        telefon = format_phone_number(original_telefon)
        meta_title = item.get('meta_title', '')
        meta_description = item.get('meta_description', '')
        paket = item.get('paket', [])
        if paket:
            paket_pozisyon = paket[0].get('pozisyon', '')
            if paket_pozisyon == 'ust':
                ust.append({'resim': resim, 'telefon': telefon, 'original_telefon': original_telefon, 'meta_title':meta_title, 'meta_description': meta_description})
            elif paket_pozisyon == 'orta':
                orta.append({'resim': resim, 'telefon': telefon, 'original_telefon': original_telefon, 'meta_title':meta_title, 'meta_description': meta_description})
            elif paket_pozisyon == 'alt':
                alt.append({'resim': resim, 'telefon': telefon, 'original_telefon': original_telefon, 'meta_title':meta_title, 'meta_description': meta_description})

    return render(request, 'index.html', {'ust': ust, 'orta': orta, 'alt': alt, 'title': formatted_domain, 'whatsapp': whatsapp_number, 'blogs': blogs, 'original_domain':original_domain, 'backlinks': backlinks})


def format_phone_number(num):
    clean_num = str(num)[2:]  # Convert to string and remove the first two digits ('90')
    formatted_num = "0 ({}) {} {}".format(clean_num[:3], clean_num[3:6], clean_num[6:])
    return formatted_num



def sitemap(request):
    my_url = request.META['HTTP_HOST']
    last_mod_date = datetime.now().isoformat()

    # f-string kullanarak XML oluşturuyoruz.
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
                    http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
        <url>
          <loc>https://{my_url}</loc>
            <lastmod>2023-06-20T13:28:56+00:00</lastmod>
        </url>
        <url>
          <loc>https://{my_url}/amp</loc>
            <lastmod>2023-06-20T13:28:56+00:00</lastmod>
        </url>
        </urlset>"""
    return HttpResponse(xml, content_type='application/xml')

def redirect_to_amp(request):
    return redirect("/amp")