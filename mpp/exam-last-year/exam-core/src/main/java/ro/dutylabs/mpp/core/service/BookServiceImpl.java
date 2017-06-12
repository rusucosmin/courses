package ro.dutylabs.mpp.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ro.dutylabs.mpp.core.model.Author;
import ro.dutylabs.mpp.core.model.Book;
import ro.dutylabs.mpp.core.repository.BookRepository;

import java.util.List;

/**
 * Created by cosmin on 12/06/2017.
 */
@Service
public class BookServiceImpl implements BookService {
    @Autowired
    private BookRepository bookRepository;

    @Override
    public List<Book> findAll() {
        return bookRepository.findAll();
    }

    @Override
    public Book createBook(String isbn, String title, int year, Author author) {
        Book book = Book.builder()
                .isbn(isbn)
                .title(title)
                .year(year)
                .author(author)
                .build();
        book = bookRepository.save(book);
        return book;
    }

    @Override
    public Book findOne(Long id) {
        return bookRepository.getOne(id);
    }

    @Override
    @Transactional
    public Book updateBook(Long id, String isbn, String title, int year, Author author) {
        Book book = bookRepository.getOne(id);
        book.setIsbn(isbn);
        book.setTitle(title);
        book.setAuthor(author);
        return book;
    }

    @Override
    public void deleteBook(Long id) {
        bookRepository.delete(id);
    }
}
