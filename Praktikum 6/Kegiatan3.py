Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama="Afifah Ghaisani Imana"
>>> NIM="L200190198"
>>> X="1"+NIM[7:]
>>> a=int(X)
>>> b=len(Nama)
>>> type(a)
<class 'int'>
>>> #karena data pada variabel X sudah dirubah dari tipe sting menjadi integer
>>> a/b
57.04761904761905
>>> #karena jumlah dari 1198 dibagi 21 adalah 57.04761904761905
>>> a//b
57
>>> #karena hasil bagi 1198 dibagi 21 adalah 57.04761904761905 dan dibulatkan menjadi 57
>>> 10*(a-999)
1990
>>> #karena hasil dari a-999 yang bernilai 1198 dikurangi 999 adalah 199 yang kemudian hasilnya dikalikan dengan 10
>>> b**2
441
>>> #karena tanda(**) adalah untuk mempangkatkan
>>> a%b
1
>>> #karena tanda (%) berarti hasil sisa pembagian dari 1198 oleh 21 adalah 1
>>> c=12.5
>>> type(c)
<class 'float'>
>>> #karena "12.5" adalah bilangan desimal bukan bilangan bulat
>>> a/c
95.84
>>> #karena hasil dari 1198 dibagi 12.5 adalah 95.84
>>> a//c
95.0
>>> #karena hasil bagi 1198 dibagi 12.5 adalah 95.84 dan dibulatkan menjadi 95.0
>>> a%c
10.5
>>> #karena tanda (%) berarti hasil sisa pembagian dari 1198 oleh 12.5 adalah 10.5
>>> c>b
False
>>> #karena tanda (<) merupakan operasi perbandingan yang menghasikan nilai true atau false, 12.5>21 bernilai false karena 12.5<21
>>> type(c>b)
<class 'bool'>
>>> #karena tanda (<) yang merupakan operasi perbandingan bertipe bool
>>> a>b and b>c
True
>>> #karena 1198>21 bernilai true dan 21>12.5 bernilai true. true and true bernilai true
>>> a>110 or b<10
True
>>> a>1100 or b<10
True
>>> #karena 1198>1100 bernilai true atau 21>10 bernilai true. true or true bernilai true
