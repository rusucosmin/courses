package ro.dutylabs.mpp.web.converter;

import ro.dutylabs.mpp.core.model.BaseEntity;
import ro.dutylabs.mpp.web.dto.BaseDto;

public interface Converter<Model extends BaseEntity<Long>, Dto extends BaseDto>
        extends ConverterGeneric<Model, Dto> {
}