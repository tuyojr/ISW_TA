package com.interswitch.databasestart.repository.impl;

import com.interswitch.databasestart.model.DatabaseModel;
import com.interswitch.databasestart.repository.DatabaseRepository;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jakarta.persistence.TypedQuery;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

@Component
public class JpaDatabaseRepository implements DatabaseRepository {
    @PersistenceContext
    private EntityManager em;

    @Override
    public Optional<DatabaseModel> findCustomerByID(Long id) {
        TypedQuery<DatabaseModel> query = em.createQuery("SELECT c FROM DatabaseModel " +
                "c WHERE c.id = :id", DatabaseModel.class);
        return Optional.of(query.setParameter("id", id).getSingleResult());
    }

    @Override
    public List<DatabaseModel> findAllCustomers() {
        TypedQuery<DatabaseModel> query = em.createQuery("SELECT c FROM " +
                "DatabaseModel c", DatabaseModel.class);
        return query.getResultList();
    }

    @Override
    public void deleteCustomerByID(Long id) {
        DatabaseModel customer = findCustomerByID(id).get();
        if(customer != null){ em.remove(customer); }
    }

    @Override
    public DatabaseModel updateCustomerByID(Long id, DatabaseModel updatedCustomer) {
        if(findCustomerByID(id).get() != null){
            em.merge(updatedCustomer);
        }
        return updatedCustomer;
    }

    @Override
    public DatabaseModel addNewCustomer(DatabaseModel customer) {
        em.persist(customer);
        return customer;
    }
}
