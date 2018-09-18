class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception

  def show
    render template: 'assignment1'
  end

  ActionController::Parameters.action_on_unpermitted_parameters = :raise

  def validate_params
    activity = Validate::Location.new(params)
    if !activity.valid?
      render json: { error: activity.errors }
    end
  end

  rescue_from(ActionController::UnpermittedParameters) do |pme|
    render json: { error: { unknown_parameters: pme.params } },
           status: :bad_request
  end

end
