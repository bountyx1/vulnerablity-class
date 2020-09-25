<%@ page import = "java.io.*,java.util.*" %>
 <%
 Enumeration headerNames = request.getHeaderNames();
 while(headerNames.hasMoreElements()) {
                  String paramName = (String)headerNames.nextElement();
                  out.print("{\""+paramName+"\":");
                  String paramValue = request.getHeader(paramName);
                  out.println("\""+paramValue+"\"}");
               }
            %>
