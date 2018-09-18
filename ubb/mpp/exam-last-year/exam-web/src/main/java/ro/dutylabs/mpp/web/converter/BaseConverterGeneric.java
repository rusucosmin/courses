package ro.dutylabs.mpp.web.converter;

import java.util.Collection;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * Created by cosmin on 23/05/2017.
 */

public abstract class BaseConverterGeneric<Model, Dto> implements ConverterGeneric<Model, Dto> {
    public Set<Dto> convertModelsToDtos(Collection<Model> models) {
        return models.stream()
                .map(model -> convertModelToDto(model))
                .collect(Collectors.toSet());
    }

    public Set<Model> convertDtosToModel(Collection<Dto> dtos) {
        return dtos.stream()
                .map(dto -> convertDtoToModel(dto))
                .collect(Collectors.toSet());
    }
}
