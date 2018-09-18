package ro.dutylabs.mpp.web.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.Set;

/**
 * Created by cosmin on 12/06/2017.
 */
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
public class BooksDto {
    private Set<BookDto> books;
}
