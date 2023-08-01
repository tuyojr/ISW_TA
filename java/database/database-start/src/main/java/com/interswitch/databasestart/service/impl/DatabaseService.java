package com.interswitch.databasestart.service.impl;

import com.interswitch.databasestart.model.DatabaseModel;
import com.interswitch.databasestart.repository.impl.DatabaseRepositoryJpa;
import com.interswitch.databasestart.service.IDatabaseService;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.Optional;

@Service
public class DatabaseService implements IDatabaseService {
//    @Autowired
    private final DatabaseRepositoryJpa databaseRepository;

    public DatabaseService(DatabaseRepositoryJpa databaseRepository) {
        this.databaseRepository = databaseRepository;
    }

    @Override
    public DatabaseModel addNewCustomer(DatabaseModel customer) {
//        if(customer == null){
//            return null;
//        }
        return databaseRepository.addNewCustomer(customer);
    }

    @Override
    public String updateExistingCustomer(Long id, DatabaseModel updatedCustomer) {
        Optional<DatabaseModel> existingCustomer = databaseRepository.findCustomerByID(id);
        if (existingCustomer.isPresent()) {
            DatabaseModel customer_to_update = existingCustomer.get();
            customer_to_update.setFullName(updatedCustomer.getFullName());
            customer_to_update.setPhoneNumber(updatedCustomer.getPhoneNumber());
            databaseRepository.updateCustomerByID(id, customer_to_update);
        } else {
            throw new IllegalArgumentException("User with " + id + " not found");
        }
        return "Customer updated successfully.";
    }

    @Override
    public Optional<DatabaseModel> getOneCustomerByID(Long id) {
        if (id == null) return Optional.empty();
        // return the details of the customer with the specified id
        return databaseRepository.findCustomerByID(id);
    }

    @Override
    public Collection<DatabaseModel> getAllCustomers() {
        return databaseRepository.findAllCustomers();
    }
}
