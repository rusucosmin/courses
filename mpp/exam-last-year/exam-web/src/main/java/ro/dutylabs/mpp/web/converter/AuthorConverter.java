package ro.dutylabs.mpp.web.converter;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import ro.dutylabs.mpp.core.model.Author;
import ro.dutylabs.mpp.web.dto.AuthorDto;

import java.util.HashSet;

/**
 * Created by cosmin on 11/06/2017.
 */
@Component
public class AuthorConverter extends BaseConverter<Author, AuthorDto> {
    @Autowired
    private BookConverter bookConverter;
    @Override
    public Author convertDtoToModel(AuthorDto authorDto) {
        Author client = Author.builder()
                .name(authorDto.getName())
                .books(new HashSet<>())
                .build();
        client.setId(authorDto.getId());
        return client;
    }

    @Override
    public AuthorDto convertModelToDto(Author client) {
        AuthorDto clientdto = AuthorDto.builder()
                .name(client.getName())
                .books(bookConverter.convertModelsToDtos(client.getBooks()))
                .build();
        clientdto.setId(client.getId());
        return clientdto;
    }
}
