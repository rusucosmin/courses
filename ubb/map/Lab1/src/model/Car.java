package model;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.apache.commons.lang3.builder.ToStringBuilder;

/**
 * Created by cosmin on 10/7/16.
 */
public class Car implements Vehicle {
    private String color;
    private String brand;
    private String type;
    private String name;

    public Car(String type, String brand, String name, String color) {
        this.type = type;
        this.brand = brand;
        this.name = name;
        this.color = color;
    }

    public String getBrand() {
        return brand;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setType(String type) {
        this.type = type;
    }

    @Override
    public String toString() {
        ToStringBuilder builder = new ToStringBuilder(this)
                .append(this.brand)
                .append(this.type)
                .append(this.name)
                .append(this.color);
        return builder.build();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (!(o instanceof Car)) return false;

        Car car = (Car) o;

        return new EqualsBuilder()
                .append(color, car.color)
                .append(brand, car.brand)
                .append(type, car.type)
                .append(name, car.name)
                .isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder(17, 37)
                .append(color)
                .append(brand)
                .append(type)
                .append(name)
                .toHashCode();
    }

    @Override
    public String getColor() {
        return color;
    }
}
