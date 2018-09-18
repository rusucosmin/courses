package ro.dutylabs.mpp.web.converter;

import ro.dutylabs.mpp.core.model.BaseEntity;
import ro.dutylabs.mpp.web.dto.BaseDto;

import java.util.Set;
import java.util.stream.Collectors;

public abstract class BaseConverter<Model extends BaseEntity<Long>, Dto extends BaseDto>
            extends BaseConverterGeneric<Model, Dto> implements Converter<Model, Dto> {

    public Set<Long> convertModelsToIDs(Set<Model> models) {
        return models.stream()
                .map(model -> model.getId())
                .collect(Collectors.toSet());
    }

    public Set<Long> convertDTOsToIDs(Set<Dto> dtos) {
        return dtos.stream()
                .map(dto -> dto.getId())
                .collect(Collectors.toSet());
    }
}
