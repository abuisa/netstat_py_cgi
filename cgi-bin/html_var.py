
header = """
<html>
<head>
<title>Python CGI - Netstat</title>
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
</head>
<body>"""


form = """
<h2><a href="gto.py?searchbox=&hname=NO">NetStat</a></h2>
<form name="search" action="gto.py" method="get" border="1">
Filter Keyword : <input type="text" name="searchbox">
<input type="submit" value="Submit">
<input type="radio" name="hname" value="NO" checked>Hide Host  |
<input type="radio" name="hname" value="YES">Show Host

</form>"""

endbody = "</body></html>"


