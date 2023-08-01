package com.interswitch.databasestart.repository;

import com.interswitch.databasestart.model.DatabaseModel;
import java.util.*;

public interface DatabaseRepository{
    // create 5 methods: findByID(returns customer), findAll(returns list of customer),
    // deleteByID(returns void), updateByID(return customer), addNewCustomer(returns customer)

    Optional<DatabaseModel> findCustomerByID(Long id);
    List<DatabaseModel> findAllCustomers();
    void deleteCustomerByID(Long id);
    DatabaseModel updateCustomerByID(Long id, DatabaseModel updatedCustomer);
    DatabaseModel addNewCustomer(DatabaseModel customer);
}
