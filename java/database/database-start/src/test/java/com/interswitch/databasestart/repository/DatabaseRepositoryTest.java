package com.interswitch.databasestart.repository;

import com.interswitch.databasestart.model.DatabaseModel;
import com.interswitch.databasestart.repository.impl.DatabaseRepositoryInMemory;
import com.interswitch.databasestart.repository.impl.DatabaseRepositoryJpa;
import com.interswitch.databasestart.service.impl.DatabaseService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.*;

import static org.mockito.AdditionalAnswers.returnsFirstArg;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;


public class DatabaseRepositoryTest {
    private DatabaseRepositoryJpa databaseRepositoryJpa;
    private DatabaseRepositoryInMemory databaseRepositoryInMemory;
    private DatabaseService databaseService;

    @BeforeEach
    public void setUp(){
        databaseRepositoryJpa = mock(DatabaseRepositoryJpa.class);
        databaseRepositoryInMemory = new DatabaseRepositoryInMemory(databaseRepositoryJpa);
        databaseService = new DatabaseService(databaseRepositoryJpa);

    }

    @Test
    void addCustomer(){
        DatabaseModel customer = new DatabaseModel(1L,
                "Shisui Uchiha",
                8048578344L,
                "1988-10-02"
        );
        when(databaseRepositoryJpa.addNewCustomer(customer)).then(returnsFirstArg());
    }

    @Test
    void getAllCustomers(){
        List<DatabaseModel> customers = new ArrayList<>();
        databaseService.addNewCustomer(new DatabaseModel(1L,
                "Itachi Uchiha",
                7033374782L,
                "1992-11-17")
        );
        databaseService.addNewCustomer(new DatabaseModel(2L,
                "Madara Uchiha",
                9032839349L,
                "1914-01-23")
        );
        when(databaseService.getAllCustomers()).thenReturn(customers);
    }
}
