package ng.spring.restapp.controller;

import lombok.AllArgsConstructor;
import ng.spring.restapp.model.Product;
import ng.spring.restapp.service.impl.ProductService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@AllArgsConstructor
@RestController
@RequestMapping("/proddb")
public class ProdController {
    private final ProductService productService;

    @RequestMapping(value = "/products")
    public ResponseEntity<Object> getProducts(){
        return new ResponseEntity<>(productService.getProducts(), HttpStatus.OK);
    }

    @RequestMapping(value = "/products/{id}")
    public ResponseEntity<Object> getProducts(@PathVariable("id") Long id) {
        return new ResponseEntity<>(productService.getProduct(id), HttpStatus.OK);
    }
    @RequestMapping(value="/products", method= RequestMethod.POST)
    public ResponseEntity<Object> createProduct(@RequestBody Product product){
        productService.add(product);
        return new ResponseEntity<>("Product is created successfully",
                HttpStatus.CREATED);
    }

    @RequestMapping(value = "/products/{id}", method = RequestMethod.PUT)
    public ResponseEntity<Object> updateProduct(@PathVariable("id") Long id, @RequestBody Product product){
        productService.updateProduct(id, product);
        return new ResponseEntity<>("Product is updated successfully.", HttpStatus.OK);
    }
    @RequestMapping(value = "/products/{id}", method=RequestMethod.DELETE)
    public ResponseEntity<Object> delete(@PathVariable("id") Long id){
        productService.removeProduct(id);
        return new ResponseEntity<>("Product is deleted successfully", HttpStatus.OK);
    }
}
