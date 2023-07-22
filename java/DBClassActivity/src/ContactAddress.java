import java.sql.*;

public class ContactAddress {
    static final String INSERT_QUERY = "INSERT INTO Contact_Addresses ( address_id, contact_id) " +
            "VALUES (?,?)";

    public static void createContactAddressLink(User address, User contact) {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(INSERT_QUERY);
        ) {
            // Execute a query
            stmt.setInt(1, address.getAddress_id());
            stmt.setInt(2, contact.getContact_id());
            int result = stmt.executeUpdate();
            if (result == 1) {
                System.out.println("Contact linked to address successfully!");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
