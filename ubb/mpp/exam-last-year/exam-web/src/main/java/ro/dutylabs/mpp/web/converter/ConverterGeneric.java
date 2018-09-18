package ro.dutylabs.mpp.web.converter;

/**
 * Created by cosmin on 23/05/2017.
 */
public interface ConverterGeneric<Model, Dto> {
    Model convertDtoToModel(Dto dto);

    Dto convertModelToDto(Model model);
}
