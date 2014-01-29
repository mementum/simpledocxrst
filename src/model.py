#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
################################################################################
# 
#   Copyright (C) 2014 Daniel Rodriguez
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
import docx

def GetDocument(filename):
    try:
        document = docx.opendocx(filename)
    except IOError, e:
        return False, e

    # Fetch all the text out of the document we just created
    paratextlist = GetDocumentText(document)

    # Make explicit unicode version
    newparatextlist = list()
    for paratext in paratextlist:
        newparatextlist.append(paratext.encode("utf-8"))

    return True, '\n\n'.join(newparatextlist)


headings = {'1': '=', '2': '-', '3': '.', '4': '^', '5': '"', '6': ':', '7': '_'}
indents = [700, 1000, 1300, 999999]

def norm_name_w(tag):
    return '{' + docx.nsprefixes['w'] + '}' + tag

ns_paragraph = norm_name_w('p')
ns_table = norm_name_w('tbl')
ns_text = norm_name_w('t')
ns_tab = norm_name_w('tab')
ns_indent = norm_name_w('ind')
ns_br = norm_name_w('br')

ns_val = norm_name_w('val')
ns_left = norm_name_w('left')
ns_pstyle = norm_name_w('pStyle')
ns_ilvl = norm_name_w('ilvl')

def GetDocumentText(document):
    '''Return the raw text of a document, as a list of paragraphs.'''
    paragraphs = list()

    try:
        body = document.xpath('/w:document/w:body', namespaces=docx.nsprefixes)[0]
    except Exception, e:
        print 'Exception', e
    else:
        getbodyparagraphs(body, paragraphs)

    return paragraphs

def getbodyparagraphs(parent, outlist):
    for child in parent:
        tag = child.tag

        if tag == ns_paragraph:
            paratext = parseparagraph(child)
            if paratext:
                outlist.append(paratext)
        elif tag == ns_table:
            pass
        else: # image, toc, caption, title ?
            pass

def parseparagraph(paragraph):
    # Loop through each paragraph
    paratext = u''
    pStyle, heading, listpara, ilvl, pindent = None, None, None, 0, 0

    for element in paragraph.iter():
        # Find t (text) elements
        tag = element.tag
        if tag == ns_text:
            if element.text:
                paratext += element.text
        elif tag == ns_tab:
            paratext += '\t'
        elif tag == ns_br:
            paratext += '\n\n'

        elif tag == ns_ilvl:
            ilvl = element.get(ns_val)
        elif tag == ns_indent:
            pindent = element.get(ns_left)
            pindent = int(pindent) if pindent else 0
            if pindent < 700:
                pindent = 0
            elif pindent < 1000:
                pindent = 1
            elif pindent < 1300:
                pindent = 2
            else:
                pindent = 3
        elif tag == ns_pstyle:
            valattr = element.get(ns_val)
            if valattr.startswith('Heading'):
                heading = headings[valattr[-1]]
            elif valattr.startswith('ListParagraph'):
                listpara = True
            else:
                pStyle = 'unknown'

    if pStyle is 'unknown':
        return ''
    if heading:
        paratext += '\n' + heading * len(paratext)
    if listpara:
        ilvl_space = ' ' * (3 * (int(ilvl) + 1))
        paratext = ilvl_space + '- ' + paratext
    if pindent and not heading:
        indent_space = ' ' * (3 * pindent)
        paratext = indent_space + paratext

    # Add our completed paragraph text to the list of paragraph text
    return paratext
