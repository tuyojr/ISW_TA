<%
int n = Integer.parseInt(request.getParameter("value"));
for(int i=1;i<=10;i++)
{
    out.print(i*n+"<br>");
}
%>