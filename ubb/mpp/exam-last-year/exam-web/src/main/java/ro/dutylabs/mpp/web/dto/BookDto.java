package ro.dutylabs.mpp.web.dto;

import lombok.*;

/**
 * Created by cosmin on 12/06/2017.
 */
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
@ToString
public class BookDto extends BaseDto {
    private String isbn;
    private String title;
    private int year;
}
