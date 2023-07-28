package ng.spring.restapp.service.impl;

import ng.spring.restapp.model.Product;
import ng.spring.restapp.repository.ProductRepository;
import ng.spring.restapp.service.IProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class ProductServiceImplementation implements IProductService {

    @Autowired
    ProductRepository productRepository;

    @Override
    public String newProductName(Product product) {
        if(product == null){
            return "Product is null, it should not be.";
        }productRepository.save(product);
        return "Product saved successfully with id: " + product.getId() +
                " and name: " + product.getName() + ".";
    }

    @Override
    public Optional<Product> getSingleProduct(Long id) {
        return Optional.empty();
    }

    @Override
    public Collection<Product> getAllProducts() {
        return null;
    }

    @Override
    public void removeProduct(Long id) {

    }

    @Override
    public Product updateProduct(Long id) {
        return null;
    }
}
