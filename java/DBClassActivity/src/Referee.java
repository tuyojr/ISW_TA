import java.sql.*;

public class Referee {
    static final String INSERT_QUERY = "INSERT INTO Referee (name, phone_number, profession, address)  " +
            "VALUES (?,?,?,?)";
    static final String SELECT_QUERY = "SELECT TOP 1 referee_id FROM Referee ORDER BY referee_id DESC";

    public static String createReferee(User ref) {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(INSERT_QUERY);
        ) {
            // Execute a query
            stmt.setString(1, ref.getName());
            stmt.setInt(2, ref.getPhone_number());
            stmt.setString(3, ref.getProfession());
            stmt.setInt(4, ref.getAddress_id());
            int result = stmt.executeUpdate();
            if (result == 1) return "Referee created successfully!";
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static User selectRefereeID() {
        try(Connection conn = DriverManager
                .getConnection(Main.DB_URL);
            PreparedStatement stmt = conn.prepareStatement(SELECT_QUERY);
        ) {
            // Execute a query
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                User referee_id = new User();
                referee_id.setReferee_id(rs.getInt("referee_id"));
                return referee_id;
            } else {
                return null;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
}
