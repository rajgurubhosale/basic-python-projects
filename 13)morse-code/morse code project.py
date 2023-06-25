from morseCodeData import morse_code_map

#chnge g value later in dict of morse code


code_list=[ ]
def morseCodeGenrator(text):
    for i in text:
        if i in morse_code_map:
            code_list.append(morse_code_map[i])
        if i.isalpha()==True:
            if i.isupper()==False:
                i=i.upper()
                code_list.append(morse_code_map[i])


    return " ".join(code_list)



temp_list=[]
def morseItrepreter(text):
    morse_keys=list(morse_code_map.keys())  #list of all keys in dict
    morse_values=list(morse_code_map.values())   #list of all values in dict
    temp=text.split()    # to create a list of morse code from given text
    for i in temp:
        idx=morse_values.index(i)    #index of temp element in values list
        ele=morse_keys[idx]          #for key which is present at idx in key list
        temp_list.append(ele)
    return "".join(temp_list)


print("welcome to morse code project".title())
choice=int(input('''
1-Morse code Genrator
2-Code Intrepretor
'''))
if choice==1:
    test=input("enter text to genrate morse code: ".title())
    code=morseCodeGenrator(test)
    print(f"Morse Code: {code}")
if choice==2:
    test=input("enter a morse code to interpretate it: ".title())
    code=morseItrepreter(test)
    print(f"Interpretated Message:{code}")
