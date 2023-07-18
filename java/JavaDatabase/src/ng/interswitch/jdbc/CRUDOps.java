package ng.interswitch.jdbc;

import java.io.*;
import java.sql.*;

public class CRUDOps {

    static final String DB_URL = "jdbc:sqlserver://;servername=ISW-230524-1335;database=Training;"+
            "instanceName=SQLEXPRESS;" +
            "encrypt=false;integratedSecurity=true;";

    public static String userInput(){
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter your table name: ");
        String tableName = null;
        try {
            tableName = br.readLine();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return tableName;
    }

    public static void createTable() throws ClassNotFoundException{
        try{
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String mySQLQuery = "CREATE TABLE " + userInput() + " (id INT not NULL IDENTITY(1, 1), " +
                    " first VARCHAR(50), " + " last VARCHAR(50), " +
                    " age INT, " + " PRIMARY KEY ( id ))";
            stmt.executeUpdate(mySQLQuery);
            System.out.println("Created table in given database...");
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void insertRecord() throws ClassNotFoundException{
        try{
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String tableName = userInput();
            String mySQLQuery1 = "INSERT INTO " + tableName + " VALUES ('Marcus', 'Atillus-Regulus', 21)";
            stmt.executeUpdate(mySQLQuery1);
            System.out.println("Inserted first record in given table...");
            String mySQLQuery2 = "INSERT INTO " + tableName + " VALUES ('Spartacus', 'Marcellius', 24)";
            stmt.executeUpdate(mySQLQuery2);
            System.out.println("Inserted second record in given table...");
            String mySQLQuery3 = "INSERT INTO " + tableName + " VALUES ('Crixus', 'Marcellius', 24)";
            stmt.executeUpdate(mySQLQuery3);
            String mySQLQuery4 = "INSERT INTO " + tableName + " VALUES ('Giaus', 'Pendergast', 37)";
            stmt.executeUpdate(mySQLQuery4);
            System.out.println("Inserted Third record in given table...");
            String mySQLQuery5 = "INSERT INTO " + tableName + " VALUES ('Aurellius', 'Dionysus', 33)";
            stmt.executeUpdate(mySQLQuery5);
            System.out.println("Inserted Fourth record in given table...");
            String mySQLQuery6 = "INSERT INTO " + tableName + " VALUES ('Aphrodite', 'Gander', 21)";
            stmt.executeUpdate(mySQLQuery6);
            System.out.println("Inserted Fifth record in given table...");
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void selectRecords() throws ClassNotFoundException{
        try{
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String mySQLQuery = "SELECT * FROM " + userInput();
            stmt.executeQuery(mySQLQuery);
            ResultSet rs = stmt.getResultSet();
            while(rs.next()) {
                System.out.println(rs.getString("id") + "---" + rs.getString("first")
                        + "---" + rs.getString("last")+ "---" + rs.getString("age")
                );
            }
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void updateRecord() throws ClassNotFoundException{
        try {
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String mySQLQuery = "UPDATE " + userInput() + " SET first = 'Spartacus' WHERE id = 2";
            stmt.executeUpdate(mySQLQuery);
            System.out.println("Record updated...");
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }
    public static void deleteRecord() throws ClassNotFoundException{
        try {
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String mySQLQuery = "DELETE FROM "+ userInput() + " WHERE id = 6";
            stmt.executeUpdate(mySQLQuery);
            System.out.println("Record permanently deleted...");
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void selectRecordsWIthIDGreaterThanAndLessThanFour() throws ClassNotFoundException{
        try{
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String mySQLQuery = "SELECT * FROM " + userInput() + " WHERE (id > 1) AND (id < 4)";
            stmt.executeQuery(mySQLQuery);
            ResultSet rs = stmt.getResultSet();
            while(rs.next()) {
                System.out.println(rs.getString("id") + "---" + rs.getString("first")
                        + "---" + rs.getString("last")+ "---" + rs.getString("age")
                );
            }
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void selectRecordsWhereFirstNameStartsWithCr() throws ClassNotFoundException{
        try{
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String mySQLQuery = "SELECT * FROM " + userInput() + " WHERE first LIKE 'Cr%'";
            stmt.executeQuery(mySQLQuery);
            ResultSet rs = stmt.getResultSet();
            while(rs.next()) {
                System.out.println(rs.getString("id") + "---" + rs.getString("first")
                        + "---" + rs.getString("last")+ "---" + rs.getString("age")
                );
            }
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void selectRecordsSortedInDescendingOrderOfFirstName() throws ClassNotFoundException{
        try{
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String mySQLQuery = "SELECT * FROM " + userInput() + " ORDER BY first DESC";
            stmt.executeQuery(mySQLQuery);
            ResultSet rs = stmt.getResultSet();
            while(rs.next()) {
                System.out.println(rs.getString("id") + "---" + rs.getString("first")
                        + "---" + rs.getString("last")+ "---" + rs.getString("age")
                );
            }
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void dropTable() throws ClassNotFoundException {
        try {
            Connection connection = DriverManager.getConnection(DB_URL);
            Statement stmt = connection.createStatement();
            String mySQLQuery = "DROP TABLE "+ userInput();
            stmt.executeUpdate(mySQLQuery);
            System.out.println("Table dropped...");
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }

    public static void main(String[] args) throws ClassNotFoundException {
        try{
            Connection connection = DriverManager.getConnection(DB_URL);
//            createTable();
//            insertRecord();
//            selectRecords();
//            updateRecord();
//            deleteRecord();
//            selectRecordsWIthIDGreaterThanAndLessThanFour();
//            selectRecordsWhereFirstNameStartsWithCr();
//            selectRecordsSortedInDescendingOrderOfFirstName()
//            dropTable();
            System.out.println("Bayron Mode Connection, successful!");
            connection.close();
        } catch (SQLException omoENoWorkO) {
            omoENoWorkO.printStackTrace();
        }
    }
}
