package ro.dutylabs.mpp.web.dto;

import lombok.*;

import java.io.Serializable;

/**
 * Created by cosmin on 11/06/2017.
 */
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class BaseDto implements Serializable {
    private Long id;
}
