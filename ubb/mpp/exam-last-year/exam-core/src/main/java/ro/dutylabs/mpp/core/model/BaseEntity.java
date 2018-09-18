package ro.dutylabs.mpp.core.model;

import javax.persistence.*;
import java.io.Serializable;

@MappedSuperclass
public abstract class BaseEntity<ID extends Serializable> implements Serializable {

    @Id
    @TableGenerator(name = "TABLE_GENERATOR", initialValue = 0, allocationSize = 1)
    @GeneratedValue(strategy = GenerationType.TABLE, generator = "TABLE_GENERATOR")
    @Column(name = "id", unique = true, nullable = false)
    private ID id;

    public ID getId() {
        return id;
    }

    public void setId(ID id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "BaseEntity{" +
                "id=" + id +
                '}';
    }
}
