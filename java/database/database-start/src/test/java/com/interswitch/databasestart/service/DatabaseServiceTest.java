package com.interswitch.databasestart.service;

import com.interswitch.databasestart.repository.DatabaseRepository;
import com.interswitch.databasestart.service.impl.DatabaseService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.AssertionsForInterfaceTypes.assertThat;
import static org.mockito.AdditionalAnswers.returnsFirstArg;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class DatabaseServiceTest {
    private DatabaseRepository databaseRepository;
    private DatabaseService databaseService;

    @BeforeEach
    void setUp(){
        databaseRepository = mock(DatabaseRepository.class);
        databaseService = new DatabaseService(databaseRepository);
    }

    @Test
    void testAddCustomer(){
        when(databaseService
                .addNewCustomer(any()))
                .then(returnsFirstArg());
    }

    @Test
    void testGetAllCustomers(){
        assertThat(databaseService.getAllCustomers())
                .isEmpty();
    }
}
