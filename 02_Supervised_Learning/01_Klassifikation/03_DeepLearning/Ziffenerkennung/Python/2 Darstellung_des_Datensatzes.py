import os

# Es wird ein HTML Dokument , also eine Webseite erstellt
html_code = ["<html<body>", "<h1>Dataset</h1>"]

# all files in directory images
files = os.listdir("bilder")

for file in files:
    # print(file)
    label = file[-5]
    html_code.append(f'<div style="display:inline-block; margin:5px;">')
    html_code.append(f'<img src="bilder/{file}" style="width:64px; height:64px;"><br>')
    html_code.append(f'Ziffer: {label}')
    html_code.append('</div>')
    html_code.append('\n')

html_code.append("")

f = open("datensatz.html", "w")
for line in html_code:
    f.write(line)
