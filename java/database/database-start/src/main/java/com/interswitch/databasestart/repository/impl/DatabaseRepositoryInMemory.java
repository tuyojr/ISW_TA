package com.interswitch.databasestart.repository.impl;

import com.interswitch.databasestart.model.DatabaseModel;
import com.interswitch.databasestart.repository.DatabaseRepository;

import java.util.*;
import java.util.Optional;

public class DatabaseRepositoryInMemory implements DatabaseRepository{

    private final DatabaseRepositoryJpa databaseRepositoryJpa;
    private Map<Long, DatabaseModel> databaseInMemory = new HashMap<>();

    public DatabaseRepositoryInMemory(DatabaseRepositoryJpa databaseRepositoryJpa) {
        this.databaseRepositoryJpa = databaseRepositoryJpa;
    }

    @Override
    public Optional<DatabaseModel> findCustomerByID(Long id) {
        return Optional.of(databaseInMemory.get(id));
    }

    @Override
    public List<DatabaseModel> findAllCustomers() {
        return new ArrayList<>(databaseInMemory.values());
    }

    @Override
    public void deleteCustomerByID(Long id) {
        databaseInMemory.remove(id);
    }

    @Override
    public DatabaseModel updateCustomerByID(Long id, DatabaseModel updatedCustomer) {
        return databaseInMemory.put(id, updatedCustomer);
    }

    @Override
    public DatabaseModel addNewCustomer(DatabaseModel customer) {
        return databaseInMemory.put(customer.getId(), customer);
    }
}
