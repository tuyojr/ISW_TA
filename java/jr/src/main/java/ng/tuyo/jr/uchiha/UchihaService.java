package ng.tuyo.jr.uchiha;

import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.util.List;

// the service layer is where the business logic is implemented.
// this means that data is manipulated here before it is sent to the
// controller layer which is the API layer that sends the data to the client(browser)
// we need to tell that the UchihaService class is a dependency of the UchihaController class
// it needs to be instantiated so that the controller can use it.
// the @Component annotation is used to tell spring that the UchihaService class is a
// dependency of the UchihaController class
@Component
public class UchihaService {
    public List<Uchiha> getUchiha(){ return List.of(
            new Uchiha(
                    1L,
                    "Sasuke",
                    "Rinne Sharingan",
                    LocalDate.of(2000, 11, 13),
                    23
            )
    );
    }
}
