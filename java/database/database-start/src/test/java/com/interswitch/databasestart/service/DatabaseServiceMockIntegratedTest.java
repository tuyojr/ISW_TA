package com.interswitch.databasestart.service;

import org.junit.jupiter.api.Test;
import org.springframework.boot.autoconfigure.AutoConfiguration;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.jdbc.Sql;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.transaction.annotation.Transactional;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfiguration
@Transactional
@ActiveProfiles("test")
public class DatabaseServiceMockIntegratedTest {
    private MockMvc mockMvc;

    @Test
    @Sql("create-customer.sql")
    public void testCreateCustomer() throws Exception{
        mockMvc.perform(post("/customers")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"id\":1,\"fullName\":\"Itachi\",\"phoneNumber\":\"" +
                        "8012345678\",\"dateJoined\":\"1992-11-22\"}"))
                .andExpect(status().isCreated());
    }
}
