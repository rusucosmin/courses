package ro.dutylabs.mpp.web.converter;

import org.springframework.stereotype.Component;
import ro.dutylabs.mpp.core.model.Book;
import ro.dutylabs.mpp.web.dto.BookDto;

/**
 * Created by cosmin on 12/06/2017.
 */
@Component
public class BookConverter extends BaseConverter<Book, BookDto> {
    @Override
    public Book convertDtoToModel(BookDto bookDto) {
        Book book = Book.builder()
                .isbn(bookDto.getIsbn())
                .title(bookDto.getTitle())
                .year(bookDto.getYear())
                .build();
        book.setId(bookDto.getId());
        return book;
    }

    @Override
    public BookDto convertModelToDto(Book book) {
        BookDto bookDto = BookDto.builder()
                .isbn(book.getIsbn())
                .title(book.getTitle())
                .year(book.getYear())
                .build();
        bookDto.setId(book.getId());
        return bookDto;
    }
}
