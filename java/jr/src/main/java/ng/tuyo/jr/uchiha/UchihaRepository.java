package ng.tuyo.jr.uchiha;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RestController;

import java.util.Optional;

// the repository layer is where the data is stored and retrieved from the database
// the JpaRepository interface is used to perform CRUD operations on the database
// the JpaRepository interface takes two parameters
// the first parameter is the class that represents the table in the database
// the second parameter is the type of the primary key of the table
// we want to use this interface inside the service class

@Repository // makes the class serve as a repository layer (repository layer is also known as the data access layer)
public interface UchihaRepository extends JpaRepository<Uchiha, Long> {
    // custom method to find a user by name
//    @Query("SELECT u FROM Uchiha u WHERE u.name = ?1") // this is the query that jbql runs on our db.
    Optional<Uchiha> findUchihaByName(String name);

    Optional<Uchiha> findUchihaById(Long uchihaId);
}
