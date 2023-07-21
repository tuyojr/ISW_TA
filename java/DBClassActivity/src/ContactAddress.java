import java.sql.*;

public class ContactAddress {
    static final String INSERT_QUERY = "INSERT INTO Contact_Addresses ( address_id, contact_id " +
            "VALUES (?,?)";

    public static String createAddressRefereeLink(User ref) {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(INSERT_QUERY);
        ) {
            // Execute a query
            stmt.setInt(1, ref.getAddress_id());
            stmt.setInt(2, ref.getContact_id());
            int result = stmt.executeUpdate();
            if (result == 1) return "Address linked to referee successfully!";
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
}
