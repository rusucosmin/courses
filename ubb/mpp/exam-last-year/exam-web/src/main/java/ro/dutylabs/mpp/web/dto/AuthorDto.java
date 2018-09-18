package ro.dutylabs.mpp.web.dto;

import lombok.*;

import java.util.Set;

/**
 * Created by cosmin on 11/06/2017.
 */
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
@ToString
public class AuthorDto extends BaseDto {
    private String name;
    private Set<BookDto> books;
}
