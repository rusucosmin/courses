class CryptoController < ActionController::API
  before_action :validate_params

  ActionController::Parameters.action_on_unpermitted_parameters = :raise

#  api :GET, "/encrypt"
#  param :alphabet, String, :desc => "The alphabet to be used when encrypting", :required => true
#  param :alpha, Integer, :desc => "First element of the encrypting key", :required => true
#  param :beta, Integer, :desc => "Second element of the encrypting key", :required => true
#  param :text, String, :desc => "Text to be encrypted" , :required => true
  def encrypt
    render json: {  :alphabet => @cipher.alphabet,
                    :alpha => @cipher.alpha,
                    :beta => @cipher.beta,
                    :text => @cipher.text,
                    :encrypted => @cipher.encrypt }
  end


#  api :GET, "/decrypt"
#  param :alphabet, String, :desc => "The alphabet to be used when encrypting", :required => true
#  param :alpha, Integer, :desc => "First element of the encrypting key", :required => true
#  param :beta, Integer, :desc => "Second element of the encrypting key", :required => true
#  param :text, String, :desc => "Text to be encrypted" , :required => true
  def decrypt
    render json: {  :alphabet => @cipher.alphabet,
                    :alpha => @cipher.alpha,
                    :beta => @cipher.beta,
                    :text => @cipher.text,
                    :decrypted => @cipher.decrypt }
  end

  rescue_from(ActionController::UnpermittedParameters) do |pme|
    render json: { error:  { unknown_parameters: pme.params } },
             status: :bad_request
  end

private

    def validate_params
      @cipher = Cipher.new get_params
      if !@cipher.valid?
        render json: { error: @cipher.errors } and return
      end
    end

    def get_params
      print "get_params"
      params.permit(:text, :alphabet, :alpha, :beta)
    end
end
