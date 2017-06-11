package ro.dutylabs.mpp.web.dto;

import lombok.*;

/**
 * Created by cosmin on 11/06/2017.
 */
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
@ToString
public class ClientDto extends BaseDto {
    private String name;
}
