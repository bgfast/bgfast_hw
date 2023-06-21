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
<%        
        // Connect to Azure SQL DB
        out.println("<h2>Java Azure SQL Sample</h2>");
        out.println("<h4>Azure SQL demo with JSP front page and Java class backend using sql credentials</h4>");
        HWMain hw = new HWMain();

        try {
            //out.println("Reset starting<br>");
            out.println("<div><br>");
            
                //out.println(hw.resetDatabaseTable());
        } catch (Exception e) {
            out.println("Reset error:"+e.toString());
        } finally {
            //out.println("<br>Reset complete<br>");
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
<small><i>Hello World! version 0.28</i></small>

</body>
</html>
