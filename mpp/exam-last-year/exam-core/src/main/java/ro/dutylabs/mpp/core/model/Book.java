package ro.dutylabs.mpp.core.model;

import lombok.*;

import javax.persistence.*;

/**
 * Created by cosmin on 12/06/2017.
 */
@Entity
@Table(name = "books")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Book extends BaseEntity<Long> {
    @Column(name = "isbn")
    private String isbn;
    @Column(name = "title")
    private String title;
    @Column(name = "year")
    private int year;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="author_id", nullable = false)
    private Author author;
}
