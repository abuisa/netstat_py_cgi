import cgi
import main_modl as mm
import html_var as html
print("Content-Type: text/html")

print(html.header)
print(html.form)
form = cgi.FieldStorage()
srh =  form.getvalue('searchbox') 
hname =  form.getvalue('hname')
if srh == None: srh = ':';
if srh != '':srh = srh
if hname == 'YES':t =mm.out2list(srh,True)
if hname == 'NO':t =mm.out2list(srh,False)
print('Filter Keyword : <b>'+srh+'</b> | Show Host: <b>'+hname+'</b>')
print('<table border="0">')
for l in t:
	print('<tr>')
	if l[0] == "NO":
		for ll in l:		
			ll = str(ll)
			print('<th>'+ll+'</th>')
		print('</tr>')
	if l[0] != "NO":
		for ll in l:	
			ll = str(ll)
			print('<td>'+ll+'</td>')
		print('</tr>')
	
print('</table><hr>')	

print(html.endbody)
#main()			