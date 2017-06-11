package ro.dutylabs.mpp.web.converter;

import org.springframework.stereotype.Component;
import ro.dutylabs.mpp.core.model.Client;
import ro.dutylabs.mpp.web.dto.ClientDto;

/**
 * Created by cosmin on 11/06/2017.
 */
@Component
public class ClientConverter extends BaseConverter<Client, ClientDto> {
    @Override
    public Client convertDtoToModel(ClientDto clientDto) {
        Client client = Client.builder()
                .name(clientDto.getName())
                .build();
        client.setId(clientDto.getId());
        return client;
    }

    @Override
    public ClientDto convertModelToDto(Client client) {
        ClientDto clientdto = ClientDto.builder()
                .name(client.getName())
                .build();
        clientdto.setId(client.getId());
        return clientdto;
    }
}
