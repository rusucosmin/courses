require 'test_helper'

class EncryptFlowTest < ActionDispatch::IntegrationTest
  test "user encrypting with default parameters" do
    # user gets to the home page
    get "/"
    assert_equal 200, status
  end
end
