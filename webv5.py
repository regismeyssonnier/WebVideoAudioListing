import os    
IP = "86.221.172.222"
#IP = "90.15.237.4"
def CreateListFiles(path, d):    
	fw = open(path + "\\index.html", "w")    
	fw.write("<html><head><link rel=\"icon\" type=\"image/png\" href=\"favicon.ico\"/>"); 
	fw.write("<meta charset=\"UTF-8\">"); 
	fw.write("<meta name=\"description\" content=\"Free Video Online\">"); 
	fw.write("<meta name=\"keywords\" content=\"Video,mp4,mp3\">"); 
	fw.write("<meta name=\"author\" content=\"cleirvinv08srdk5sjiwglcs1yunfg@gmail.com\">"); 
	fw.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"); 
	fw.write("<title>Free Video Online</title>");
	fw.write("</head><body lang=\"en\" onload=\"Init()\" onscroll=\"Unscroll()\">");    
	fw.write("<style>");    
	fw.write("body{background-image: url(\"\");background-color:#555555;color:#000000;font-family:Arial;margin:0px;}");    
	fw.write(".ltable{background-image: url(\"\");}");
	fw.write("a{color:#00FF00;}");   
	fw.write("h1{color:#FF55FF;}");   
	fw.write(".menu_u {position:fixed;background-color: #FFFFFF;z-index:500;}");	
	fw.write(".menu_p {opacity:0.9;filter:alpha(opacity=90);}");
	fw.write(".menu_elem {background-color: #000000;width:33%;text-align:center;padding-top:10px;padding-bottom:10px;}");
	fw.write(".menu_elem a {color: white;text-align: center;text-decoration: none;}");
	fw.write(".menu_elem:hover {background: -webkit-radial-gradient(green, #008800, black);background: -o-radial-gradient(green, #008800, black);");
	fw.write("background: -moz-radial-gradient(green, #008800, black);background: radial-gradient(green, #008800, black); background-color: #000000;}");
	fw.write(".sel_menu_elem{width:33%;text-align:center;padding-top:10px;padding-bottom:10px;");
	fw.write("background: -webkit-radial-gradient(green 30%, #008800 10%, black 60%);background: -o-radial-gradient(green 30%, #008800 10%, black 60%);");
	fw.write("background: -moz-radial-gradient(green 30%, #008800 10%, black 60%);background: radial-gradient(green 30%, #008800 10%, black 60%); background-color: #000000;}");
	fw.write(".sel_menu_elem a {color: white;text-align: center;text-decoration: none;}");
	fw.write(".sel_menu_elem:hover {background: -webkit-radial-gradient(green, #008800, black);background: -o-radial-gradient(green, #008800, black);");
	fw.write("background: -moz-radial-gradient(green, #008800, black);background: radial-gradient(green, #008800, black); background-color: #000000;}");
	#fw.write(".link{background-color:#000000;opacity:0.7;filter:alpha(opacity=70);color:#00FF00;cursor:hand;}");  
	#fw.write(".size{background-color:#000000;opacity:0.7;filter:alpha(opacity=70);}"); 
	fw.write(".link{color:#000000;cursor:hand;}");  
	fw.write(".link:hover{color:red;cursor:hand;}");  
	fw.write(".trf:hover td{background-color:#FAEBD7;color:red;cursor:hand;}"); 
	fw.write(".size{color:#000000;}"); 
	fw.write(".txt{color:#008800;}");    
	fw.write(".dvid{");  
	fw.write("	background-image: url(\"\");");  
	fw.write("	padding:0px 0px 0px 0px;");  
	fw.write("	width:100%;");  
	fw.write("	height:100%;");  
	fw.write("	background-color:#555555;"); 
	fw.write("	background: -webkit-radial-gradient(circle, #335555, #555555, black);background: -o-radial-gradient(circle, #335555, #555555, black);");
	fw.write("	background: -moz-radial-gradient(circle, #335555, #555555, black);background: radial-gradient(circle,#335555 ,#555555, black);");
	#fw.write("	background-color: hsla(120, 100%, 25%, 0.70);");  
	fw.write("	position:absolute;");  
	fw.write("	left:0px;");  
	fw.write("	top:0px;");  
	fw.write("	display:none;");  
	fw.write("	z-index:1000;"); 
	fw.write("}");  
	fw.write(".dvidsp span{position:relative;color:orange;cursor:hand;padding:5px 0px 0px 0px;margin:15px 10px 5px 0px;}");
	fw.write(".dplay{"); 
	#fw.write("	background-color: hsla(120, 100%, 25%, 0.99);");   
	fw.write("	z-index:1100;"); 
	fw.write("}"); 
	fw.write(".dclose{");  
	fw.write("	position:relative;");  
	fw.write("	left:0px;");  
	fw.write("	top:10px;");  
	fw.write("	width : 100px;");  
	fw.write("	height: 25px;");  
	fw.write("	color:orange;cursor:hand;");  
	fw.write("	font-size: 20px;");  
	fw.write("}");  
	fw.write(".dclose:hover{");  
	fw.write("	color : red;");  
	fw.write("}");  
	fw.write(".bclose{");  
	fw.write("	position:absolute;");  
	fw.write("	right:0px;");  
	fw.write("	top:0px;");  
	fw.write("	width : 25px;");  
	fw.write("	height: 25px;");  
	fw.write("	background-color:red;");  
	fw.write("	color:white;cursor:hand;");  
	fw.write("	text-align:center;"); 
	fw.write("	border-radius:5px;"); 
	fw.write("	font-size: 20px;");  
	fw.write("}"); 
	fw.write(".bclose:hover{");  
	fw.write("	color : orange;");  
	fw.write("}");  
	fw.write(".bfull{");  
	fw.write("	position:absolute;");  
	fw.write("	right:30px;");  
	fw.write("	top:0px;");  
	fw.write("	width : 25px;");  
	fw.write("	height: 25px;");  
	fw.write("	background-color:blue;");  
	fw.write("	color:white;cursor:hand;");  
	fw.write("	text-align:center;"); 
	fw.write("	border-radius:5px;"); 
	fw.write("	font-size: 20px;");  
	fw.write("}"); 
	fw.write(".bfull:hover{");  
	fw.write("	color : orange;");  
	fw.write("}"); 
	fw.write("</style>");    
	fw.write("<script>");  
	fw.write("	function Init(){");
	fw.write("		setSpeed(1.06, 'x106');"); 
	fw.write("		setVolume(0.15);"); 
	fw.write("	}");
	fw.write("	var scrolling = 1;");  
	fw.write("function Unscroll(){");  
	fw.write("	if(scrolling == 0){");  
	fw.write("		document.body.scrollTop = 0;");  
	fw.write("		document.documentElement.scrollTop = 0;");  
	fw.write("	}");  
	fw.write("}");  
	fw.write("	function ShVideo(s){");  
	fw.write("		scrolling = 0;");  
	fw.write("		document.body.scrollTop = 0;");  
	fw.write("		document.documentElement.scrollTop = 0;");  
	fw.write("		document.getElementById(\"vid\").style.display = \"block\";");  
	fw.write("		document.getElementById(\"video_control\").src = s;");  
	fw.write("		document.getElementById(\"video_control\").preload = \"auto\";");  
	fw.write("		document.getElementById(\"video_control\").loop = \"true\";");  
	fw.write("		return false;");  
	fw.write("	}");  
	fw.write("	function HVideo(){");  
	fw.write("		scrolling = 1;");  
	fw.write("		document.getElementById(\"vid\").style.display = \"none\";");  
	fw.write("		document.getElementById(\"video_control\").pause();");  
	fw.write("		return false;");  
	fw.write("	}");  
	fw.write("	function getState(){");
	fw.write("		var state = document.getElementById(\"video_control\").networkState;");
	fw.write("		var res;");
	fw.write("		if(state == 0){");
	fw.write("			res =  \"Not initialized\";");
	fw.write("		}");
	fw.write("		else if(state == 1){");
	fw.write("			res = \"Active\";");
	fw.write("		}");
	fw.write("		else if(state == 2){");
	fw.write("			res = \"Downloading data\";");
	fw.write("		}");
	fw.write("		else if(state == 3){");
	fw.write("			res = \"Not found\";");
	fw.write("		}");
	fw.write("		document.getElementById(\"state\").innerHTML = \"State : \" + res;");
	fw.write("	}");
	fw.write("	var ID=\"xm1\";");
	fw.write("	function setSpeed(x, i){");
	fw.write("		document.getElementById(\"video_control\").defaultPlaybackRate = x;"); 
	fw.write("		document.getElementById(\"video_control\").load();"); 
	fw.write("		document.getElementById(ID).style.color = \"orange\";");
	fw.write("		document.getElementById(i).style.color = \"yellow\";");
	fw.write("		ID = i;");
	fw.write("	}");
	fw.write("	function setVolume(x){");
	fw.write("		document.getElementById(\"video_control\").volume = x;"); 
	fw.write("	}");
	fw.write("</script>");  
	fw.write("<div id=\"vid\" class=\"dvid\" >");  
	fw.write("<div id=\"bfull\" class=\"bfull\" onclick=\"Init();\">=</div>");
	fw.write("<div id=\"bclose\" class=\"bclose\" onclick=\"HVideo();\">x");
	fw.write("</div>");
	fw.write("<div  align=\"center\">");  
	fw.write("		<video  width=\"80%\" height=\"80%\" controls id=\"video_control\">");  
	fw.write("		  <source src=\"\" type=\"video/mp4\">");  
	fw.write("		</video>");  
	fw.write("		<div class=\"dvidsp\"  >");  
	fw.write("			<span id=\"state\" onclick=\"getState();\">State</span>");  
	fw.write("			<span id=\"xm1\" onclick=\"setSpeed(-1.0, 'xm1');\">Speed : x-1</span>");
	fw.write("			<span id=\"xm05\" onclick=\"setSpeed(-0.5, 'xm05');\">x-0.5</span>");
	fw.write("			<span id=\"x025\" onclick=\"setSpeed(0.25, 'x025');\">x0.25</span>");
	fw.write("			<span id=\"x05\" onclick=\"setSpeed(0.5, 'x05');\">x0.5</span>");
	fw.write("			<span id=\"x075\" onclick=\"setSpeed(0.75, 'x075');\">x0.75</span>");
	fw.write("			<span id=\"x1\" onclick=\"setSpeed(1.0, 'x1');\">x1</span>");
	fw.write("			<span id=\"x106\" onclick=\"setSpeed(1.06, 'x106');\">x1.06</span>");
	fw.write("			<span id=\"x115\" onclick=\"setSpeed(1.15, 'x115');\">x1.15</span>");
	fw.write("			<span id=\"x125\" onclick=\"setSpeed(1.25, 'x125');\">x1.25</span>");
	fw.write("			<span id=\"x15\" onclick=\"setSpeed(1.5, 'x15');\">x1.5</span>");
	fw.write("			<span id=\"x175\" onclick=\"setSpeed(1.75, 'x175');\">x1.75</span>");
	fw.write("			<span id=\"x2\" onclick=\"setSpeed(2.0, 'x2');\">x2</span>");
	fw.write("			<span id=\"x5\" onclick=\"setSpeed(5.0, 'x5');\">x5</span>");
	fw.write("		</div>");  
	#fw.write("		<div class=\"dclose\" onclick=\"HVideo();\" >");  
	#fw.write("			Close");  
	#fw.write("		</div>");  
	fw.write("	</div>");  
	fw.write("</div>");  
	fw.write("<table class=\"menu_u\" width=\"100%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\">");
	fw.write("<tbody><tr>") 
	fw.write("<td class=\"sel_menu_elem\"><a class=\"active\" href=\"#up\">Video</a></td>");
	fw.write("<td class=\"menu_elem\"><a class=\"active\" href=\"#up\">Musique</a></td>");
	fw.write("<td class=\"menu_elem\"><a class=\"active\" href=\"#up\">Magazine</a></td>");
	fw.write("</tr></tbody>") 
	fw.write("</table><br><br><br>") 
	#fw.write("<h1 id=\"up\" class=\"\" align=\"center\">Free Video Online</h1>")    
	#fw.write("<div align=\"center\"><iframe id=\"up\" src=\"https://www.facebook.com/plugins/follow?href=https%3A%2F%2Fwww.facebook.com%2FLe.BoSSSSSSS&amp;layout=standard&amp;show_faces=true&amp;colorscheme=light&amp;width=450&amp;height=80\" scrolling=\"no\" frameborder=\"0\" style=\"border:none; overflow:hidden; width:450px; height:80px;\" allowTransparency=\"true\"></iframe></div>") 
	fw.write("<table class=\"menu_p\" width=\"90%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\">");
	fw.write("<tbody><tr>") 
	fw.write("<td class=\"sel_menu_elem\" style=\"border-radius: 20px 0px 0px 0px;\"><a class=\"active\" href=\"http://" + IP + "/Video/index.html\">Video</a></td>");
	fw.write("<td class=\"menu_elem\"><a class=\"active\" href=\"http://" + IP + "/Music/index.html\">Music</a></td>");
	fw.write("<td class=\"menu_elem\" style=\"border-radius: 0px 20px 0px 0px;\"><a class=\"active\" href=\"http://" + IP  + "/Magazine/index.html\">Lyrics</a></td>");
	fw.write("</tr></tbody>") 
	fw.write("</table>") 
	fw.write("<table class=\"ltable\" width=\"90%\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" style=\"background-color:white;\">");    
	fw.write("<tbody>")    
	fw.write("<tr><th></th><th>filename</th><th width=\"10%\" colspan=\"2\" align=\"center\">size</th></tr>");    
	lf = os.listdir(path)  
	i = 1
	for f in lf:    
		if ".mp4" in f or ".mp3" in f: 
			fw.write("<tr class=\"trf\"><td align=\"center\">{0}</td><td style=\"padding:2px 0px 2px 10px;\" align=\"left\">".format(i)); i=i+1    
			s = os.stat(path + "\\" + f)    
			if f == d:    
				fw.write("	<a href=\"" + f + "\\list.html" + "\">" + f + "</a>");    
			else:    
				fw.write("	<span class=\"link\" onclick=\"javascript:ShVideo('" + f + "')\">" + f + "</span>");   
			fw.write("</td><td class=\"size\" align=\"right\">"); 
			si = s.st_size;
			r = si / 1073741824;
			if r > 0 :
				fw.write("{:,}</td><td class=\"size\" align=\"left\"> &nbsp;Go".format(r)); 
			else :
				r = si / 1048576;
				if r > 0 :
					fw.write("{:,}</td><td class=\"size\" align=\"left\"> &nbsp;Mo".format(r)); 
				else :
					r = si / 1024;
					if r > 0 :
						fw.write("{:,}</td><td class=\"size\" align=\"left\"> &nbsp;Ko".format(r));    
					else :
						fw.write("{:,}</td><td class=\"size\" align=\"left\"> &nbsp;bytes".format(r));    
			fw.write("</td></tr>");    
	fw.write("</tbody>");    
	fw.write("</table>");    
	fw.write("</body></html>");    
	fw.close()    
CreateListFiles(os.getcwd(), "")    
import SimpleHTTPServer    
import SocketServer    
PORT = 80 
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler    
httpd = SocketServer.TCPServer(("", PORT), Handler)    
print "serving at port", PORT    
httpd.serve_forever()    
