package ro.dutylabs.mpp.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ro.dutylabs.mpp.core.model.Author;
import ro.dutylabs.mpp.core.model.Book;
import ro.dutylabs.mpp.core.repository.AuthorRepository;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Created by cosmin on 11/06/2017.
 */
@Service
public class AuthorServiceImpl implements AuthorService {

    private static final Logger log = LoggerFactory.getLogger(AuthorServiceImpl.class);

    @Autowired
    private AuthorRepository authorRepository;
    @Autowired
    private BookService bookService;

    @Override
    public List<Author> findAll() {
        return authorRepository.findAll();
    }

    @Override
    public Author createAuthor(String name) {
        Author author = Author.builder()
                .name(name)
                .books(new HashSet<>())
                .build();
        author = authorRepository.save(author);
        return author;
    }

    @Override
    public Author findOne(Long id) {
        return authorRepository.getOne(id);
    }

    @Override
    @Transactional
    public Author updateAuthor(Long id, String name, Set<Long> books) {
        Author author = authorRepository.getOne(id);
        author.setName(name);
        /// TODO: updatea books of client with id 'id' based on ids from books
        /// not needed for the exam
        return author;
    }

    @Override
    public void deleteAuthor(Long id) {
        authorRepository.delete(id);
    }

    @Override
    @Transactional
    public Author addBook(Long id, String isbn, String title, int year) {
        Book book = bookService.createBook(isbn, title, year, authorRepository.getOne(id));
        authorRepository.getOne(id).getBooks().add(book);
        return authorRepository.getOne(id);
    }
}
