# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:00:59 2020

@author: Sharmila Siram
"""
import wolframalpha
client = wolframalpha.Client("WXQ48V-TY6K637297")

import wikipedia
import PySimpleGUI as sg

sg.theme('DarkTeal')	
layout = [  [sg.Text('Enter a command:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Assistant', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    wolf_possible = None
    wiki_possible = None
    
    ##if wolfram search is successful or not
    try:
        res = res = client.query(values[0])
        wolfram_res = next(res.results).text
    except:
        wolf_possible = "No"
    ## if wiki search is possible or not.
    try:
        wiki_res = wikipedia.summary(values[0])
    except:
        wiki_possible = "No"
    
    #pops up the result(s)    
    if wolf_possible is None and wiki_possible is None:
        sg.Popup("wolfram result: " + wolfram_res, "Wikipedia Result: " + wiki_res)
    elif wolf_possible is None:
        sg.Popup("wolfram result: " + wolfram_res)
    elif wiki_possible is None:
        sg.Popup("wikipedia result: " + wiki_res)
    else:
        sg.Popup('no results')
        
window.close()

