package ng.interswitch.jdbc;

import java.sql.*;

public class JDBCLink {

    public static void main(String[] args) throws ClassNotFoundException {
        String DB_URL = "jdbc:sqlserver://;servername=SERVER_NAME;database=DB_NAME;"+
                "instanceName=SQL_NAME;" +
                "encrypt=false;integratedSecurity=true;";

        try{
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            Connection conn = DriverManager.getConnection(DB_URL);
            Statement stmt = conn.createStatement();
            String sql = "SELECT * FROM dbo.table_name";
            stmt.execute(sql);
            // print the output of the query
            ResultSet rs = stmt.getResultSet();
            while(rs.next()) {
                System.out.println(rs.getString("colum1") + "---" + rs.getString("column2")
                        + "---" + rs.getString("colum3")+ "---" + rs.getString("colum4")
                        + "---" + rs.getString("colum5")
                );
            }
            System.out.println("Bayron Mode, successful!");
            conn.close();
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }
}
