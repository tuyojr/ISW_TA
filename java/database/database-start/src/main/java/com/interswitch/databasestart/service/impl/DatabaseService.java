package com.interswitch.databasestart.service.impl;

import com.interswitch.databasestart.model.DatabaseModel;
import com.interswitch.databasestart.repository.DatabaseRepository;
import com.interswitch.databasestart.service.IDatabaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.Optional;

@Service
public class DatabaseService implements IDatabaseService {
    @Autowired
    DatabaseRepository databaseRepository;

    @Override
    public String addNewCustomer(DatabaseModel customer) {
        if(customer == null){
            return "Customer is null, it should not be.";
        }
        Long id = databaseRepository.save(customer).getId();
        return "Customer saved successfully with id: " + id + ".";
    }

    @Override
    public String updateExistingCustomer(Long id, DatabaseModel updatedCustomer) {
        Optional<DatabaseModel> existingCustomer = databaseRepository.findById(id);
        if (existingCustomer.isPresent()) {
            DatabaseModel customer_to_update = existingCustomer.get();
            customer_to_update.setFullName(updatedCustomer.getFullName());
            customer_to_update.setPhoneNumber(updatedCustomer.getPhoneNumber());
            databaseRepository.save(customer_to_update);
        } else {
            throw new IllegalArgumentException("User with " + id + " not found");
        }
        return "Customer updated successfully.";
    }

    @Override
    public Optional<DatabaseModel> getOneCustomerByID(Long id) {
        if (id == null) return Optional.empty();
        return databaseRepository.findById(id);
    }

    @Override
    public Collection<DatabaseModel> getAllCustomers() {
        return databaseRepository.findAll();
    }
}
