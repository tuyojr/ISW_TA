import java.sql.*;

public class ContactReferees {
    static final String INSERT_QUERY = "INSERT INTO Contact_Refree (contact_id, referee_id)  " +
            "VALUES (?,?)";

    public static void createContactRefereeLink(User contact, User referee) {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(INSERT_QUERY);
        ) {
            // Execute a query
            stmt.setInt(1, contact.getContact_id());
            stmt.setInt(2, referee.getReferee_id());
            int result = stmt.executeUpdate();
            if (result == 1) System.out.println("Contact linked to referee successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
