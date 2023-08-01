package com.interswitch.databasestart.repository.impl;

import com.interswitch.databasestart.model.DatabaseModel;
import com.interswitch.databasestart.repository.DatabaseRepository;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;

public class DatabaseRepositoryJpa implements DatabaseRepository{
    private final JpaRepository<DatabaseModel, Long> jpaRepository;

    public DatabaseRepositoryJpa(JpaRepository jpaRepository) {
        this.jpaRepository = jpaRepository;
    }

    @Override
    public Optional<DatabaseModel> findCustomerByID(Long id) {
        return jpaRepository.findById(id);
    }

    @Override
    public List<DatabaseModel> findAllCustomers() {
        return jpaRepository.findAll();
    }

    @Override
    public void deleteCustomerByID(Long id) {
        jpaRepository.deleteById(id);
    }

    @Override
    public DatabaseModel updateCustomerByID(Long id, DatabaseModel updatedCustomer) {
        return jpaRepository.save(updatedCustomer);
    }

    @Override
    public DatabaseModel addNewCustomer(DatabaseModel customer) {
        return jpaRepository.save(customer);
    }
}
