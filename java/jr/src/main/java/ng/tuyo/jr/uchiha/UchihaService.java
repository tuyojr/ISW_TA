package ng.tuyo.jr.uchiha;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

// the service layer is where the business logic is implemented.
// this means that data is manipulated here before it is sent to the
// controller layer which is the API layer that sends the data to the client(browser)
// we need to tell that the UchihaService class is a dependency of the UchihaController class
// it needs to be instantiated so that the controller can use it.
// the @Component annotation is used to tell spring that the UchihaService class is a
// dependency of the UchihaController class
//@Component is the parent of @Service, @Repository, @Controller and @RestController
@Service // makes the class serve as a service layer
public class UchihaService {

    private final UchihaRepository uchihaRepository; // an instance of the UchihaRepository class has
    // to be injected into the constructor so that the service can use it

    @Autowired // injects an instance of the UchihaRepository class into the constructor
    public UchihaService(UchihaRepository uchihaRepository) {
        this.uchihaRepository = uchihaRepository;
    }
    public List<Uchiha> getUchiha(){ return uchihaRepository.findAll();
    }

    public void addNewUchiha(Uchiha uchiha) {
        Optional<Uchiha> uchihaByNameOptional = uchihaRepository
                .findUchihaByName(uchiha.getName());
        if(uchihaByNameOptional.isPresent()){
            throw new IllegalStateException("This name already exists, no two Uchihas can have the same name.");
        }
        uchihaRepository.save(uchiha);
        System.out.println("New Uchiha added to the clan successfully.");
    }


    public void deleteUchiha(Long uchihaId) {
        boolean exists = uchihaRepository.existsById(uchihaId);
        if(!exists){
            throw new IllegalStateException("Uchiha with id " +
                    uchihaId +
                    " does not exist in the clan.");
        }
        uchihaRepository.deleteById(uchihaId);
        System.out.println("Uchiha with id " +
                uchihaId +
                " has been exiled from the clan successfully.");
    }

    @Transactional // this annotation is used to update the database
    public void updateUchiha(Long uchihaId, String name, String powerUp){
        Uchiha uchiha = uchihaRepository.findById(uchihaId)
                .orElseThrow(() -> new IllegalStateException("Uchiha with id " +
                        uchihaId +
                        " does not exist in the clan."));
        if(name != null && !name.isEmpty() && !name.equals(uchiha.getName())){
            uchiha.setName(name);
        }
        if(powerUp != null && !powerUp.isEmpty() && !powerUp.equals(uchiha.getPowerUp())){
            uchiha.setPowerUp(powerUp);
        }
        System.out.println("Uchiha with id " +
                uchihaId +
                " has been updated successfully.");
    }
}
