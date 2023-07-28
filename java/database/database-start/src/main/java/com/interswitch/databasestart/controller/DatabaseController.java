package com.interswitch.databasestart.controller;

import com.interswitch.databasestart.model.DatabaseModel;
import com.interswitch.databasestart.service.IDatabaseService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@AllArgsConstructor
@RestController
@RequestMapping("/customers")
public class DatabaseController {

    private final IDatabaseService dbService;

    @RequestMapping(value = "/all-customers")
    public ResponseEntity<Object> getAllCustomers(){
        return new ResponseEntity<>(dbService.getAllCustomers(), HttpStatus.OK);
    }

    @RequestMapping(value = "/all-customers/{id}")
    public ResponseEntity<Object> getCustomerByID(@PathVariable("id") Long id) {
        return new ResponseEntity<>(dbService.getOneCustomerByID(id), HttpStatus.OK);
    }

    @RequestMapping(value = "/add-customer", method = RequestMethod.POST)
    public ResponseEntity<Object> addNewCustomer(@RequestBody DatabaseModel customer){
        dbService.addNewCustomer(customer);
        return new ResponseEntity<>("New customer added successfully!", HttpStatus.CREATED);
    }

    @RequestMapping(value = "/update-customer/{id}", method = RequestMethod.PUT)
    public ResponseEntity<Object> updateExistingCustomer(@PathVariable("id") Long id, @RequestBody DatabaseModel customer){
        dbService.updateExistingCustomer(id, customer);
        return new ResponseEntity<>("Customer details updated successfully.", HttpStatus.OK);
    }
}
