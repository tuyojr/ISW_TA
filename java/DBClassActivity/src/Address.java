import java.sql.*;

public class Address {
    static final String INSERT_QUERY = "INSERT INTO Address (street, city, state, " +
            "country, zipcode) VALUES (?,?,?,?,?)";

    static final String SELECT_QUERY = "SELECT TOP 1 address_id FROM dbo.Address ORDER BY address_id DESC;";

    public static String createAddress(User address) {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(INSERT_QUERY);
        ) {
            // Execute a query
            stmt.setString(1, address.getStreet());
            stmt.setString(2, address.getCity());
            stmt.setString(3, address.getState());
            stmt.setString(4, address.getCountry());
            stmt.setInt(5, address.getZip_code());
            int result = stmt.executeUpdate();
            if (result == 1) return "Address added successfully!";
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static User selectAddressID() {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(SELECT_QUERY);
        ) {
            // Execute a query
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                User address_id = new User();
                address_id.setAddress_id(rs.getInt("address_id"));
                return address_id;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
}
