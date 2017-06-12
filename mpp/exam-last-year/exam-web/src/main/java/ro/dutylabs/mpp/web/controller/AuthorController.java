package ro.dutylabs.mpp.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;
import ro.dutylabs.mpp.core.model.Author;
import ro.dutylabs.mpp.core.service.AuthorService;
import ro.dutylabs.mpp.core.service.BookService;
import ro.dutylabs.mpp.web.converter.AuthorConverter;
import ro.dutylabs.mpp.web.dto.AuthorDto;
import ro.dutylabs.mpp.web.dto.AuthorsDto;
import ro.dutylabs.mpp.web.dto.BookDto;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by cosmin on 11/06/2017.
 */
@RestController
public class AuthorController {
    @Autowired
    private AuthorService authorService;
    @Autowired
    private BookService bookService;
    @Autowired
    private AuthorConverter authorConverter;

    private static final Logger log = LoggerFactory.getLogger(AuthorController.class);

    @RequestMapping(value = "/authors", method = RequestMethod.GET)
    @Transactional
    public AuthorsDto getAll() {
        log.trace("AuthorController::getAll()");
        System.out.println("AuthorController::getAll()");
        AuthorsDto authorsDto = new AuthorsDto(authorConverter.convertModelsToDtos(authorService.findAll()));
        log.trace("DONE: AuthorController::getAll()");
        return authorsDto;
    }

    @RequestMapping(value = "/authors", method = RequestMethod.POST)
    public Map<String, AuthorDto> createAuthor(@RequestBody final Map<String, AuthorDto> clientDtoMap) {
        log.trace("AuthorController()::createAuthor");
        log.trace(String.valueOf(clientDtoMap));
        AuthorDto authorDto = clientDtoMap.get("author");
        Author author = authorService.createAuthor(authorDto.getName());
        Map<String, AuthorDto> result = new HashMap<>();
        result.put("author", authorConverter.convertModelToDto(author));
        return result;
    }

    @RequestMapping(value = "/authors/{authorId}", method = RequestMethod.PUT)
    @Transactional
    public Map<String, AuthorDto> addBook(
            @PathVariable final Long authorId,
            @RequestBody final Map<String, BookDto> bookDtoMap) {
        log.trace("AuthorController()::addBook()");
        log.trace(String.valueOf(authorId));
        log.trace(String.valueOf(bookDtoMap));
        BookDto bookDto = bookDtoMap.get("book");
        Author author = authorService.addBook(authorId, bookDto.getIsbn(), bookDto.getTitle(), bookDto.getYear());
        Map<String, AuthorDto> result = new HashMap<>();
        result.put("author", authorConverter.convertModelToDto(author));
        return result;
    }

}
