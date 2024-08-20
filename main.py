from pyscript import document

e_to_m = {
'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
'y':'-.--', 'z':'--..', ' ':' ', '1':'.----',
'2':'..---', '3':'...--', '4':'....-',
'5':'.....', '6':'-....', '7':'--...',
'8':'---..', '9':'----.', '0':'-----',
'.':'.-.-.-', ',':'--..--', '?':'..--..',
"'":".----.", '!':'-.-.--', '/':'-..-.',
'(':'-.--.', ')':'-.--.-', '&':'.-...',
':':'---...', ';':'-.-.-.', '=':'-...-',
'+':'.-.-.', '-':'-....-', '_':'..--.-',
'"':'.-..-.', '$':'...-..-', '@':'.--.-.',
' ':'[space]',
'End of Work':'...-.-', 'Error':'........',
'Start':'-.-.-' 
} 

m_to_e = {
'.-':'a', '-...':'b', '-.-.':'c', '-..':'d',
'.':'e', '..-.':'f', '--.':'g', '....':'h',
'..':'i', '.---':'j', '-.-':'k', '.-..':'l',
'--':'m', '-.':'n', '---':'o', '.--.':'p',
'--.-':'q', '.-.':'r', '...':'s', '-':'t',
'..-':'u', '...-':'v', '.--':'w', '-..-':'x',
'-.--':'y', '--..':'z', ' ':' ', '.----':'1',
'..---':'2', '...--':'3', '....-':'4',
'.....':'5', '-....':'6', '--...':'7',
'---..':'8', '----.':'9', '-----':'0',
'.-.-.-':'.', '--..--':',', '..--..':'?',
".----.":"'", '-.-.--':'!', '-..-.':'/',
'-.--.':'(', '-.--.-':')', '.-...':'&',
'---...':':', '-.-.-.':';', '-...-':'=',
'.-.-.':'+', '-....-':'-', '..--.-':'_',
'.-..-.':'"', '...-..-':'$', '.--.-.':'@',
' ':' ', '[space]':' ',
'...-.-':'End of Work', '........':'Error',
'-.-.-':'Start'
} 

def from_letters(event):
    """Translate letters to Morse"""
    morse_output_text = ""
    text_to_translate = document.querySelector("#input_str").value.lower()
    for letter in text_to_translate:
        morse_output_text += e_to_m.get(letter, '?') 
        morse_output_text += ' '
    document.querySelector("#output").innerText = morse_output_text


def from_morse(event):
    """Translate letters to Morse"""
    morse_output_text = ""
    morse_to_translate = document.querySelector("#input_str").value.split(' ')
    for letter in morse_to_translate:
        morse_output_text += m_to_e.get(letter, '?')
    #compensates for program adding extra "?" to end of english string:
    if morse_output_text[-1] == "?": 
        morse_output_text = morse_output_text[:-1]
    document.querySelector("#output").innerText = morse_output_text


def clear(event):
    """Clear textarea id=input_str"""
    document.querySelector("#input_str").value = ''
  
  