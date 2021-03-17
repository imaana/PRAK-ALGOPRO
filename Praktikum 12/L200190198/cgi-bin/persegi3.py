def hitung_luas():
    """fungsi menghitung luas dari persegi"""
    sisi = 4
    luas = sisi*sisi
    return luas

print("<!DOCTYPE html>\n")
print("""<html>
<head>
<title>Bangun Geometri</title></body>\n""")

print("<h1>Bangun Geometri</h1>")
print("<table>")
print("""<tr>
<td>Nama Bangun</td>
<td>:</td>
<td>Persegi</td></tr>
<tr>
<td>Dimensi(2D/3D)</td>
<td>:</td>
<td>2 Dimensi</td></tr>
<tr>
<td>Rumus Luas</td>
<td>:</td>
<td>sisi x sisi</td></tr>
<tr>
<td>Parameter 1(sisi)</td>
<td>:</td>
<td>4</td></tr>
<tr>
<td>Luas</td>
<td>:</td>
<td>""")
print(hitung_luas())
print("""</td></tr></table></body></html>""")
