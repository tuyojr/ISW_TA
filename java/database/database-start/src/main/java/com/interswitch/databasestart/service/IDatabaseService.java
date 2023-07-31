package com.interswitch.databasestart.service;

import com.interswitch.databasestart.model.DatabaseModel;

import java.util.*;

public interface IDatabaseService {

    DatabaseModel addNewCustomer(DatabaseModel customer);
    String updateExistingCustomer(Long id, DatabaseModel updatedCustomer);
    Optional<DatabaseModel> getOneCustomerByID(Long id);
    Collection<DatabaseModel> getAllCustomers();

}
