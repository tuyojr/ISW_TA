package ng.spring.restapp.controller;

import lombok.AllArgsConstructor;
import ng.spring.restapp.model.Product;
import ng.spring.restapp.service.impl.ProductServiceImplementation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@AllArgsConstructor
@RestController
@RequestMapping("/prod")
public class ProductController {

    @Autowired
    ProductServiceImplementation productService;
    @PostMapping("/products")
    public ResponseEntity<Object> newProduct(@RequestBody Product product){
        productService.newProductName(product);
        return new ResponseEntity<>("New product added successfully!", HttpStatus.CREATED);
    }
}
