import java.util.*;
import java.io.*;
import java.sql.*;

public class Main {
    static final String DB_URL = "jdbc:sqlserver://;servername=ISW-230524-1335;database=Training;"+
            "instanceName=SQLEXPRESS;" +
            "encrypt=false;integratedSecurity=true;";

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        try(Connection connection = DriverManager.getConnection(DB_URL)){
            System.out.println("Bayron Connection Successful!");
        }catch(SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }
}