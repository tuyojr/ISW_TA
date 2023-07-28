package ng.spring.restapp.service;

import ng.spring.restapp.model.Product;
import java.util.Collection;
import java.util.Optional;

public interface IProductService {
    String newProductName(Product product);

    Optional<Product> getSingleProduct(Long id);

    Collection<Product> getAllProducts();

    void removeProduct(Long id);

    Product updateProduct(Long id);
}
