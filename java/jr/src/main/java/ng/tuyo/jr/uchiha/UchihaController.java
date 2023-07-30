package ng.tuyo.jr.uchiha;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

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

    @PostMapping
    public void registerNewUchiha(@RequestBody Uchiha uchiha){
        uchihaService.addNewUchiha(uchiha);
    }

    @DeleteMapping(path = "{uchihaId}")
    public void deleteUchiha(@PathVariable("uchihaId") Long uchihaId){
        uchihaService.deleteUchiha(uchihaId);
    }

    @PutMapping(path = "{uchihaId}")
    public void updateUchiha(
            @PathVariable("uchihaId") Long uchihaId,
            @RequestParam(required = false) String name,
            @RequestParam(required = false) String powerUp){
        uchihaService.updateUchiha(uchihaId, name, powerUp);
    }
}
