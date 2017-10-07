
header = """
<html>
<head>
<title>Python CGI - Netstat</title>
"""
css = """
<style>
body {
  font-family: "Open Sans", sans-serif;
  line-height: 1.25;
}

table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    /*width: 100%;*/
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

td {
    padding: 2px 10px;
}
tr:nth-child(even) {
    background-color: #eeeeee;
}
</style>
"""
jsc = """
  <!-- <script src="jquery-1.10.2.js"></script> -->
<script language ="javascript" >
	var tmp;
	function f1() {
		tmp = setTimeout("callitrept()", 8000);
	}
	function callitrept() {
		document.getElementById("go").click();
	}
	function msg(a){
		alert(a)
	}
	function c(){
		var s = document.getElementById("ar").checked
		alert(s)
	}
</script>
"""
startbody = """
</head>
<body onload="f1()">
<h2><a href="index.py?searchbox=&hname=NO">NetStat</a></h2>
"""
startbody1 = """
</head>
<body">
"""

form = """
<form name="search" action="index.py" method="get" border="1">
Filter Keyword : <input type="text" name="searchbox" value="estab">
<input type="submit" value="GO !" id="go">
<input type="radio" name="hname" value="NO">Hide Host  |
<input type="radio" name="hname" value="YES" checked>Show Host  <!-- |
<input type="checkbox" id="ar" onclick="c()" name="autor"  value="Autorefresh"> Autorefresh -->
</form>"""

endbody = "</body></html>"


