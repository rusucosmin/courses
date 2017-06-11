package ro.dutylabs.mpp.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import ro.dutylabs.mpp.core.service.ClientService;
import ro.dutylabs.mpp.web.converter.ClientConverter;
import ro.dutylabs.mpp.web.dto.ClientsDto;

/**
 * Created by cosmin on 11/06/2017.
 */
@RestController
public class ClientController {
    @Autowired
    private ClientService clientService;
    @Autowired
    private ClientConverter clientConverter;

    private static final Logger log = LoggerFactory.getLogger(ClientController.class);

    @RequestMapping(value = "/clients", method = RequestMethod.GET)
    public ClientsDto getAll() {
        log.trace("ClientController::getAll()");
        return new ClientsDto(clientConverter.convertModelsToDtos(clientService.findAll()));
    }
}
