package model;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.apache.commons.lang3.builder.ToStringBuilder;

/**
 * Created by cosmin on 10/7/16.
 */
public class Motorcyle implements Vehicle {
    private String color;
    private String brand;
    private String name;
    private double maxSpeed;

    public Motorcyle(String brand, String name, String color, double maxSpeed) {
        this.brand = brand;
        this.name = name;
        this.color = color;
        this.maxSpeed = maxSpeed;
    }

    @Override
    public String toString() {
        ToStringBuilder builder = new ToStringBuilder(this)
                .append(this.brand)
                .append(this.name)
                .append(this.color)
                .append(this.maxSpeed);
        return builder.build();
    }

    public String getBrand() {
        return brand;
    }

    public String getName() {
        return name;
    }

    public double getMaxSpeed() {
        return maxSpeed;
    }

    @Override
    public int hashCode() {
        HashCodeBuilder builder = new HashCodeBuilder()
                .append(this.brand)
                .append(this.name)
                .append(this.color)
                .append(this.maxSpeed);
        return builder.build();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (!(o instanceof Motorcyle)) return false;

        Motorcyle motorcyle = (Motorcyle) o;

        return new EqualsBuilder()
                .append(maxSpeed, motorcyle.maxSpeed)
                .append(color, motorcyle.color)
                .append(brand, motorcyle.brand)
                .append(name, motorcyle.name)
                .isEquals();
    }

    @Override
    public String getColor() {
        return this.color;
    }
}
