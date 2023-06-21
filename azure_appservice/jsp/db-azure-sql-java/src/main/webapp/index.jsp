<%@ page import="com.azure.sql.sample.HWMain" %>

<html>
    <head>
        <style>
        div {
          background-color: #f1f1f1;
        }
        </style>
        </head>
        
<body>
    <br><a href="reset.jsp">Reset the database.</a><br>
    <a href="insights.jsp">See all settings and configuration.</a><br>
<%
        //Java class uses the following library: import java.sql.*;
        //out.println("Your IP address is " + request.getRemoteAddr() + "<br>");

        // Connect to Azure SQL DB
        out.println("<h2>Java Azure SQL Sample</h2>");
        out.println("<h4>Azure SQL demo with JSP front page and Java class backend using sql credentials</h4>");
        HWMain hw = new HWMain();

        try {
            //out.println("Demo starting<br>");
            out.println("<div><br>");
            
                out.println(hw.getAndIncrementCounter());
        } catch (Exception e) {
            out.println("Demo failed"+e.toString());
        } finally {
            //out.println("<br>Demo complete<br>");
        }
        out.println("<p></div>");

%>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<small><i>Hello World! version 0.34</i></small>

</body>
</html>
