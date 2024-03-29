import java.sql.*;

public class Contact {
    static final String INSERT_QUERY = "INSERT INTO Contact (first_name, last_name, phone_number, " +
            "sex, date_of_birth) VALUES (?,?,?,?,?)";

    static final String SELECT_QUERY = "SELECT TOP 1 contact_id FROM Contact ORDER BY contact_id DESC";

    public static String createContact(User contact) {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(INSERT_QUERY);
        ) {
            // Execute a query
            stmt.setString(1, contact.getFirst_name());
            stmt.setString(2, contact.getLast_name());
            stmt.setInt(3, contact.getPhone_number());
            stmt.setString(4, contact.getSex());
            stmt.setString(5, contact.getDate_of_birth());
            int result = stmt.executeUpdate();
            if (result == 1) return "Contact created successfully!";
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static User selectContactID() {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(SELECT_QUERY);
        ) {
            // Execute a query
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                User contact_id = new User();
                contact_id.setContact_id(rs.getInt("contact_id"));
                return contact_id;
            } else {
                return null;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
}
