package model;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.apache.commons.lang3.builder.ToStringBuilder;

/**
 * Created by cosmin on 10/7/16.
 */
public class Bicycle implements Vehicle {
    private String color;
    private String type;
    private double wheelSize;

    public Bicycle(String type, String color, double wheelSize) {
        this.type = type;
        this.color = color;
        this.wheelSize = wheelSize;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (!(o instanceof Bicycle)) return false;

        Bicycle bicycle = (Bicycle) o;

        return new EqualsBuilder()
                .append(wheelSize, bicycle.wheelSize)
                .append(color, bicycle.color)
                .append(type, bicycle.type)
                .isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder(17, 37)
                .append(color)
                .append(type)
                .append(wheelSize)
                .toHashCode();
    }

    @Override
    public String toString() {
        ToStringBuilder builder = new ToStringBuilder(this)
                .append(this.color)
                .append(this.type)
                .append(this.wheelSize);
        return builder.build();
    }

    @Override
    public String getColor() {
        return this.color;
    }

    public String getType() {
        return type;
    }

    public double getWheelSize() {
        return wheelSize;
    }
}
