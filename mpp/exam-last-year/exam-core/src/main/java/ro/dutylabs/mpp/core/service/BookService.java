package ro.dutylabs.mpp.core.service;

import ro.dutylabs.mpp.core.model.Author;
import ro.dutylabs.mpp.core.model.Book;

import java.util.List;

/**
 * Created by cosmin on 12/06/2017.
 */
public interface BookService {
    List<Book> findAll();
    Book createBook(String isbn, String title, int year, Author author);
    Book findOne(Long id);
    Book updateBook(Long id, String isbn, String title, int year, Author author);
    void deleteBook(Long id);
}
