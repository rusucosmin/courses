package ro.dutylabs.mpp.core.service;

import ro.dutylabs.mpp.core.model.Author;

import java.util.List;
import java.util.Set;

/**
 * Created by cosmin on 11/06/2017.
 */
public interface AuthorService {
    List<Author> findAll();
    Author createAuthor(String name);
    Author findOne(Long id);
    Author updateAuthor(Long id, String name, Set<Long> books);
    void deleteAuthor(Long id);
    Author addBook(Long id, String isbn, String title, int year);
}
