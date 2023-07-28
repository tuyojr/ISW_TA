package ng.tuyo.jr.uchiha;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.util.List;

// contains all the resources / endpoints for the Uchiha class
// this is the API layer
@RestController //makes the class serve as a restful endpoint
@RequestMapping(path = "api/v1/uchiha") // makes the class serve as a restful endpoint
public class UchihaController {

    // using the n-tier architecture
    // the controller layer should only be concerned with the request and response

    private final UchihaService uchihaService;

    // an instance of the uchihaService has to be injected into the constructor so that the controller can use it
    // this can be done by using the @Autowired annotation or by using the constructor injection
    public UchihaController(@Autowired UchihaService uchihaService) {
        this.uchihaService = uchihaService;
    }

    @GetMapping // makes the method serve as a GET endpoint which is a restful endpoint
    public List<Uchiha> getUchiha(){
        return uchihaService.getUchiha();
    }
}
