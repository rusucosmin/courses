package ro.dutylabs.mpp.core.service;

import ro.dutylabs.mpp.core.model.Client;

import java.util.List;

/**
 * Created by cosmin on 11/06/2017.
 */
public interface ClientService {
    List<Client> findAll();
    Client createClient(String name);
    Client findOne(Long id);
    Client updateClient(Long id, String name);
    void deleteClient(Long id);
}
