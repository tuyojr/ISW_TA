package ng.spring.restapp.service.impl;

import ng.spring.restapp.model.Product;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

@Service
public class ProductService {
    private static Map<Long, Product> productRepo = new HashMap<>();
    static{
        Product honey = new Product();
        honey.setId(1L);
        honey.setName("Honey");
        productRepo.put(honey.getId(), honey);
        Product almond = new Product();
        almond.setId(2L);
        almond.setName("Almond");
        productRepo.put(almond.getId(), almond);
    }

    public void add(Product product) {
        productRepo.put(product.getId(), product);
    }

    public void removeProduct(Long id) {
        if(productRepo.containsKey(id)) {
            productRepo.remove(id);
        }
    }

    public void updateProduct(Long id, Product product) {
        if(productRepo.containsKey(product.getId())) {
            productRepo.remove(product.getId());
            productRepo.put(product.getId(), product);
        }
    }

    public Product getProduct(Long id) {
        return productRepo.get(id);
    }

    public Collection<Product> getProducts(){
        return productRepo.values();
    }
}
