package ng.interswitch.jdbc;
import java.io.*;
import java.sql.*;
public class CRUDOpsII {
    static final String DB_URL = "jdbc:sqlserver://;servername=ISW-230524-1335;database=Training;"+
            "instanceName=SQLEXPRESS;" +
            "encrypt=false;integratedSecurity=true;";

    public static String userTable() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter your table name: ");
        String tableName;
        tableName = br.readLine();
        return tableName;
    }

    public static String columns() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the number of columns you want to input: ");
        int columnNumber;
        columnNumber = Integer.parseInt(br.readLine());
        String[] columns = new String[columnNumber];
        for(int i = 0; i < columnNumber; i++){
            BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Enter column name and constraints: ");
            columns[i] = buff.readLine();
        }
        return String.join(", ", columns);
    }

    public static void createTable() throws ClassNotFoundException, IOException {
        try(Connection connection = DriverManager.getConnection(DB_URL)) {
            Statement stmt = connection.createStatement();
            String sqlQuery = "CREATE TABLE " + userTable() + "(" + columns() + ")";
//            System.out.println(sqlQuery);
            stmt.executeUpdate(sqlQuery);
            System.out.println("Table created successfully...");
        } catch(SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        try(Connection connection = DriverManager.getConnection(DB_URL)){
            System.out.println("Bayron Connection Successful!");
            createTable();
        }catch(SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }
}
