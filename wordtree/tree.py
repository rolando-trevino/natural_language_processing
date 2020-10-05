import io

def write_tree(sentences, word, format_ = 'implicit'):
    f = open("demo_tree.html", "w")

    f.write('<html>\n')
    f.write('<head>\n')
    f.write('\t<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n')
    f.write('\t<script type="text/javascript">\n')
    f.write('\tgoogle.charts.load(\'current\', {packages:[\'wordtree\']});\n')
    f.write('\tgoogle.charts.setOnLoadCallback(drawChart);\n')
    f.write('\n')
    f.write('\tfunction drawChart() {\n')
    f.write('\t\tvar data = google.visualization.arrayToDataTable(\n')
    f.write('\t\t[ \n')
    f.write('\t\t[\'Phrases\'],\n')
    for sentence in sentences:
        f.write(f'\t\t[\'{sentence}\'],\n')
    f.write('\t\t]\n')
    f.write('\t\t);\n')
    f.write('\n')
    f.write('\t\tvar options = {\n')
    f.write('\t\twordtree: {\n')
    f.write(f'\t\t\tformat: \'{format_}\',\n')
    f.write(f'\t\t\tword: \'{word}\'\n')
    f.write('\t\t}\n')
    f.write('\t\t};\n')
    f.write('\n')
    f.write('\t\tvar chart = new google.visualization.WordTree(document.getElementById(\'wordtree_basic\'));\n')
    f.write('\t\tchart.draw(data, options);\n')
    f.write('\t}\n')
    f.write('\t</script>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('\t<div id="wordtree_basic" style="width: 900px; height: 500px;"></div>\n')
    f.write('</body>\n')
    f.write('</html>\n')

    f.close()

arbol = ['hola soy pablo gomez','hola soy rolando', 'hola soy pablo gonalze']

write_tree(arbol, 'hola')

