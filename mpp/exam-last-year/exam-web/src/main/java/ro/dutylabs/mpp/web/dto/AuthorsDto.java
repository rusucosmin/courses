package ro.dutylabs.mpp.web.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.io.Serializable;
import java.util.Set;

/**
 * Created by cosmin on 11/06/2017.
 */
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
public class AuthorsDto implements Serializable {
    private Set<AuthorDto> authors;
}
