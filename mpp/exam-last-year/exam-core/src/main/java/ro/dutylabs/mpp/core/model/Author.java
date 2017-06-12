package ro.dutylabs.mpp.core.model;

import lombok.*;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "authors")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Author extends BaseEntity<Long> {
    @Column(name = "name", nullable = false)
    private String name;
    @OneToMany(mappedBy="author", cascade = CascadeType.ALL, fetch=FetchType.LAZY)
    private Set<Book> books = new HashSet<>();
}

