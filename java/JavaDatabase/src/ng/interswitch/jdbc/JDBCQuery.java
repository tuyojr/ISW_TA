package ng.interswitch.jdbc;

import java.sql.*;

public class JDBCQuery {
    static final String DB_URL = "jdbc:sqlserver://;servername=ISW-230524-1335;database=Training;"+
            "instanceName=SQLEXPRESS;" +
            "encrypt=false;integratedSecurity=true;";
    public static void main(String[] args) throws ClassNotFoundException {
        try{
            Connection conn = DriverManager.getConnection(DB_URL);
            System.out.println("Bayron Mode, successful!");
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }
}
