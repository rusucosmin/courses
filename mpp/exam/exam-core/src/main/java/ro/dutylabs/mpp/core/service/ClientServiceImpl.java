package ro.dutylabs.mpp.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ro.dutylabs.mpp.core.model.Client;
import ro.dutylabs.mpp.core.repository.ClientRepository;

import java.util.List;

/**
 * Created by cosmin on 11/06/2017.
 */
@Service
public class ClientServiceImpl implements ClientService {

    private static final Logger log = LoggerFactory.getLogger(ClientServiceImpl.class);

    @Autowired
    private ClientRepository clientRepository;

    @Override
    public List<Client> findAll() {
        return clientRepository.findAll();
    }

    @Override
    public Client createClient(String name) {
        Client client = Client.builder()
                .name(name)
                .build();
        client = clientRepository.save(client);
        return client;
    }

    @Override
    public Client findOne(Long id) {
        return clientRepository.findOne(id);
    }

    @Override
    @Transactional
    public Client updateClient(Long id, String name) {
        Client client = clientRepository.getOne(id);
        clientRepository.findOne(id);
        client.setName(name);
        return client;
    }

    @Override
    public void deleteClient(Long id) {
        clientRepository.delete(id);
    }
}
