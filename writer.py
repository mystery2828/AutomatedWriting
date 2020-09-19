import random
import os

letter_color = "black"
letter_set = "set2"
trcolor = False
totalset = len(os.listdir("images/letters")) + 1


htmlc = [
    "<html><head><style>.lines{width:100%;height:auto;float:left;}#paper{background:white;height:auto;float:left;padding:20px 20px;width:90%;}img,span{height:20px;width:15px;float:left;margin-top:5px;margin-bottom:5px;}.clblack{filter:brightness(50%);}.clblue{filter:brightness(100%);}</style></head><body><div id='paper'>"
]

with open("content1.txt", "r") as textfile:
    
    for lines in textfile:
        # print(lines)
        # Strips the newline character
        curst = lines.strip()
        htmlc.append('<div class="lines">')
        # print(curst)
        print(curst)
        for ch in curst:
            # get char ASCII Code of char
            # print(ch)
            chcode = ord(ch)
            
            if chcode == 32:
                htmlc.append("<span></span>")

            elif chcode != 32:
                    htmlc.append(
                        "<img src='D:\\Desktop\\MyHandWriting\\images\\letters\\set2\\black\\{}.jpg'/>".format(chcode)
                    )

        htmlc.append("</div>")
        # htmlc.append("</br>")

htmlc.append("</div></body></html>")

with open("page1.html", "w") as page_html:
    page_html.writelines(htmlc)
